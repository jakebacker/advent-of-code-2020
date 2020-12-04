import re

data = []

with open("inputs/day4.txt", "r") as f:
#with open("test/day4.txt", "r") as f:
    data = f.read().split("\n")  # This part may change

objects = []

index = 0
ii = False
for d in data:
    if d.strip() == "":
        if ii:
            ii = False
        else:
            index += 1
        continue

    if ii:
        continue

    object = {}
    if index < len(objects):
        # Object exists
        object = objects[index]

    fields = d.split(" ")
    for f in fields:
        name = f.split(":")[0].strip()
        value = f.split(":")[1].strip()
        if name in object:
            # This is invalid
            ii = True
            break
        object[name] = value

    if ii:
        continue

    if index < len(objects):
        objects[index] = object
    else:
        objects.append(object)


valid = 0

valid_fields = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
for o in objects:
    fields = o.keys()

    invalid = False
    for v in valid_fields:
        if v not in fields:
            invalid = True
            break

    if not invalid:

        if 1920 <= int(o["byr"]) <= 2002 and 2010 <= int(o["iyr"]) <= 2020 and 2020 <= int(o["eyr"]) <= 2030:
            hgt = o["hgt"]

            invalid_2 = False

            if hgt[-2:] == "cm":
                if int(hgt.split("cm")[0]) < 150 or int(hgt.split("cm")[0]) > 193:
                    invalid_2 = True
            elif hgt[-2:] == "in":
                if int(hgt.split("in")[0]) < 59 or int(hgt.split("in")[0]) > 76:
                    invalid_2 = True
            else:
                invalid_2 = True

            if not invalid_2:
                hcl = o["hcl"]

                m = re.match("#[0-9a-f]{6}", hcl)

                if m is not None and len(hcl) == len(m.group()) == 7:
                    if o["ecl"] == "amb" or o["ecl"] == "blu" or o["ecl"] == "brn" or o["ecl"] == "grn" or o["ecl"] == "gry" or o["ecl"] == "hzl" or o["ecl"] == "oth":
                        pid = o["pid"]

                        mm = re.match("\\d{9}", pid)

                        if mm is not None and len(pid) == len(mm.group()):
                            valid += 1

print(valid)
