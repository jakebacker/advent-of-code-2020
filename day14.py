data = []

with open("inputs/day14.txt", "r") as f:
#with open("test/day14.txt", "r") as f:
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
        address = after.split("]")[0]
        value = after.split(" ")[2]

        bin_val = convert(value)
        l_val = list(bin_val)

        for i in range(0, len(mask)):
            if mask[i] == "1":
                l_val[i] = "1"
            elif mask[i] == "0":
                l_val[i] = "0"

        mem[address] = int("".join(l_val), 2)


sum = 0

for n in mem.values():
    sum += n

print(sum)