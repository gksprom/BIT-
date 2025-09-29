%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "parsetree.h"
#include "ir.h"

int yylex(void);
void yyerror(const char *s);
%}

%start input

%union {
    char *sval;
    struct TreeNode *node;
}

%token <sval> ID
%token <sval> INT FLOAT
%token ASSIGN NEWLINE
%token PLUS MINUS MUL DIV MOD POW LPAREN RPAREN
%type <node> expr stmt input
%type <node> opt_newline


%left PLUS MINUS
%left MUL DIV MOD
%right POW

%%

input: input stmt
     | stmt
     ;

opt_newline: NEWLINE
           | /* empty */ ;

stmt: ID ASSIGN expr opt_newline {
    TreeNode *root = mkTree("=", mkTree($1, NULL, NULL), $3);
    char *dummy;
    List ir = IRGenModule(root, &dummy);
    printList(ir);
}
;

expr: expr PLUS expr     { $$ = mkTree("+", $1, $3); }
    | expr MINUS expr    { $$ = mkTree("-", $1, $3); }
    | expr MUL expr      { $$ = mkTree("*", $1, $3); }
    | expr DIV expr      { $$ = mkTree("/", $1, $3); }
    | expr MOD expr      { $$ = mkTree("%", $1, $3); }
    | expr POW expr      { $$ = mkTree("^", $1, $3); }
    | LPAREN expr RPAREN { $$ = $2; }
    | INT                { $$ = mkTree($1, NULL, NULL); }
    | FLOAT              { $$ = mkTree($1, NULL, NULL); }
    | ID                 { $$ = mkTree($1, NULL, NULL); }
;

%%

int main(int argc, char **argv) {
    extern FILE *yyin;
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            perror("fopen");
            return 1;
        }
    }
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    fprintf(stderr, "Parse error: %s\n", s);
}
