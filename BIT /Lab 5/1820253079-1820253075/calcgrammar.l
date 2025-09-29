%{
#include "calcgrammar.tab.h"
#include <stdlib.h>
#include <stdio.h>
%}

%%
[0-9]+\.[0-9]+    { yylval.u_float = atof(yytext); return VALf; }
[0-9]+            { yylval.u_int   = atoi(yytext); return VALi; }
"+"               { return PLUS; }
"-"               { return MINUS; }
"*"               { return MULT; }
"/"               { return DIV; }
"%"               { return MOD; }
"^"               { return POWER; }
"("               { return LBRAC; }
")"               { return RBRAC; }
";"               { return SEMI; }
[ \t\n\r]+        { /* skip whitespace */ }
.                 { return yytext[0]; }
%%

int yywrap() {
    return 1;
}
