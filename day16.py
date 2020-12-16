data = []

with open("inputs/day16.txt", "r") as f:
#with open("test/day16.txt", "r") as f:
    data = f.read().split("\n")  # This part may change

# {"name": ((1, 3),(5, 7))}
rules = {}


def in_rules(num):
    for val in rules.values():
        first = val[0]
        second = val[1]

        if first[0] <= num <= first[1] or second[0] <= num <= second[1]:
            return True
    return False


def valid_positions(col):
    positions = []

    for key in rules.keys():
        first = rules[key][0]
        second = rules[key][1]

        all_valid = True
        for num in col:
            if not first[0] <= int(num) <= first[1] and not second[0] <= int(num) <= second[1]:
                all_valid = False
        if all_valid:
            positions.append(key)
    return positions


index = 1
for d in data:
    if d.strip() == "":
        break

    name = d.split(":")[0]
    rest = d.split(":")[1].strip()
    rule_1 = rest.split(" ")[0]
    rule_2 = rest.split(" ")[2]

    rule_1_min = int(rule_1.split("-")[0])
    rule_1_max = int(rule_1.split("-")[1])
    rule_2_min = int(rule_2.split("-")[0])
    rule_2_max = int(rule_2.split("-")[1])

    rules[name] = ((rule_1_min, rule_1_max), (rule_2_min, rule_2_max))
    index += 1

your_ticket = data[index+1].split(",")

nearby = data[index+4:]

total = 0

modified_nearby = []

for t in nearby:
    vals = t.split(",")

    valid = True

    for v in vals:
        if not in_rules(int(v)):
            total += int(v)
            valid = False
            break
    if not valid:
        continue
    modified_nearby.append(vals)

print(total)

# Part 2

trans_nearby = list(map(list, zip(*modified_nearby)))

# [(0, [class, row]), (1, [row]), (2, [class, seat, row])]
valid_fields = []

for i in range(0, len(trans_nearby)):
    c = trans_nearby[i]
    valid_fields.append((i, valid_positions(c)))

sorted_valid_fields = sorted(valid_fields, key=lambda x: len(x[1]))  # Sort the fields by the length of the array

final_fields = [""]*len(sorted_valid_fields)  # Force the array to be the right length
taken = []
for f in sorted_valid_fields:
    col_num = f[0]
    fields = f[1]

    modified = [i for i in fields if i not in taken]

    if not len(modified) == 1:
        print("aaaaaa")

    taken.append(modified[0])
    final_fields[col_num] = modified[0]

print(final_fields)

your_ticket_corrected = {}

for f in range(0, len(final_fields)):
    your_ticket_corrected[final_fields[f]] = your_ticket[f]

print(your_ticket_corrected)


product = 1

for key in your_ticket_corrected:
    if "departure" in key:
        product *= int(your_ticket_corrected[key])

print(product)