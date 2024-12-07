from itertools import product

# Read the input file
with open("D:/GitHub/Advent of Code/Day_07/input.txt", "r") as file:
    lines = file.readlines()

def evaluate_expression(numbers, operators):
    """
    Evaluates an expression with given numbers and operators in a left-to-right manner,
    including the concatenation operator (||).
    """
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

total_calibration_result = 0

for line in lines:
    # Parse the line to extract the test value and numbers
    test_value, numbers = line.strip().split(":")
    test_value = int(test_value.strip())
    numbers = list(map(int, numbers.strip().split()))
    
    # Generate all combinations of operators
    operator_count = len(numbers) - 1
    possible_operators = product(['+', '*', '||'], repeat=operator_count)
    
    # Check if any combination of operators matches the test value
    for operators in possible_operators:
        if evaluate_expression(numbers, operators) == test_value:
            total_calibration_result += test_value
            break

# Output the total calibration result
print(total_calibration_result)
