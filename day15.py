data = []

with open("inputs/day15.txt", "r") as f:
#with open("test/day15.txt", "r") as f:
    data = f.read().split(",")  # This part may change


last_spoken = {}

iterations = 30000000

previous_num = data[-1]
next_num = ""

for i in range(0, len(data)-1):
    last_spoken[data[i]] = i+1

for i in range(len(data), iterations):
    if previous_num not in last_spoken:
        # First time spoken, go 0
        next_num = "0"
    else:
        age = i - last_spoken[previous_num]
        next_num = str(age)

    last_spoken[previous_num] = i
    previous_num = next_num

print(previous_num)
