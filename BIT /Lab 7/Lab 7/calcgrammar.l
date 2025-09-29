%{
#include "calcgrammar.tab.h"
#include <stdlib.h>
#include <string.h>
%}

FLOAT     [0-9]+\.[0-9]+
INT       [0-9]+
ID        [a-zA-Z_][a-zA-Z0-9_]*

%%

\n          { return NEWLINE; }
[ \t]+      ;
"="         { return ASSIGN; }
"+"         { return PLUS; }
"-"         { return MINUS; }
"*"         { return MUL; }
"/"         { return DIV; }
"%"         { return MOD; }
"^"         { return POW; }
"("         { return LPAREN; }
")"         { return RPAREN; }
{FLOAT}     { yylval.sval = strdup(yytext); return FLOAT; }
{INT}       { yylval.sval = strdup(yytext); return INT; }
{ID}        { yylval.sval = strdup(yytext); return ID; }
.           { fprintf(stderr, "Invalid character: %s\n", yytext); }

%%

int yywrap(void) {
    return 1;
}
