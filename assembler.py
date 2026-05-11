symbol_table = {}

location_counter = 0
start_address = 0
program_name = ""

lines = []

n = int(input("Enter number of lines: "))

print("\nEnter Assembly Program:\n")

for i in range(n):
    lines.append(input())


# -------------------------
# PASS 1 (Symbol Table + Addressing)
# -------------------------

for line in lines:

    parts = line.split()

    if len(parts) == 0:
        continue

    # START statement
    if "START" in parts:
        program_name = parts[0]
        start_address = int(parts[2], 16)
        location_counter = start_address
        continue

    # END statement
    if parts[0] == "END":
        break

    # Label present
    if len(parts) == 3:
        label = parts[0]
        symbol_table[label] = hex(location_counter)

        opcode = parts[1]
        location_counter += 3   # assuming all instructions = 3 bytes

    # No label
    else:
        opcode = parts[0]
        location_counter += 3


# -------------------------
# HEADER RECORD (H)
# -------------------------

program_length = location_counter - start_address

print("\n--------------------")
print("SYMBOL TABLE")
print("--------------------")

print("SYMBOL\tADDRESS")
for sym in symbol_table:
    print(sym, "\t", symbol_table[sym])


print("\n--------------------")
print("H RECORD")
print("--------------------")

print("H", program_name, hex(start_address), hex(program_length))


# -------------------------
# END RECORD (E)
# -------------------------

print("\n--------------------")
print("E RECORD")
print("--------------------")

print("E", hex(start_address))