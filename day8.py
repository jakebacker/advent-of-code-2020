data = []

with open("inputs/day8.txt", "r") as f:
#with open("test/day8.txt", "r") as f:
    data = f.read().split("\n")  # This part may change

# [(instruction, value), (instruction, value)]
instructions = []

for d in data:
    s = d.split(" ")

    instructions.append((s[0], s[1]))

completed_instructions = []

acc = 0
ip = 0

running = True

while running:
    if ip in completed_instructions:
        running = False
        break

    completed_instructions.append(ip)

    pair = instructions[ip]
    ins = pair[0]
    val = pair[1]

    if ins == "acc":
        acc += int(val)
    elif ins == "jmp":
        ip += (int(val)-1)

    ip += 1

print(acc)