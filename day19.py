data = []

with open("inputs/day19.txt", "r") as f:
#with open("test/day19.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


class MatchRule:

    left = []  # Array of MatchRule or str
    right = None

    def __init__(self):
        self.left = []

    def add_left(self, left):
        self.left.append(left)

    def add_right(self, right):
        if self.right is None:
            self.right = []
        self.right.append(right)


def matches(val, rule: MatchRule):
    curr_val = val
    if rule.right is None:
        for r in rule.left:
            if isinstance(r, str):
                if curr_val.startswith(r):
                    curr_val = curr_val[curr_val.index(r) + len(r):]
                else:
                    return False, ""
            else:
                result = matches(curr_val, r)
                if not result[0]:
                    return False, ""
                curr_val = result[1]
        return True, curr_val
    else:
        matches_left = True
        matches_right = True
        for r in rule.left:
            if isinstance(r, str):
                if curr_val.startswith(r):
                    curr_val = curr_val[curr_val.index(r) + len(r):]
                else:
                    matches_left = False
                    break
            else:
                result = matches(curr_val, r)
                if not result[0]:
                    matches_left = False
                    break
                curr_val = result[1]
        if matches_left:
            return True, curr_val
        curr_val = val
        for r in rule.right:
            if isinstance(r, str):
                if curr_val.startswith(r):
                    curr_val = curr_val[curr_val.index(r) + len(r):]
                else:
                    matches_right = False
                    break
            else:
                result = matches(curr_val, r)
                if not result[0]:
                    matches_right = False
                    break
                curr_val = result[1]
        if matches_right:
            return True, curr_val
        return False, ""


rules_str = []
messages = []

for i in range(0, len(data)):
    if data[i].strip() == "":
        rules_str = data[:i]
        messages = data[i+1:]
        break

rules = []

for i in range(0, len(rules_str)):
    rules.append(MatchRule())

for i in range(0, len(rules_str)):
    rule_num = int(rules_str[i].split(":")[0].strip())
    r = rules_str[i].split(":")[1].strip()

    if "|" in r:
        left = r.split("|")[0].strip()
        right = r.split("|")[1].strip()

        for l in left:
            if not l.strip() == "":
                rules[rule_num].add_left(rules[int(l)])
        for r in right:
            if not r.strip() == "":
                rules[rule_num].add_right(rules[int(r)])
    elif "\"" in r:
        rules[rule_num].add_left(r[1:len(r)-1])
    else:
        for l in r:
            if not l.strip() == "":
                rules[rule_num].add_left(rules[int(l)])

count = 0
for m in messages:
    result = matches(m, rules[0])

    if result[0] and result[1].strip() == "":
        print(matches(m, rules[0]))
        count += 1
print(count)


# REGEX: ^a(ab|ba)
# ^a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b