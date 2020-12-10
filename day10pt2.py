data = []

with open("inputs/day10.txt", "r") as f:
#with open("test/day10.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


adapters = []
for d in data:
    adapters.append(int(d))

adapters.append(0)

adapters.sort()

adapters.append(adapters[-1] + 3)  # The device

num_ways = [1] + [0] * (len(adapters)-1)

# How many ways to get to each adapter
for i in range(1, len(adapters)):
    total = 0
    # Look at previous 3 adapters. If it is possible to get to that one, add its value to this total.
    a_min = i-3
    if a_min < 0:
        a_min = 0

    for x in range(a_min, i):
        if adapters[i] - adapters[x] <= 3:
            total += num_ways[x]

    # Store total
    num_ways[i] = total

print(num_ways[-1])
