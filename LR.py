n = int(input("Enter number of productions: "))

grammar = {}
print("Enter the productions (e.g., A->Aa|b):")

for _ in range(n):
    production = input()
    lhs, rhs = production.split("->")
    grammar[lhs] = rhs.split("|")


for lhs in grammar:
    alpha = []
    beta = []

    for prod in grammar[lhs]:
        if prod.startswith(lhs):
            alpha.append(prod[len(lhs):])
        else:
            beta.append(prod)

    if alpha:
        print("\nAfter Removing Left Recursion:\n")
        print(lhs, "->", end=" ")

        for i in range(len(beta)):
            print(beta[i] + lhs + "'", end="")
            if i != len(beta)-1:
                print(" | ", end="")

        print()
        print(lhs + "'", "->", end=" ")

        for i in range(len(alpha)):
            print(alpha[i] + lhs + "'", end="")

            if i != len(alpha)-1:
                print(" | ", end="")

        print(" | ε")
    else:
        print("\nNo Left Recursion in", lhs)