data = []

with open("inputs/day9.txt", "r") as f:
#with open("test/day9.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


preamble_size = 25

preamble_start = 0

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
        break

    preamble_start += 1
