data = []

with open("inputs/day10.txt", "r") as f:
#with open("test/day10.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


adapters = []
for d in data:
    adapters.append(int(d))

adapters.sort()

adapters.append(adapters[-1] + 3)  # The device

differences = []

effective_rating = 0

for a in adapters:
    if a - effective_rating > 3:
        print("error!!!!!!")
        break

    differences.append(a - effective_rating)
    effective_rating = a

print(differences.count(1))
print(differences.count(3))
print(differences.count(1) * differences.count(3))
