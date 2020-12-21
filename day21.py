data = []

with open("inputs/day21.txt", "r") as f:
#with open("test/day21.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


foods = []

possible_allergens = {}  # {ingredient: [allergens]}

for d in data:
    parts = d.split("(")
    ingredients = parts[0].strip().split(" ")
    allergens = ''.join(parts[1].split(")")[0].split(" ")[1:]).split(",")

    for i in range(0, len(allergens)):
        allergens[i] = allergens[i].strip()

    foods.append((ingredients, allergens))

for f in foods:
    for i in f[0]:
        if i not in possible_allergens:
            possible_allergens[i] = []

# Loop through each food
# Loop through each allergen
# Loop through each ingredient
# Say "can this ingredient be this allergen". To do this, look in all other foods that also contain this allergen
# If the food contains the same ingredient, it is possible for it to be that allergen
# If it does not, it cannot
for f in foods:
    for a in f[1]:
        for i in f[0]:
            not_there = True
            possible = False
            for other in foods:
                if f == other:
                    continue
                if a in other[1]:
                    not_there = False
                    if i in other[0]:
                        # It is possible
                        possible = True
                    else:
                        # It is not possible
                        possible = False
                        break
            if not_there or possible:
                if a not in possible_allergens[i]:
                    possible_allergens[i].append(a)

no_allergens = []

for i in possible_allergens:
    if len(possible_allergens[i]) == 0:
        no_allergens.append(i)

total = 0
for f in foods:
    for i in f[0]:
        if i in no_allergens:
            total += 1

print(total)

# Part 2
print(possible_allergens)

actual_allergens = {}  # {allergen: ingredient}

while True:
    modified = False
    for i in possible_allergens:
        if len(possible_allergens[i]) == 1:
            modified = True
            allergen = possible_allergens[i][0]
            actual_allergens[allergen] = i

            # Remove this allergen from all other places
            for ing in possible_allergens:
                new_allergens = []
                for a in possible_allergens[ing]:
                    if not a == allergen:
                        new_allergens.append(a)
                possible_allergens[ing] = new_allergens
    if not modified:
        break

print(actual_allergens)

sorted_keys = []

for key in sorted(actual_allergens):
    sorted_keys.append(key)

canon_list = ""
for s in sorted_keys:
    canon_list += actual_allergens[s] + ","

print(canon_list[:-1])