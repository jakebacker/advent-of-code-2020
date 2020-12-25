data = []

#with open("inputs/day25.txt", "r") as f:
with open("test/day25.txt", "r") as f:
    data = f.read().split("\n")  # This part may change

card_public = int(data[0])
door_public = int(data[1])


# Calculate loops

card_loop = 0

subject = 7
value = 1
while not value == card_public:
    card_loop += 1
    value = (value*subject) % 20201227

print(card_loop)

# Do the same for the door


# Calculate encryption key

key = 1
subject = door_public
for i in range(0, card_loop):
    key *= subject
    key = key % 20201227

print(key)
