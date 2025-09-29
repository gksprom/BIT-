%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

extern FILE *yyin;
extern int yylex();
void yyerror(const char *s);

%}

%union {
    int u_int;
    float u_float;
}

%token <u_int> VALi
%token <u_float> VALf
%token PLUS MINUS MULT DIV MOD POWER LBRAC RBRAC SEMI

%type <u_float> expr term factor

%left PLUS MINUS
%left MULT DIV MOD
%right POWER

%start prog

%%

prog:
    stmt_list
;

stmt_list:
    stmt_list stmt
    | stmt
;

stmt:
    expr SEMI { printf("%f\n", $1); }
;

expr:
    expr PLUS term { $$ = $1 + $3; }
    | expr MINUS term { $$ = $1 - $3; }
    | term
;

term:
    term MULT factor { $$ = $1 * $3; }
    | term DIV factor { 
        if ($3 == 0) {
            yyerror("division by zero");
            $$ = 0;
        } else {
            $$ = $1 / $3;
        }
    }
    | term MOD factor { $$ = (int)$1 % (int)$3; }
    | factor
;

factor:
    LBRAC expr RBRAC { $$ = $2; }
    | VALi { $$ = $1; }
    | VALf { $$ = $1; }
    | factor POWER factor { $$ = pow($1, $3); }
;

%%

void yyerror(const char *s) {
    printf("Error: %s\n", s);
}

int main() {
    yyin = fopen("inputfile.txt", "r");
    if (!yyin) {
        perror("Error opening input file");
        return 1;
    }

    yyparse();
    fclose(yyin);
    return 0;
}
