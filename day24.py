import copy


def count_tiles(tiles):
    count = 0
    for c in tiles:
        if tiles[c]:
            count += 1
    return count


def count_grid(grid):
    count = 0
    for q in range(0, len(grid)):
        for r in range(0, len(grid)):
            if grid[q][r] == 1:
                count += 1
    return count


data = []

with open("inputs/day24.txt", "r") as f:
#with open("test/day24.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


directions = []

for d in data:
    instructions = []

    i = 0
    while i < len(d):
        instruction = d[i]

        val = ""
        if instruction == "s" or instruction == "n":
            val = instruction + d[i+1]
            i += 1
        else:
            val = instruction
        instructions.append(val)
        i += 1
    directions.append(instructions)


coords = {}  # axial coordinates

# Initialize
for d in directions:
    r = 0
    q = 0

    for i in d:
        if i == "e":
            q += 1
        elif i == "w":
            q -= 1
        elif i == "ne":
            q += 1
            r -= 1
        elif i == "sw":
            q -= 1
            r += 1
        elif i == "se":
            r += 1
        elif i == "nw":
            r -= 1
        else:
            print("aaaaaaa")

    if (r, q) in coords:
        coords[(r, q)] = not coords[(r, q)]
    else:
        coords[(r, q)] = True

grid = []

size = 201
for s in range(0, size):
    grid.append([0]*size)

middle = int((size-1)/2)

for c in coords:

    if coords[c]:
        q = c[0] + middle
        r = c[1] + middle

        grid[q][r] = 1

copy_grid = copy.deepcopy(grid)


neighbors_delta = [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]

# Run
for d in range(0, 100):
    for q in range(0, len(grid)):
        for r in range(0, len(grid)):
            val = grid[q][r]

            # Count neighbors
            neighbors = 0
            for n in neighbors_delta:
                dq = q + n[0]
                dr = r + n[1]

                if 0 <= dq < len(grid) and 0 <= dr < len(grid):
                    neighbor = grid[q+n[0]][r+n[1]]

                    if neighbor == 1:
                        neighbors += 1

            if val == 1 and (neighbors == 0 or neighbors > 2):
                copy_grid[q][r] = 0
            elif val == 0 and neighbors == 2:
                copy_grid[q][r] = 1

    grid = copy.deepcopy(copy_grid)
print(count_grid(grid))



