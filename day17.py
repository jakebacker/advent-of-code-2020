import copy

data = []

with open("inputs/day17.txt", "r") as f:
#with open("test/day17.txt", "r") as f:
    data = f.read().split("\n")  # This part may change

grid_size = 19  # 15
grid_middle = int((grid_size-2)/2)  # grid_middle, grid_middle, grid_middle is 0, 0, 0 (except not actually)

grid = [[["." for x in range(grid_size)] for y in range(grid_size)] for z in range(grid_size)]

plane = []  # z, y, x
for d in data:
    pad_num = int((grid_size - len(d))/2)
    left_pad = ["." for x in range(pad_num)]
    right_pad = ["." for x in range(pad_num)]
    row = left_pad + list(d) + right_pad
    plane.append(row)

plane_pad = int((grid_size - len(plane))/2)
left_plane_pad = [["." for x in range(grid_size)] for y in range(plane_pad)]
right_plane_pad = [["." for x in range(grid_size)] for y in range(plane_pad)]
plane = left_plane_pad + plane + right_plane_pad

grid[grid_middle] = plane

next_grid = copy.deepcopy(grid)

print(grid)

for c in range(0, 6):
    for z in range(0, len(grid)):
        for y in range(0, len(grid[z])):
            for x in range(0, len(grid[z][y])):
                cell = grid[z][y][x]

                # Find num adjacent
                adjacent = 0
                for dz in range(-1, 2):
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if dx == 0 and dy == 0 and dz == 0:
                                continue
                            new_z = z + dz
                            new_y = y + dy
                            new_x = x + dx
                            if 0 <= new_z < len(grid) and 0 <= new_y < len(grid[new_z]) and 0 <= new_x < len(grid[new_z][new_y]):
                                # If it is in the board
                                if grid[new_z][new_y][new_x] == "#":
                                    adjacent += 1

                if cell == "#":
                    if adjacent == 2 or adjacent == 3:
                        next_grid[z][y][x] = "#"
                    else:
                        next_grid[z][y][x] = "."
                else:
                    if adjacent == 3:
                        next_grid[z][y][x] = "#"

    grid = copy.deepcopy(next_grid)


alive_count = 0

for z in range(0, len(grid)):
    for y in range(0, len(grid[z])):
        for x in range(0, len(grid[z][y])):
            cell = grid[z][y][x]

            if cell == "#":
                alive_count += 1

print(alive_count)