import re


def get_score(cards):

    total = 0
    mult = 1
    for c in cards[::-1]:
        total += c * mult
        mult += 1
    return total

data = []

with open("inputs/day22.txt", "r") as f:
#with open("test/day22.txt", "r") as f:
    data = f.read().split("\n")  # This part may change

player_1 = []
player_2 = []


is_player_1 = True
for d in data:
    if d.strip() == "":
        is_player_1 = False
        continue
    if re.match("\\d+", d.split(" ")[0]):  # Is it just numbers
        if is_player_1:
            player_1.append(int(d))
        else:
            player_2.append(int(d))


while len(player_1) > 0 and len(player_2) > 0:
    top_1 = player_1.pop(0)
    top_2 = player_2.pop(0)

    if top_1 > top_2:
        player_1.append(top_1)
        player_1.append(top_2)
    else:
        player_2.append(top_2)
        player_2.append(top_1)

if len(player_1) == 0:
    print(get_score(player_2))
else:
    print(get_score(player_1))
