data = []

with open("inputs/day8.txt", "r") as f:
#with open("test/day8.txt", "r") as f:
    data = f.read().split("\n")  # This part may change

# [(instruction, value), (instruction, value)]
instructions_original = []

for d in data:
    s = d.split(" ")

    instructions_original.append((s[0], s[1]))

acc = 0

for i in range(0, len(instructions_original)):
    instructions = instructions_original.copy()

    if instructions[i][0] == "acc":
        continue
    elif instructions[i][0] == "nop":
        instructions[i] = ("jmp", instructions[i][1])
    elif instructions[i][0] == "jmp":
        instructions[i] = ("nop", instructions[i][1])

    completed_instructions = []

    acc = 0
    ip = 0

    running = True
    graceful_term = False

    while running:
        if ip in completed_instructions:
            running = False
            break

        completed_instructions.append(ip)

        if ip >= len(instructions):
            graceful_term = True
            running = False
            break

        pair = instructions[ip]
        ins = pair[0]
        val = pair[1]

        if ins == "acc":
            acc += int(val)
        elif ins == "jmp":
            ip += (int(val)-1)

        ip += 1

    if graceful_term:
        print("done")
        break

print(acc)