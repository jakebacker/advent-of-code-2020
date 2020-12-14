data = []

with open("inputs/day14.txt", "r") as f:
#with open("test/day14pt2.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


def convert(num):
    b = bin(int(num)).split("b")[1]

    prefix = "0"*(36-len(b))

    return prefix + b


mask = "X"*36

mem = {}

for d in data:
    if "mask" in d:
        # Update mask
        mask = d.split(" ")[2]
    else:
        # Update mem
        after = d.split("[")[1]
        address = convert(after.split("]")[0])
        l_address = list(address)
        value = after.split(" ")[2]

        for i in range(0, len(mask)):
            if mask[i] == "1":
                l_address[i] = "1"
            elif mask[i] == "X":
                l_address[i] = "X"

        x_locs = [i for i, x in enumerate(l_address) if x == "X"]

        enabled = [0]*len(x_locs)

        for x in x_locs:
            l_address[x] = "0"

        options = [bin(x)[2:].zfill(len(enabled)) for x in range(pow(2, len(enabled)))]

        # Count up in binary with the enabled array
        count = 1
        for o in options:
            enabled = list(o)

            for i in range(1, len(enabled)+1):
                index = -i
                if enabled[i-1] == "1":
                    l_address[x_locs[index]] = "1"
                else:
                    l_address[x_locs[index]] = "0"

            final_address = int("".join(l_address), 2)
            mem[final_address] = value

            count += 1

sum = 0

for n in mem.values():
    sum += int(n)

print(sum)
