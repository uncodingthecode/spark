# Program Block Table Generation

block_table = {}

current_block = "DEFAULT"

block_number = 0

locctr = {}

# Default block
block_table[current_block] = {
    "Block Number": block_number,
    "Start Address": 0,
    "Length": 0
}

locctr[current_block] = 0


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

    # USE directive
    if words[0] == "USE":

        # Switch block
        if len(words) > 1:

            current_block = words[1]

        else:

            current_block = "DEFAULT"

        # New block creation
        if current_block not in block_table:

            block_number += 1

            block_table[current_block] = {
                "Block Number": block_number,
                "Start Address": 0,
                "Length": 0
            }

            locctr[current_block] = 0

    # Ignore START and END
    elif "START" in words or "END" in words:

        continue

    else:

        # Assume every instruction = 3 bytes
        locctr[current_block] += 3


# -----------------------------
# CALCULATE BLOCK LENGTHS
# -----------------------------

for block in block_table:

    block_table[block]["Length"] = locctr[block]


# -----------------------------
# CALCULATE START ADDRESSES
# -----------------------------

start = 0

for block in block_table:

    block_table[block]["Start Address"] = start

    start += block_table[block]["Length"]


# -----------------------------
# PRINT BLOCK TABLE
# -----------------------------

print("\nBLOCK TABLE\n")

print("Block Name\tBlock No\tStart Address\tLength\n")

for block in block_table:

    print(
        block,
        "\t\t",
        block_table[block]["Block Number"],
        "\t\t",
        str(block_table[block]["Start Address"]).zfill(6),
        "\t\t",
        str(block_table[block]["Length"]).zfill(6)
    )