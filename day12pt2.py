data = []

with open("inputs/day12.txt", "r") as f:
#with open("test/day12.txt", "r") as f:
    data = f.read().split("\n")  # This part may change

vert = 0
horz = 0

way_vert = 1
way_horz = 10

direction = 0  # 0 is east

for d in data:
    action = d[0]
    param = int(d[1:])

    if action == "N":
        way_vert += param
    elif action == "S":
        way_vert -= param
    elif action == "E":
        way_horz += param
    elif action == "W":
        way_horz -= param
    elif action == "L":
        direction += param
        if direction < 0:
            direction += 360
    elif action == "R":
        direction -= param
        if direction < 0:
            direction += 360
    elif action == "F":
        for i in range(0, param):
            horz += way_horz
            vert += way_vert
    else:
        print("broke")

    num = direction % 360
    num = int(num / 90)
    for i in range(0, num):
        temp = way_horz
        way_horz = -way_vert
        way_vert = temp

    direction = 0

print(abs(vert) + abs(horz))
