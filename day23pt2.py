class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.previous = None


data = ""

with open("inputs/day23.txt", "r") as f:
#with open("test/day23.txt", "r") as f:
    data = f.read()  # This part may change


data_list = list(data)
node_references = {}  # Store references to each node here
max = 0

index = 0
head = None
previous = None
for c in data_list:
    node = Node(int(c))
    node.previous = previous
    if previous is not None:
        previous.next = node
    else:
        head = node
    previous = node
    node_references[int(c)] = node
    index += 1


for i in range(index+1, 1000001):
    node = Node(i)
    node.previous = previous
    previous.next = node
    previous = node
    node_references[i] = node
    index += 1

previous.next = head
head.previous = previous

max = 1000000
current_cup_node = head

current_cup = current_cup_node.data

for i in range(0, 10000000):
    current_cup = current_cup_node.data
    selected = []
    dest_label = current_cup - 1

    iter_node = current_cup_node.next
    for r in range(0, 3):
        selected.append(iter_node.data)

        temp = iter_node.next

        iter_node.previous.next = iter_node.next
        iter_node.next.previous = iter_node.previous
        node_references[iter_node.data] = None

        iter_node = temp

    dest = None
    while True:  # This is not the place to optimize. This only runs max 3 times
        if dest_label in selected:
            dest_label -= 1
        elif dest_label <= 0:
            dest_label = max
        else:
            dest = node_references[dest_label]
            break

    for s in selected:
        new_node = Node(s)
        new_node.previous = dest
        new_node.next = dest.next
        dest.next = new_node
        new_node.next.previous = new_node

        dest = new_node
        node_references[dest.data] = dest

    current_cup_node = current_cup_node.next

one_node = node_references[1]
cup_1 = one_node.next.data
cup_2 = one_node.next.next.data

print(cup_1)
print(cup_2)
print(cup_1*cup_2)
