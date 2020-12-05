data = []

with open("inputs/day5.txt", "r") as f:
#with open("test/day5.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


ids = []

# Part 1

max_id = 0

for d in data:

    min_row = 0
    max_row = 127

    min_col = 0
    max_col = 7

    row_data = d[0:-3]
    col_data = d[-3:]

    seat_id = 0

    for r in row_data:
        if r == "B":
            min_row = min_row + int((max_row - min_row) / 2) + 1
        elif r == "F":
            max_row = max_row - int((max_row - min_row) / 2) - 1
        else:
            print("invalid")

    seat_id = min_row * 8

    for c in col_data:
        if c == "R":
            min_col = min_col + int((max_col-min_col)/2) + 1
        elif c == "L":
            max_col = max_col - int((max_col-min_col)/2) - 1
        else:
            print("invalid")

    seat_id += min_col

    ids.append(seat_id)

    if seat_id > max_id:
        max_id = seat_id

print(max_id)

# Part 2

for i in range(0, max_id+1):
    if i-1 in ids and i+1 in ids and i not in ids:
        print(i)
