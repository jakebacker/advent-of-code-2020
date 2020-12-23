data = ""

with open("inputs/day23.txt", "r") as f:
#with open("test/day23.txt", "r") as f:
    data = f.read()  # This part may change


data_list = list(data)
cups = []
current_cup_index = 0
max = 0

for c in data_list:
    cups.append(int(c))
    if int(c) > max:
        max = int(c)

current_cup = cups[current_cup_index]

for i in range(0, 100):
    current_cup = cups[current_cup_index]
    selected = []
    dest_label = cups[current_cup_index] - 1

    for r in range(0, 3):
        select_index = (current_cup_index + 1 + r) % len(cups)
        selected.append(cups[select_index])
    for s in selected:
        cups.remove(s)

    dest = 0
    while True:
        if dest_label in selected:
            dest_label -= 1
        elif dest_label <= 0:
            dest_label = max
        else:
            dest = cups.index(dest_label) + 1
            break

    for s in selected:
        cups.insert(dest, s)
        dest += 1

    current_cup_index = (cups.index(current_cup) + 1) % len(cups)

one_index = cups.index(1)+1
final = []

for i in range(0, len(cups)-1):
    final.append(cups[one_index % len(cups)])
    one_index += 1

print(final)