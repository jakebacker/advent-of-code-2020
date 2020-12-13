import math

data = []

def mmod(a, b):
    out = a % b
    if out < 0:
        out += b
    return out

with open("inputs/day13.txt", "r") as f:
#with open("test/day13.txt", "r") as f:
    data = f.read().split("\n")  # This part may change

depart = int(data[0])

busses = data[1].split(",")

busses_proper = []

indicies = []

index = 0
for b in busses:
    if b != "x":
        busses_proper.append(int(b))
        indicies.append(index)
    index += 1

next_times = []

for b in busses_proper:
    next_times.append(math.ceil(depart/b)*b)

wait = min(next_times)
bus = busses_proper[next_times.index(wait)]

wait = wait - depart

print(bus)
print(wait)

print(bus * wait)

# Part 2

finalTime = busses_proper[0]
multiplier = busses_proper[0]

for i in range(1, len(busses_proper)):
    n = 0
    while (finalTime % busses_proper[i]) != mmod((busses_proper[i]-indicies[i]), busses_proper[i]):
        finalTime += multiplier

    multiplier *= busses_proper[i]

print(finalTime)
