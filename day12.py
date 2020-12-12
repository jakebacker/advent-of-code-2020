data = []

with open("inputs/day12.txt", "r") as f:
#with open("test/day12.txt", "r") as f:
    data = f.read().split("\n")  # This part may change

vert = 0
horz = 0

direction = 0  # 0 is east

for d in data:
    action = d[0]
    param = int(d[1:])

    if action == "N":
        vert += param
    elif action == "S":
        vert -= param
    elif action == "E":
        horz += param
    elif action == "W":
        horz -= param
    elif action == "L":
        direction += param
        if direction < 0:
            direction += 360
    elif action == "R":
        direction -= param
        if direction < 0:
            direction += 360
    elif action == "F":
        num = direction % 360
        if num == 0:
            horz += param
        elif num == 90:
            vert += param
        elif num == 180:
            horz -= param
        elif num == 270:
            vert -= param
        else:
            print("aaaa")
    else:
        print("broke")


print(abs(vert) + abs(horz))
