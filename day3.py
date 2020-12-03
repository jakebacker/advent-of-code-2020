data = []

with open("inputs/day3.txt", "r") as f:
#with open("test/day3.txt", "r") as f:
    data = f.read().split("\n")  # This part may change

count = 0

x_size = len(data[0])

dx = 1
dy = 2
x = 0
y = 0
while True:
    value = data[y][x - x_size*int(x/x_size)]

    if value == "#":
        count += 1

    y += dy
    x += dx

    if y >= len(data):
        break


print(count)