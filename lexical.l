%{
#include<stdio.h>
%}

KEYWORD    int|float|char|double|if|else|for|while|switch|case|break|return|void
ID         [a-zA-Z_][a-zA-Z0-9_]*
NUMBER     [0-9]+
OPERATOR   \+|\-|\*|\/|==|!=|<=|>=|=|<|>
DELIMITER  \(|\)|\{|\}|;|,

%%

{KEYWORD}     { printf("%s -> Keyword\n", yytext); }

{ID}          { printf("%s -> Identifier\n", yytext); }

{NUMBER}      { printf("%s -> Number\n", yytext); }

{OPERATOR}    { printf("%s -> Operator\n", yytext); }

{DELIMITER}   { printf("%s -> Delimiter\n", yytext); }

[ \t\n]+      ;    /* Ignore spaces */

.             { printf("%s -> Invalid Token\n", yytext); }

%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter program:\n");
    yylex();
    return 0;
}