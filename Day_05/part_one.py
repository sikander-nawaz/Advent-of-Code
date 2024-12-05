from collections import defaultdict

# Function to check if a given update is in the correct order
def is_correct_order(update, rules):
    index_map = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map and index_map[x] > index_map[y]:
            return False
    return True

# Function to find the middle page of a correctly-ordered update
def find_middle_page(update):
    return update[len(update) // 2]

# Parse the input file
with open("input.txt", "r") as file:
    data = file.read().split("\n\n")
    ordering_rules = [tuple(map(int, line.split('|'))) for line in data[0].splitlines()]
    updates = [list(map(int, line.split(','))) for line in data[1].splitlines()]

# Process updates and calculate the sum of middle pages
rules_set = set(ordering_rules)
result = sum(find_middle_page(update) for update in updates if is_correct_order(update, rules_set))

print(result)
