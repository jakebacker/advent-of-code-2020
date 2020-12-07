data = []

with open("inputs/day7.txt", "r") as f:
#with open("test/day7.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


# {"color": [(color, count)]}
bags = {}

contains = []
looked_through = []


def find_color(target, bag_contents):
    for (c_color, count) in bag_contents:
        if c_color in contains:
            return True
        if c_color in looked_through:
            return False
        if c_color == target:
            return True
        # Iterate deeper
        result = find_color(target, bags[c_color])
        if result:
            contains.append(c_color)
            return True
    return False


for d in data:
    if d.strip() == "":
        continue

    s1 = d.split(" contain ")

    color = s1[0].split(" bags")[0].strip()

    contents_str = s1[1].strip()

    s2 = contents_str.split(",")

    bags[color] = []

    if len(s2) == 1:
        if "no other bags" in s2[0]:
            continue

    for b in s2:
        bag = b.split(" bag")[0].strip()

        s3 = bag.split(" ")

        bag_count = s3[0]
        inner_color = (s3[1] + " " + s3[2])

        bags[color].append((inner_color, bag_count))


num_contains = 0

looking_for = "shiny gold"

for color, contents in bags.items():
    if find_color(looking_for, contents):
        contains.append(color)
        looked_through.append(color)
        num_contains += 1

print(num_contains)