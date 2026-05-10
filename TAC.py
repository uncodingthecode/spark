# Basic Block Generation from TAC

n = int(input("Enter number of TAC statements: "))

statements = []

print("\nEnter TAC statements:\n")

for i in range(n):

    stmt = input()

    statements.append(stmt)


# -----------------------------
# FIND LEADERS
# -----------------------------

leaders = set()

# First statement is always a leader
leaders.add(0)

for i in range(len(statements)):

    stmt = statements[i]

    words = stmt.split()

    # If goto exists
    if "goto" in words:

        target = int(words[-1]) - 1

        # Target statement is a leader
        leaders.add(target)

        # Next statement is also a leader
        if i + 1 < len(statements):
            leaders.add(i + 1)


leaders = sorted(leaders)

# -----------------------------
# FORM BASIC BLOCKS
# -----------------------------

basic_blocks = []

for i in range(len(leaders)):

    start = leaders[i]

    # Last leader
    if i == len(leaders) - 1:

        end = len(statements)

    else:

        end = leaders[i + 1]

    block = statements[start:end]

    basic_blocks.append(block)


# -----------------------------
# PRINT BASIC BLOCKS
# -----------------------------

print("\nNumber of Basic Blocks:", len(basic_blocks))

print("\nBASIC BLOCKS:\n")

for i in range(len(basic_blocks)):

    print("Basic Block", i + 1)

    for stmt in basic_blocks[i]:

        print(stmt)

    print()