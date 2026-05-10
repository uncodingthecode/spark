# Simple Assembler Program

# OPTAB with instruction sizes
optab = {
    "LDA": 3,
    "STA": 3,
    "ADD": 3,
    "SUB": 3,
    "MUL": 3,
    "DIV": 3,
    "JMP": 3
}

# Input assembly program
n = int(input("Enter number of lines in assembly program: "))

program = []

print("\nEnter assembly instructions:")
print("Format: LABEL OPCODE OPERAND\n")

for _ in range(n):

    line = input().split()

    # Handle missing label
    if len(line) == 2:
        line = ['-', line[0], line[1]]

    program.append(line)


# -----------------------------
# PASS 1
# -----------------------------

symbol_table = {}

start_address = 0
locctr = 0
program_name = ""

for i in range(len(program)):

    label, opcode, operand = program[i]

    # START
    if opcode == "START":

        start_address = int(operand)
        locctr = start_address
        program_name = label

        continue

    # Add label to symbol table
    if label != '-':

        symbol_table[label] = locctr

    # Instruction
    if opcode in optab:

        locctr += optab[opcode]

    # WORD
    elif opcode == "WORD":

        locctr += 3

    # RESW
    elif opcode == "RESW":

        locctr += 3 * int(operand)

    # RESB
    elif opcode == "RESB":

        locctr += int(operand)

    # BYTE
    elif opcode == "BYTE":

        locctr += 1

    # END
    elif opcode == "END":

        break


program_length = locctr - start_address


# -----------------------------
# PRINT SYMBOL TABLE
# -----------------------------

print("\nSYMBOL TABLE\n")

print("Symbol\tValue")

for symbol in symbol_table:

    print(symbol, "\t", symbol_table[symbol])


# -----------------------------
# H RECORD
# -----------------------------

print("\nHEADER RECORD")

print("H^" + program_name +
      "^" + str(start_address) +
      "^" + str(program_length))


# -----------------------------
# E RECORD
# -----------------------------

print("\nEND RECORD")

print("E^" + str(start_address))