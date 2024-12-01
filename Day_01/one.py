# Read the input file
with open("input.txt") as f:
    lines = f.read().strip().split("\n")

# Parse the input into two separate lists
left = []
right = []

for line in lines:
    l, r = map(int, line.split())  # Split each line into two numbers
    left.append(l)                # Add to left list
    right.append(r)               # Add to right list

# Calculate the similarity score
similarity_score = 0

for num in left:
    count_in_right = right.count(num)  # Count occurrences in the right list
    similarity_score += num * count_in_right  # Increment similarity score

# Print the result
print("Similarity Score:", similarity_score)