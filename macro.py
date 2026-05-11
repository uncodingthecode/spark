# Macro Processor Program

deftab = []
namtab = {}

n = int(input("Enter number of lines in ASM program: "))

program = []

print("\nEnter ASM program:\n")

for _ in range(n):

    line = input()

    program.append(line)


inside_macro = False
macro_name = ""

for i in range(len(program)):

    line = program[i].strip()

    # Start of macro
    if line == "MACRO":

        inside_macro = True

        macro_start = len(deftab)

        continue

    # Macro definition
    if inside_macro:

        # First line after MACRO = macro header
        if macro_name == "":

            macro_name = line.split()[0]

            namtab[macro_name] = [macro_start]

        deftab.append(line)

        # End of macro
        if line == "MEND":

            inside_macro = False
            namtab[macro_name] = [macro_start, len(deftab)-1]
            macro_name = ""


# -----------------------------
# PRINT DEFTAB
# -----------------------------

print("\nDEFTAB\n")

for i in range(len(deftab)):

    print(i, "\t", deftab[i])


# -----------------------------
# PRINT NAMTAB
# -----------------------------

print("\nNAMTAB\n")

print("Macro Name\tStart\tEnd")

for macro in namtab:

    print(macro, "\t\t", namtab[macro][0],"\t", namtab[macro][1])