data = []

with open("inputs/day5.txt", "r") as f:
#with open("test/day5.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


ids = []

max_id = 0

for d in data:

    min = 0
    max = 127

    min_col = 0
    max_col = 7

    row_data = d[0:-3]
    col_data = d[-3:]

    seat_id = 0

    for r in row_data:
        if r == "B":
            min = min + int((max-min)/2) + 1
        elif r == "F":
            max = max - int((max-min)/2) - 1
        else:
            print("invalid")

    seat_id = min * 8


    for c in col_data:
        if c == "R":
            min_col = min_col + int((max_col-min_col)/2) + 1
        elif c == "L":
            max_col = max_col - int((max_col-min_col)/2) - 1
        else:
            print("invalid")

    seat_id += min_col

    #print(seat_id)

    ids.append(seat_id)

    if seat_id > max_id:
        max_id = seat_id


print(max_id)

ids.sort()

for i in range(0, max_id+1):
    if i-1 in ids and i+1 in ids and i not in ids:
        print(i)