data = []

with open("inputs/day7.txt", "r") as f:
#with open("test/day7.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


# {"color": [(color, count)]}
bags = {}

contains = []
looked_through = []


def find_count(bag_color):
    bag_contents = bags[bag_color]

    total = 0
    for (c_color, count) in bag_contents:
        total += int(count)
        total += find_count(c_color) * int(count)

    return total

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

print(find_count("shiny gold"))