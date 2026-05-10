# LL(1) Parser Simulation

# Input productions
grammar = {}

n = int(input("Enter number of productions: "))

print("\nEnter productions in format:")
print("E->T E'")

for _ in range(n):

    production = input()

    lhs, rhs = production.split("->")

    grammar[lhs.strip()] = rhs.strip()


# Input parsing table
parsing_table = {}

m = int(input("\nEnter number of parsing table entries: "))

print("\nEnter parsing table entries in format:")
print("NonTerminal Terminal Production")
print("Example: E id T E'\n")

for _ in range(m):

    entry = input().split()

    non_terminal = entry[0]
    terminal = entry[1]
    production = entry[2:]

    parsing_table[(non_terminal, terminal)] = production


# Start symbol
start_symbol = list(grammar.keys())[0]

# Input string
input_string = input("\nEnter input string separated by spaces:\n")

tokens = input_string.split()
tokens.append('$')

# Stack initialization
stack = ['$', start_symbol]

index = 0

print("\nSTACK\t\tINPUT\t\tACTION\n")

while True:

    top = stack[-1]
    current = tokens[index]

    print(stack, "\t", tokens[index:])

    # ACCEPT
    if top == current == '$':

        print("\nString Accepted")
        break

    # Terminal Match
    elif top == current:

        stack.pop()
        index += 1

    # Non-terminal
    elif (top, current) in parsing_table:

        production = parsing_table[(top, current)]

        stack.pop()

        print("Using Production:", top, "->", " ".join(production))

        # epsilon production
        if production != ['ε']:

            for symbol in reversed(production):
                stack.append(symbol)

    else:

        print("\nString Rejected")
        break