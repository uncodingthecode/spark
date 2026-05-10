import re

keywords = [
    "int","float","char","double","if","else","for","while",
    "switch","case","break","return","void","const","static",
    "struct","union","typedef","enum","sizeof","do","goto",
    "continue","volatile","register","extern","signed","unsigned"
]

operators = [
    "+","-","*","/","=","==","!=","<",">","<=",">="
]

delimiters = ["(", ")", "{", "}", ";", ","]

print("Enter a C program (Write END to finish):")

lines = []

while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

program = "\n".join(lines)

# Regex for tokenization
tokens = re.findall(
    r'[A-Za-z_][A-Za-z0-9_]*'      # identifiers/keywords
    r'|\d+'                        # numbers
    r'|==|!=|<=|>='               # double operators
    r'|[+\-*/=<>]'                # single operators
    r'|[{}();,]',                 # delimiters
    program
)

for token in tokens:

    if token in keywords:
        print(token, "-> Keyword")

    elif token in operators:
        print(token, "-> Operator")

    elif token in delimiters:
        print(token, "-> Delimiter")

    elif re.fullmatch(r'\d+', token):
        print(token, "-> Number")

    elif re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', token):
        print(token, "-> Identifier")

    else:
        print(token, "-> Invalid Token")