%{
#include "parsetree.h"
#include <stdio.h>

extern FILE *yyin;
void yyerror(const char *s);
int yylex(void);
extern TreeNode* root;
%}

%union {
    double dval;
    char* sval;
    TreeNode* node;
}

%token NEWLINE
%token <dval> VALf
%token <sval> ID
%token ASSIGN
%left '+' '-'
%left '*' '/' '%'
%right '^'

%type <node> expr
%type <node> stmt

%start program

%%

program:
    /* empty */
    | program stmt NEWLINE
    | program stmt
;

stmt:
    ID ASSIGN expr {
        $$ = mkTree("=", mkTree($1, NULL, NULL), $3);
        root = $$;  // Store in root for printing
        printTree(root, 0);
    }
;

expr:
    expr '+' expr { $$ = mkTree("+", $1, $3); }
    | expr '-' expr { $$ = mkTree("-", $1, $3); }
    | expr '*' expr { $$ = mkTree("*", $1, $3); }
    | expr '/' expr { $$ = mkTree("/", $1, $3); }
    | expr '%' expr { $$ = mkTree("%", $1, $3); }
    | expr '^' expr { $$ = mkTree("^", $1, $3); }
    | '(' expr ')' { $$ = $2; }
    | VALf {
        char buf[32];
        snprintf(buf, sizeof(buf), "%g", $1);
        $$ = mkTree(strdup(buf), NULL, NULL);
    }
    | ID { $$ = mkTree($1, NULL, NULL); }
;

%%

TreeNode* root = NULL;

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    yyin = fopen("math.txt", "r");
    if (!yyin) {
        perror("Error opening input");
        return 1;
    }
    
    if (yyparse() == 0) {
        printf("Parsing completed successfully\n");
    }
    fclose(yyin);
    return 0;
}