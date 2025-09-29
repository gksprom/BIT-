%{
#include <stdio.h>
#include <stdlib.h>

FILE *output_file;
%}

%option noyywrap

DIGIT      [0-9]
LETTER     [a-zA-Z_]
IDENTIFIER {LETTER}({LETTER}|{DIGIT})*
HEX        0[xX][0-9a-fA-F]+
OCTAL      0[0-7]+
FLOAT      {DIGIT}+"."{DIGIT}*
INTEGER    {DIGIT}+
CHAR       \'.\'
STRING     \"(\\.|[^\"])*\"
KEYWORDS   "int"|"return"|"void"|"while"|"typedef"|"static"|"struct"
OPERATORS  "=="|"!="|"<="|">="|">>"|"<<"|"&&"|"||"|"="|"+"|"-"|"*"|"/"|"&"
PUNCTUATION ";"|","|"("|")"|"{"|"}"|"["|"]"
PREPROCESSOR "#".* 

%%

{PREPROCESSOR}          { fprintf(output_file, "< PREPROCESSOR, %s >\n", yytext); printf("< PREPROCESSOR, %s >\n", yytext); }
{KEYWORDS}         { fprintf(output_file, "< KEYWORD, %s >\n", yytext); printf("< KEYWORD, %s >\n", yytext); }
{IDENTIFIER}       { fprintf(output_file, "< IDENTIFIER, %s >\n", yytext); printf("< IDENTIFIER, %s >\n", yytext); }
{HEX}              { fprintf(output_file, "< CONSTANT, %s >\n", yytext); printf("< CONSTANT, %s >\n", yytext); }
{OCTAL}            { fprintf(output_file, "< CONSTANT, %s >\n", yytext); printf("< CONSTANT, %s >\n", yytext); }
{FLOAT}            { fprintf(output_file, "< CONSTANT, %s >\n", yytext); printf("< CONSTANT, %s >\n", yytext); }
{INTEGER}          { fprintf(output_file, "< CONSTANT, %s >\n", yytext); printf("< CONSTANT, %s >\n", yytext); }
{CHAR}             { fprintf(output_file, "< CONSTANT, %s >\n", yytext); printf("< CONSTANT, %s >\n", yytext); }
{STRING}           { fprintf(output_file, "< STRING, %s >\n", yytext); printf("< STRING, %s >\n", yytext); }
{OPERATORS}        { fprintf(output_file, "< OPERATOR, %s >\n", yytext); printf("< OPERATOR, %s >\n", yytext); }
{PUNCTUATION}      { fprintf(output_file, "< PUNCTUATION, %s >\n", yytext); printf("< PUNCTUATION, %s >\n", yytext); }
"//".*             {  }
"/*"([^*]|[\r\n])*"*/"  { }
[ \t\n]+           {  }
.                  { fprintf(output_file, "< SPECIAL, %s >\n", yytext); printf("< SPECIAL, %s >\n", yytext); }

%%

int main() {
    output_file = fopen("output.txt", "w");
    if (!output_file) {
        perror("Failed for opening the file");
        return EXIT_FAILURE;
    }
    yylex();
    fclose(output_file);
    return EXIT_SUCCESS;
}
