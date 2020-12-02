data = []

with open("inputs/day2.txt", "r") as f:
# with open("test/day2.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


valid = 0
for d in data:
    parts1 = d.split(":")
    policy = parts1[0]
    password = parts1[1].strip()

    parts2 = policy.split(" ")
    prange = parts2[0]
    letter = parts2[1]

    parts3 = prange.split("-")
    cmin = int(parts3[0])
    cmax = int(parts3[1])

    '''
    # Part 1
    count = 0
    for c in password:
        if c is letter:
            count += 1

    if count >= cmin and count <= cmax:
        valid += 1
        '''

    # Part 2
    c = 0
    if password[cmin-1] is letter:
        c += 1
    if password[cmax-1] is letter:
       c += 1

    if c == 1:
        valid += 1

print(valid)