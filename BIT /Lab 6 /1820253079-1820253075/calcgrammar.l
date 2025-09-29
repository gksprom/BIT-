%option noyywrap nounput noinput
%{
#include "parsetree.h"
#include "calcgrammar.tab.h"

%}

ID      [a-zA-Z_][a-zA-Z0-9_]*
FLOAT   [0-9]+\.[0-9]+
INT     [0-9]+

%%

\n          { return NEWLINE; }
[ \t]+      { /* ignore whitespace */ }
"="         { return ASSIGN; }
"+"         { return '+'; }
"-"         { return '-'; }
"*"         { return '*'; }
"/"         { return '/'; }
"%"         { return '%'; }
"^"         { return '^'; }
"("         { return '('; }
")"         { return ')'; }
{FLOAT}     { yylval.dval = atof(yytext); return VALf; }
{INT}       { yylval.dval = atof(yytext); return VALf; }
{ID}        { yylval.sval = strdup(yytext); return ID; }
.           { fprintf(stderr, "Invalid character: %s\n", yytext); }

%%