import re

data = []

with open("inputs/day18.txt", "r") as f:
#with open("test/day18.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


def parse_1(expr_parts):
    left = 0
    current_op = ""
    i = 0
    while i < len(expr_parts):
        p = expr_parts[i]
        if not p == "+" and not p == "*" and not p == "(" and not p == ")":
            # Number
            if current_op == "+":
                left += int(p)
            elif current_op == "*":
                left *= int(p)
            else:
                left = int(p)

            current_op = ""
        elif p == "+":
            current_op = "+"
        elif p == "*":
            current_op = "*"
        elif p == "(":
            sub_expr = expr_parts[i + 1:]

            output = parse_1(sub_expr)

            if current_op == "+":
                left += output[0]
            elif current_op == "*":
                left *= output[0]
            else:
                left = output[0]

            expr_parts = output[1]
            i = 0

            current_op = ""
            continue
        elif p == ")":
            return left, expr_parts[i + 1:]
        else:
            print("broke!")

        i += 1

    return left, []


# Returns either a expr_parts list. If it's len is 1, it's just a number
def parse_2(expr_parts):
    i = 0
    did_op = False
    can_mul = False
    while len(expr_parts) > 1:
        if i >= len(expr_parts):  # Loop i around
            if not did_op:
                can_mul = True
            i = 0
            did_op = False
        p = expr_parts[i]

        if p == "(":
            did_op = True
            # Find matching )
            close_pos = 0
            paren_count = 0
            for c in range(i+1, len(expr_parts)):
                if expr_parts[c] == "(":
                    paren_count += 1
                elif expr_parts[c] == ")":
                    if paren_count == 0:
                        close_pos = c
                        break
                    else:
                        paren_count -= 1

            sub_expr = expr_parts[i + 1:close_pos]  # Just eval between the parenthesis

            # This returns the list in the form
            output = parse_2(sub_expr)

            if len(output) == 1:
                # Just a number
                expr_parts = expr_parts[:i] + output + expr_parts[close_pos+1:]
            else:
                # An actual expression, keep the parenthesis
                # expr_parts = expr_parts[:i+1] + output + expr_parts[close_pos:]
                print("aaaaaa")
        elif p == "+":
            did_op = True

            # If this doesn't work, something is wrong
            left = expr_parts[i-1]
            right = expr_parts[i+1]

            if isinstance(left, int) and isinstance(right, int):
                output = left + right
                expr_parts = expr_parts[:i - 1] + [output] + expr_parts[i + 2:]
                i -= 2
            elif re.fullmatch("\\d+", str(left)) and re.fullmatch("\\d+", str(right)):
                left = int(left)
                right = int(right)
                output = left + right
                expr_parts = expr_parts[:i - 1] + [output] + expr_parts[i + 2:]
                i -= 2
        elif p == "*" and can_mul:
            did_op = True

            # If this doesn't work, something is wrong
            left = expr_parts[i - 1]
            right = expr_parts[i + 1]

            if isinstance(left, int) and isinstance(right, int):
                output = left * right
                expr_parts = expr_parts[:i - 1] + [output] + expr_parts[i + 2:]
                i -= 2
            elif re.fullmatch("\\d+", str(left)) and re.fullmatch("\\d+", str(right)):
                left = int(left)
                right = int(right)
                output = left * right
                expr_parts = expr_parts[:i - 1] + [output] + expr_parts[i + 2:]
                i -= 2

        i += 1

    return expr_parts


total_sum = 0

for d in data:
    parts = []

    for c in d:
        if not c.strip() == "":
            parts.append(c)

    result = parse_1(parts)[0]
    total_sum += result
    # print(result)

print(total_sum)

total_sum_2 = 0

# Part 2
for d in data:
    parts = []

    for c in d:
        if not c.strip() == "":
            parts.append(c)

    result = parse_2(parts)[0]
    total_sum_2 += result
    # print(result)

print(total_sum_2)
