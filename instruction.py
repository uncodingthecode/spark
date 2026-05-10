# Loader / Linker Program

locctr = 0

extdef = []
extref = []

symbol_table = {}

n = int(input("Enter number of lines in ASM program: "))

program = []

print("\nEnter ASM Program:\n")

for _ in range(n):

    line = input()

    program.append(line)


# -----------------------------
# PROCESS PROGRAM
# -----------------------------

for line in program:

    words = line.split()

    if len(words) == 0:
        continue

    # START
    if "START" in words:

        locctr = int(words[-1])

    # EXTDEF
    elif words[0] == "EXTDEF":

        symbols = " ".join(words[1:]).replace(",", " ").split()

        extdef.extend(symbols)

    # EXTREF
    elif words[0] == "EXTREF":

        symbols = " ".join(words[1:]).replace(",", " ").split()

        extref.extend(symbols)

    # END
    elif words[0] == "END":

        break

    # Instructions
    else:

        # Check label
        label = words[0]

        # If label exists
        if label not in ["ADD", "SUB", "MUL", "DIV"]:

            symbol_table[label] = locctr

        # each instruction = 3 bytes
        locctr += 3


# -----------------------------
# GENERATE D RECORD
# -----------------------------

d_record = "D"

for symbol in extdef:

    if symbol in symbol_table:

        address = str(symbol_table[symbol]).zfill(6)

        d_record += "^" + symbol + "^" + address


# -----------------------------
# GENERATE R RECORD
# -----------------------------

r_record = "R"

for symbol in extref:

    r_record += "^" + symbol


# -----------------------------
# PRINT OUTPUT
# -----------------------------

print("\nD RECORD")

print(d_record)

print("\nR RECORD")

print(r_record)

print("\nLOCAL SYMBOL TABLE\n")

print("Symbol Name\tValue")

for symbol in symbol_table:

    print(symbol, "\t\t", str(symbol_table[symbol]).zfill(6))