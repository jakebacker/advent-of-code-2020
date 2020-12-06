data = []

with open("inputs/day6.txt", "r") as f:
#with open("test/day6.txt", "r") as f:
    data = f.read().split("\n")  # This part may change


yes_questions = []

sum_counts = 0

first_person = True

count = 0

for d in data:
    if d.strip() == "":
        sum_counts += len(yes_questions)
        yes_questions = []
        count = 0
        first_person = True
        continue
    if first_person:
        yes_questions = list(d)
        first_person = False
        continue

    temp_yes = yes_questions.copy()

    for c in yes_questions:
        if c not in d:
            temp_yes.remove(c)
    yes_questions = temp_yes.copy()


print(sum_counts)
