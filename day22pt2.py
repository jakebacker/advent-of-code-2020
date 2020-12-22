import re


def get_score(cards):

    total = 0
    mult = 1
    for c in cards[::-1]:
        total += c * mult
        mult += 1
    return total


def play_round(hand_1, hand_2):  # Returns (hand_1, hand_2)
    original_1 = hand_1.copy()
    original_2 = hand_2.copy()
    hands = []  # [(hand_1, hand_2)]

    while len(hand_1) > 0 and len(hand_2) > 0:

        for h in hands:
            if hand_1 == h[0] and hand_2 == h[1]:
                # Base case, player 1 wins
                return hand_1, original_2

        hands.append((hand_1.copy(), hand_2.copy()))

        top_1 = hand_1.pop(0)
        top_2 = hand_2.pop(0)

        if top_1 <= len(hand_1) and top_2 <= len(hand_2):
            # Recurse!
            result = play_round(hand_1.copy()[:top_1], hand_2.copy()[:top_2])

            if len(result[1]) == 0:
                hand_1.append(top_1)
                hand_1.append(top_2)
            elif len(result[0]) == 0:
                hand_2.append(top_2)
                hand_2.append(top_1)
            else:
                # If this happens, the fallback case happened, player 1 wins
                hand_1.append(top_1)
                hand_1.append(top_2)
        else:
            if top_1 > top_2:
                hand_1.append(top_1)
                hand_1.append(top_2)
            else:
                hand_2.append(top_2)
                hand_2.append(top_1)

    return hand_1, hand_2


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


result = play_round(player_1, player_2)

if len(result[0]) == 0:
    print(get_score(result[1]))
else:
    print(get_score(result[0]))
