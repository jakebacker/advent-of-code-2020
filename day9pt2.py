data = []

with open("inputs/day9.txt", "r") as f:
#with open("test/day9.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


preamble_size = 25

preamble_start = 0

first_invalid = 0

for i in range(preamble_start + preamble_size, len(data)):
    num = int(data[i])

    has_valid = False
    for px in range(preamble_start, preamble_start + preamble_size):
        if has_valid:
            break
        for py in range(preamble_start, preamble_start + preamble_size):
            x = int(data[px])
            y = int(data[py])

            if x == y:
                continue

            if num == x + y:
                has_valid = True
                break  # Tiny speed up

    if not has_valid:
        print(num)
        first_invalid = num
        break

    preamble_start += 1


for i in range(0, len(data)):  # All starting numbers
    min_range = first_invalid
    max_range = 0

    ii = i
    sum = 0
    while sum < first_invalid and ii < len(data):
        num = int(data[ii])
        if num == first_invalid:
            ii += 1
            continue

        if num > max_range:
            max_range = num
        if num < min_range:
            min_range = num

        sum += num
        ii += 1

    if sum == first_invalid:
        print(min_range)
        print(max_range)
        print(min_range+max_range)
        break
