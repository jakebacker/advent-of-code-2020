import re

data = []

with open("inputs/day19.txt", "r") as f:
#with open("test/day19.txt", "r") as f:
    data = f.read().split("\n")  # This part may change

rules = []


# This would work, but max recursion depth problems
def expr_gen(rule):
    if "\"" in rule:
        return rule[1:len(rule)-1]
    elif "|" in rule:
        left = rule.split("|")[0].strip()
        right = rule.split("|")[1].strip()
        left_expr = expr_gen(left)
        right_expr = expr_gen(right)

        return "(" + left_expr + "|" + right_expr + ")"
    else:
        expr = ""
        parts = rule.split(" ")
        for r in parts:
            if r.strip() == "":
                continue
            expr += expr_gen(rules[int(r)])
        return expr


rules_str = []
messages = []

for i in range(0, len(data)):
    if data[i].strip() == "":
        rules_str = data[:i]
        messages = data[i+1:]
        break

rules = [""]*len(rules_str)

for i in range(0, len(rules_str)):
    rule_num = int(rules_str[i].split(":")[0].strip())
    r = rules_str[i].split(":")[1].strip()

    rules[rule_num] = r


count = 0

expr = re.compile("^" + expr_gen(rules[0]))

for m in messages:
    result = expr.fullmatch(m)

    if result is not None:
        count += 1
        print(m)
print(count)


# REGEX: ^a(ab|ba)
# ^a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b

#  Pt2
'''
with open("test/day19pt2.txt", "r") as f:
    data = f.read().split("\n")  # This part may change

for i in range(0, len(data)):
    if data[i].strip() == "":
        rules_str = data[:i]
        messages = data[i+1:]
        break

rules = [""]*150

for i in range(0, len(rules_str)):
    rule_num = int(rules_str[i].split(":")[0].strip())
    r = rules_str[i].split(":")[1].strip()

    rules[rule_num] = r
'''
rules[8] = "42 | 42 8"
rules[11] = "42 31 | 42 11 31"

expr_42 = expr_gen(rules[42])
expr_31 = expr_gen(rules[31])

expr_8 = "(" + expr_42 + ")+"


count = 0
for i in range(1, 500):
    expr_11 = "(" + expr_42 + "){" + str(i) + "}(" + expr_31 + "){" + str(i) + "}"

    expr_0 = re.compile("^" + expr_8 + expr_11)

    for m in messages:
        result = expr_0.fullmatch(m)

        if result is not None:
            count += 1
print(count)
