grammar = {}

n = int(input("Enter number of productions: "))

for _ in range(n):

    production = input("Enter production (Example A->aB|b): ")

    lhs, rhs = production.split("->")

    grammar[lhs] = rhs.split("|")


def first(symbol):

    result = set()

    # terminal
    if not symbol.isupper():
        result.add(symbol)
        return result

    # non-terminal
    for prod in grammar[symbol]:

        first_char = prod[0]

        if first_char.isupper():

            result = result.union(first(first_char))

        else:

            result.add(first_char)

    return result


for non_terminal in grammar:

    print("FIRST(", non_terminal, ") = ", first(non_terminal))