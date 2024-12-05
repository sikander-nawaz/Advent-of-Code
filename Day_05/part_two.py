from collections import defaultdict, deque

# Function to parse input data
def parse_input(file_path):
    with open(file_path, 'r') as file:
        sections = file.read().strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in sections[0].splitlines()]
    updates = [list(map(int, line.split(','))) for line in sections[1].splitlines()]
    return rules, updates

# Function to validate an update
def is_update_valid(rules, update):
    index_map = {page: i for i, page in enumerate(update)}
    return all(index_map[x] < index_map[y] for x, y in rules if x in index_map and y in index_map)

# Topological sort to reorder pages
def reorder_update(rules, update):
    adj_list = defaultdict(list)
    in_degree = defaultdict(int)
    update_set = set(update)

    for x, y in rules:
        if x in update_set and y in update_set:
            adj_list[x].append(y)
            in_degree[y] += 1
            in_degree[x]  # Ensure all nodes are in-degree tracked.

    for page in update_set:
        if page not in in_degree:
            in_degree[page] = 0

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_pages = []

    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return [page for page in sorted_pages if page in update_set]

# Function to calculate the sum of middle pages
def calculate_sum_of_middle_pages(file_path):
    rules, updates = parse_input(file_path)
    incorrect_updates = [update for update in updates if not is_update_valid(rules, update)]
    reordered_updates = [reorder_update(rules, update) for update in incorrect_updates]
    return sum(update[len(update) // 2] for update in reordered_updates)

# File path
input_file_path = "input.txt"

# Calculate and print result
result = calculate_sum_of_middle_pages(input_file_path)
print(result)
