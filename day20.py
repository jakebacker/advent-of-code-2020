import math
import copy

data = []

with open("inputs/day20.txt", "r") as f:
#with open("test/day20.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


def transform(arr):
    trans = list(map(list, zip(*arr)))
    for t in range(0, len(trans)):
        trans[t] = ''.join(trans[t])
    return trans


def gen_normal_edges(tile_data):
    tile_trans = transform(tile_data)

    return [tile_data[0], tile_trans[-1], tile_data[-1], tile_trans[0]]


def flip_edges_horz(edges):
    return [edges[0][::-1], edges[3], edges[2][::-1], edges[1]]


def flip_edges_vert(edges):
    return [edges[2], edges[1][::-1], edges[0], edges[3][::-1]]


def rot_edges(edges):  # Rotates 90deg
    return [edges[3][::-1], edges[0], edges[1][::-1], edges[2]]


def gen_possible_edges(tile_data):
    normal = gen_normal_edges(tile_data)
    rot = rot_edges(normal)
    return [normal, rot, flip_edges_horz(normal), flip_edges_horz(rot), flip_edges_vert(normal), flip_edges_vert(rot),
            flip_edges_horz(flip_edges_vert(normal)), flip_edges_horz(flip_edges_vert(rot))]


def rot_tile(tile):
    return [''.join(list(val)) for val in list(zip(*tile[::-1]))]


def flip_tile_horz(tile):
    result = []
    for t in tile:
        result.append(t[::-1])
    return result


def flip_tile_vert(tile):
    return [''.join(list(val)) for val in list(zip(*flip_tile_horz(list(zip(*tile)))))]


tiles = {}

current_id = 0
start = True

for i in range(0, len(data)):
    if start:
        tile_name = data[i]
        tile_id = int(tile_name[5:len(tile_name)-1])
        tiles[tile_id] = []
        current_id = tile_id
        start = False
        continue
    if data[i].strip() == "":
        start = True
        continue
    tiles[current_id].append(data[i])

# {id, [[normal], [rotate], [flip_horz], [rot, flip_horz], [flip_vert], [rot, flip_vert], [flip_flip], [rot_flip_flip]]}
# Each of those contain ["top", "right", "bottom", "left"]
tiles_orient = {}

for t in tiles:
    tiles_orient[t] = gen_possible_edges(tiles[t])


grid = []

# Make the grid the right size
for i in range(0, int(math.sqrt(len(tiles)))):
    grid.append([(-1, -1)]*int(math.sqrt(len(tiles))))

product = 1

unique_edges = {}  # {id: [0, 1]} means the top and right edges are unique

# Find unique edges in input. These edges are on the very edge of the total puzzle. Solve inwards.
for e in tiles_orient:
    edges = tiles_orient[e]
    normal = edges[0]

    unique_count = 0
    for n in normal:
        was_valid = True

        for d in tiles_orient:
            if e == d:
                continue
            for t in tiles_orient[d]:
                if n in t:
                    was_valid = False
                    break

        if was_valid:
            # n is a unique edge
            if e not in unique_edges:
                unique_edges[e] = []
            unique_edges[e].append(normal.index(n))
            unique_count += 1
        if unique_count == 2:
            break
    if unique_count == 2:
        # This is a corner piece!
        print(e)
        product *= e

print(product)
print(unique_edges)

# Part 2
look_queue = []  # [(tile_num, orientation, (x, y))]
completed_list = []
looking = -1
current_loc = (0, 0)

for u in unique_edges:
    if len(unique_edges[u]) == 2:
        # u is a corner
        looking = u
        break


# Initialize the location
if 0 in unique_edges[looking] and 3 in unique_edges[looking]:
    grid[0][0] = (looking, 0)
    current_loc = (0, 0)
elif 0 in unique_edges[looking] and 1 in unique_edges[looking]:
    grid[0][len(grid)-1] = (looking, 0)
    current_loc = (0, len(grid)-1)
elif 2 in unique_edges[looking] and 3 in unique_edges[looking]:
    grid[len(grid)-1][0] = (looking, 0)
    current_loc = (len(grid)-1, 0)
else:
    grid[len(grid) - 1][len(grid) - 1] = (looking, 0)
    current_loc = (len(grid) - 1, len(grid) - 1)


# Convert the unique edges into non-unique edges
non_unique = []
for e in range(0, 4):
    if e in unique_edges[looking]:
        continue
    non_unique.append(e)

print(non_unique)


# This is just for the first iteration
# Need to initialize the queue with something, so this does just that
for n in non_unique:
    # Find its pair, connect with the correct orientation
    edge = tiles_orient[looking][0][n]  # When this code is added to the loop, 0 is not constant. Here assuming 0

    # Find the corresponding edge with the edge on the opposite side of this
    # If n==0, looking for 2 and vice versa. If n==1, looking for 3 and vise versa
    looking_for = 0
    if n == 0:
        looking_for = 2
    elif n == 2:
        looking_for = 0
    elif n == 1:
        looking_for = 3
    elif n == 3:
        looking_for = 1
    else:
        print("something broke!")

    complete = False

    # For each tile, check if it works
    for t in tiles_orient:
        # Ignore this tile
        if t == looking:
            continue

        orientations = tiles_orient[t]

        # Check each orientation of the tile
        for o in orientations:
            edge = o[looking_for]

            # Check if the corresponding edge of this oriented tile is the correct one
            if edge == tiles_orient[looking][0][n]:
                # This tile and orientation match!
                dx = 0
                dy = 0
                if looking_for == 0:
                    dx = 0
                    dy = 1
                elif looking_for == 1:
                    dx = -1
                    dy = 0
                elif looking_for == 2:
                    dx = 0
                    dy = -1
                else:
                    dx = 1
                    dy = 0
                pos = (current_loc[0]+dy, current_loc[1]+dx)
                grid[pos[0]][pos[1]] = (t, orientations.index(o))
                look_queue.append((t, orientations.index(o), pos))
                completed_list.append(looking)
                complete = True
                break
        if complete:
            break

placed = []

# look_queue has been initialized with values, time to do things!
while not len(look_queue) == 0:
    next_set = look_queue.pop(0)

    # Generate the set of edges that you need to look at.
    # These are edges that aren't unique and don't have a tile in the corresponding spot already
    next_edges = []
    for i in range(0, len(tiles_orient[next_set[0]][next_set[1]])):

        # Check if this is a unique edge. If it is, just ignore it
        if next_set[0] in unique_edges and i in unique_edges[next_set[0]]:
            continue

        # Where will the next tile on this edge be
        dx = 0
        dy = 0
        if i == 0:
            dx = 0
            dy = -1
        elif i == 1:
            dx = 1
            dy = 0
        elif i == 2:
            dx = 0
            dy = 1
        else:
            dx = -1
            dy = 0

        pos = (next_set[2][0]+dy, next_set[2][1]+dx)

        # If the cell is not occupied
        if pos[0] < 0 or pos[0] >= len(grid):
            continue
        if pos[1] < 0 or pos[1] >= len(grid):
            continue
        if grid[pos[0]][pos[1]][0] == -1:
            next_edges.append((i, pos))

    # Look through each of these edges. Look through remaining tiles to find something that fits.
    for ne in next_edges:
        e = ne[0]
        # Convert into the other side
        looking_for = 0
        if e == 0:
            looking_for = 2
        elif e == 2:
            looking_for = 0
        elif e == 1:
            looking_for = 3
        elif e == 3:
            looking_for = 1
        else:
            print("something broke!")

        edge_data = tiles_orient[next_set[0]][next_set[1]][e]

        for t in tiles_orient:
            if t == tiles_orient[next_set[0]]:
                continue
            if t in completed_list:
                continue
            if t in placed:
                continue

            orientations = tiles_orient[t]

            # Check each orientation of the tile
            for o in orientations:
                edge = o[looking_for]

                if edge == edge_data:
                    pos = ne[1]
                    grid[pos[0]][pos[1]] = (t, orientations.index(o))
                    look_queue.append((t, orientations.index(o), pos))
                    placed.append(t)
                    completed_list.append(next_set[0])

    # Queue will eventually have 0 tiles in it

# Now using the IDs and orientations, actually construct the image
image = []
for i in range(0, int(math.sqrt(len(tiles)))):
    row = []
    for ii in range(0, int(math.sqrt(len(tiles)))):
        row.append([])
    image.append(row)

for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
        cell = grid[y][x][0]
        orientation = grid[y][x][1]

        # [normal], [rotate], [flip_horz], [rot, flip_horz], [flip_vert], [rot, flip_vert], [flip_flip], [rot_flip_flip]

        if orientation == 0:
            image[y][x] = tiles[cell]
        elif orientation == 1:
            image[y][x] = rot_tile(tiles[cell])
        elif orientation == 2:
            image[y][x] = flip_tile_horz(tiles[cell])
        elif orientation == 3:
            image[y][x] = flip_tile_horz(rot_tile(tiles[cell]))
        elif orientation == 4:
            image[y][x] = flip_tile_vert(tiles[cell])
        elif orientation == 5:
            image[y][x] = flip_tile_vert(rot_tile(tiles[cell]))
        elif orientation == 6:
            image[y][x] = flip_tile_vert(flip_tile_horz(tiles[cell]))
        elif orientation == 7:
            image[y][x] = flip_tile_vert(flip_tile_horz(rot_tile(tiles[cell])))
        else:
            print("aaaaaaaaaa")

# Final image has been created!
print(image)

# Remove borders of each tile and combine tiles

for r in range(0, len(image)):
    for c in range(0, len(image[r])):
        image[r][c] = image[r][c][1:-1]  # Cut off the first and last rows

        for rr in range(0, len(image[r][c])):
            image[r][c][rr] = image[r][c][rr][1:-1]  # Cut off the first and last column of each row

final_image = []

for i in image:
    for y in range(0, len(i[0])):
        line = ""
        for x in i:
            line += x[y]
        final_image.append(line)

# Look through different orientations to find monsters
relative_coords = [(0, 0), (1, 1), (4, 1), (5, 0), (6, 0), (7, 1), (10, 1), (11, 0), (12, 0), (13, 1), (16, 1), (17, 0),
                   (18, 0), (18, -1), (19, 0)]

num_monsters = 0

final_image = flip_tile_vert(rot_tile(final_image))

print('\n'.join(final_image))

for y in range(0, len(final_image)):
    for x in range(0, len(final_image[y])):
        if final_image[y][x] == "#":

            found = True
            for r in relative_coords:
                dx = x + r[0]
                dy = y + r[1]

                if 0 <= dy < len(final_image) and 0 <= dx < len(final_image[dy]):
                    # Coords are in the board
                    if not final_image[dy][dx] == "#":
                        found = False
                        break
                else:
                    found = False
                    break
            if found:
                num_monsters += 1

print(num_monsters)

# num# - (15 * numMonsters) = num non-monster #
num_blocked = 0
for r in final_image:
    for x in r:
        if x == "#":
            num_blocked += 1

print(num_blocked - (15 * num_monsters))


# This was just code to figure out what tiles can connect together
# The conclusion is that each tile can only connect to one other tile
'''
for e in possible_edges:
    edges = possible_edges[e]
    normal = edges[0]

    for n in normal:
        print("------------------")
        print()
        pair_count = 0
        for d in possible_edges:
            if e == d:
                continue
            for t in possible_edges[d]:
                if n in t:
                    print(d)
                    pair_count += 1
        print(e)
        print(n)
        print(pair_count)
        print()
'''

