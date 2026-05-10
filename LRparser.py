# Shift Reduce Parser Simulation

# Input productions
n = int(input("Enter number of productions: "))

productions = []

print("\nEnter productions in format:")
print("E->E + E")
print("E->id\n")

for _ in range(n):

    production = input()

    lhs, rhs = production.split("->")

    rhs_symbols = rhs.strip().split()

    productions.append((lhs.strip(), rhs_symbols))


# Input string
input_string = input("\nEnter input string separated by spaces:\n")

tokens = input_string.split()
tokens.append('$')

stack = []

index = 0

print("\nSTACK\t\tINPUT\t\tACTION\n")

while True:

    reduced = False

    # SHIFT
    if index < len(tokens):

        stack.append(tokens[index])

        print(stack, "\t", tokens[index+1:], "\tSHIFT")

        index += 1

    # REDUCE
    while True:

        matched = False

        for lhs, rhs in productions:

            length = len(rhs)

            if stack[-length:] == rhs:

                print(stack, "\t", tokens[index:], f"\tREDUCE {lhs} -> {' '.join(rhs)}")

                stack = stack[:-length]

                stack.append(lhs)

                print(stack)

                matched = True
                reduced = True

                break

        if not matched:
            break

    # ACCEPT
    if stack == ['S'] and tokens[index-1] == '$':

        print("\nString Accepted")
        break

    # REJECT
    if index == len(tokens) and not reduced:

        if stack != ['S']:

            print("\nString Rejected")

        break