# Intermediate Code Generation Program

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}


# -----------------------------
# INFIX TO POSTFIX
# -----------------------------
def infix_to_postfix(expression):

    stack = []
    postfix = ""

    for ch in expression:

        # Operand
        if ch.isalnum():

            postfix += ch

        # Opening bracket
        elif ch == '(':

            stack.append(ch)

        # Closing bracket
        elif ch == ')':

            while stack and stack[-1] != '(':
                postfix += stack.pop()

            stack.pop()

        # Operator
        else:

            while (stack and stack[-1] != '(' and
                   precedence[ch] <= precedence[stack[-1]]):

                postfix += stack.pop()

            stack.append(ch)

    while stack:
        postfix += stack.pop()

    return postfix


# -----------------------------
# INFIX TO PREFIX
# -----------------------------
def infix_to_prefix(expression):

    # Reverse expression
    expression = expression[::-1]

    temp = ""

    # Swap brackets
    for ch in expression:

        if ch == '(':
            temp += ')'

        elif ch == ')':
            temp += '('

        else:
            temp += ch

    postfix = infix_to_postfix(temp)

    prefix = postfix[::-1]

    return prefix


# -----------------------------
# QUADRUPLES
# -----------------------------
def generate_quadruples(postfix):

    stack = []

    temp_count = 1

    print("\nQUADRUPLES\n")

    print("Operator\tArg1\tArg2\tResult\n")

    for ch in postfix:

        if ch.isalnum():

            stack.append(ch)

        else:

            op2 = stack.pop()
            op1 = stack.pop()

            result = "T" + str(temp_count)

            print(ch, "\t\t", op1, "\t", op2, "\t", result)

            stack.append(result)

            temp_count += 1


# -----------------------------
# TRIPLES
# -----------------------------
def generate_triples(postfix):

    stack = []

    index = 0

    print("\nTRIPLES\n")

    print("Index\tOperator\tArg1\tArg2\n")

    for ch in postfix:

        if ch.isalnum():

            stack.append(ch)

        else:

            op2 = stack.pop()
            op1 = stack.pop()

            print(index, "\t", ch, "\t\t", op1, "\t", op2)

            stack.append("(" + str(index) + ")")

            index += 1


# -----------------------------
# MAIN PROGRAM
# -----------------------------

expression = input("Enter infix expression:\n")

# Remove spaces
expression = expression.replace(" ", "")

postfix = infix_to_postfix(expression)

prefix = infix_to_prefix(expression)

print("\nPostfix Expression:", postfix)

print("Prefix Expression:", prefix)

generate_quadruples(postfix)

generate_triples(postfix)