data = []

with open("inputs/day11.txt", "r") as f:
#with open("test/day11.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


def copy_arr(arr):
    copy = []

    for a in arr:
        copy.append(a.copy())
    return copy


def check_equal(arr1, arr2):
    for yy in range(0, len(arr1)):
        for xx in range(0, len(arr1[yy])):
            if not arr1[yy][xx] == arr2[yy][xx]:
                return False
    return True


seats = []
for d in data:
    seats.append(list(d))


next_state = copy_arr(seats)

while True:
    for y in range(0, len(seats)):
        for x in range(0, len(seats[y])):
            cell = seats[y][x]

            if cell == ".":
                continue

            # Find num adjacent
            adjacent = 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue

                    # Continue looking until you reach a seat or the edge
                    new_y = y + dy
                    new_x = x + dx
                    while 0 <= new_y < len(seats) and 0 <= new_x < len(seats[new_y]):
                        # If it is in the board
                        if seats[new_y][new_x] == "#":
                            adjacent += 1
                            break
                        if seats[new_y][new_x] == "L":
                            break

                        new_y += dy
                        new_x += dx

            if seats[y][x] == "L" and adjacent == 0:
                next_state[y][x] = "#"
            elif seats[y][x] == "#" and adjacent >= 5:
                next_state[y][x] = "L"

    if check_equal(seats, next_state):
        break

    seats = copy_arr(next_state)


occupied = 0
for y in range(0, len(seats)):
    for x in range(0, len(seats[y])):
        cell = seats[y][x]
        if cell == "#":
            occupied += 1

print(occupied)