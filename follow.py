# FOLLOW Set for Multiple Productions

grammar = {}

n = int(input("Enter number of productions: "))

for _ in range(n):

    production = input("Enter production (Example S->AB): ")

    lhs, rhs = production.split("->")

    grammar[lhs] = rhs.split("|")


follow = {}

for non_terminal in grammar:
    follow[non_terminal] = set()

# Start symbol gets $
start_symbol = list(grammar.keys())[0]
follow[start_symbol].add('$')


for lhs in grammar:

    for prod in grammar[lhs]:

        for i in range(len(prod)):

            symbol = prod[i]

            if symbol.isupper():

                # if next symbol exists
                if i+1 < len(prod):

                    next_symbol = prod[i+1]

                    follow[symbol].add(next_symbol)

                else:

                    follow[symbol] = follow[symbol].union(follow[lhs])


for non_terminal in follow:

    print("FOLLOW(", non_terminal, ") = ", follow[non_terminal])