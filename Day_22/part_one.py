def mix_and_prune(secret_number, multiplier, divisor=None):
    if divisor:
        value = secret_number // divisor
    else:
        value = secret_number * multiplier
    
    mixed = secret_number ^ value
    pruned = mixed % 16777216
    return pruned

def generate_secret_sequence(initial_secret, steps):
    secret = initial_secret
    for _ in range(steps):
        secret = mix_and_prune(secret, 64)
        secret = mix_and_prune(secret, 1, 32)
        secret = mix_and_prune(secret, 2048)
    return secret

def sum_of_2000th_secrets(file_path):
    with open(file_path, 'r') as file:
        initial_secrets = [int(line.strip()) for line in file.readlines()]
    
    total = 0
    for secret in initial_secrets:
        total += generate_secret_sequence(secret, 2000)
    
    return total

# Replace 'input.txt' with the path to your input file
file_path = 'input.txt'
result = sum_of_2000th_secrets(file_path)
print(result)
