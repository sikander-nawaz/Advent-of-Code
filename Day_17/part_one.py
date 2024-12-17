# def run_3bit_program(registers, program):
#     # Initialize registers and instruction pointer
#     A, B, C = registers
#     IP = 0
#     output = []

#     # Helper function to get combo operand value
#     def get_combo_value(operand):
#         if operand <= 3:
#             return operand
#         elif operand == 4:
#             return A
#         elif operand == 5:
#             return B
#         elif operand == 6:
#             return C
#         else:
#             raise ValueError("Invalid combo operand: 7 should not appear in valid programs")

#     # Program execution loop
#     while IP < len(program):
#         opcode = program[IP]
#         operand = program[IP + 1]
#         IP += 2  # Default instruction pointer increment

#         if opcode == 0:  # adv
#             divisor = 2 ** get_combo_value(operand)
#             A = A // divisor

#         elif opcode == 1:  # bxl
#             B = B ^ operand

#         elif opcode == 2:  # bst
#             B = get_combo_value(operand) % 8

#         elif opcode == 3:  # jnz
#             if A != 0:
#                 IP = operand

#         elif opcode == 4:  # bxc
#             B = B ^ C

#         elif opcode == 5:  # out
#             output.append(get_combo_value(operand) % 8)

#         elif opcode == 6:  # bdv
#             divisor = 2 ** get_combo_value(operand)
#             B = A // divisor

#         elif opcode == 7:  # cdv
#             divisor = 2 ** get_combo_value(operand)
#             C = A // divisor

#         else:
#             raise ValueError(f"Invalid opcode: {opcode}")

#     return ",".join(map(str, output))


# # Read input file
# with open("input.txt", "r") as file:
#     lines = file.readlines()

# # Parse register values
# register_line = lines[0].strip()
# registers = [int(val.split(":")[1].strip()) for val in register_line.split(",")]

# # Parse program instructions
# program_line = lines[1].strip()
# program = list(map(int, program_line.split(":")[1].strip().split(",")))

# # Run the program
# output = run_3bit_program(registers, program)

# # Print the output
# print(output)



class Computer:
    def __init__(self, program, reg_a=0, reg_b=0, reg_c=0):
        self.program = program
        self.registers = {'A': reg_a, 'B': reg_b, 'C': reg_c}
        self.ip = 0
        self.output = []

    def get_combo_value(self, operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return self.registers['A']
        elif operand == 5:
            return self.registers['B']
        elif operand == 6:
            return self.registers['C']
        else:
            raise ValueError(f"Invalid combo operand: {operand}")

    def run(self):
        self.output = []  # Reset output
        self.ip = 0  # Reset instruction pointer
        while self.ip < len(self.program) - 1:
            opcode = self.program[self.ip]
            operand = self.program[self.ip + 1]
            
            if opcode == 0:  # adv
                self.registers['A'] //= (2 ** self.get_combo_value(operand))
            elif opcode == 1:  # bxl
                self.registers['B'] ^= operand
            elif opcode == 2:  # bst
                self.registers['B'] = self.get_combo_value(operand) % 8
            elif opcode == 3:  # jnz
                if self.registers['A'] != 0:
                    self.ip = operand
                    continue
            elif opcode == 4:  # bxc
                self.registers['B'] ^= self.registers['C']
            elif opcode == 5:  # out
                self.output.append(self.get_combo_value(operand) % 8)
            elif opcode == 6:  # bdv
                self.registers['B'] = self.registers['A'] // (2 ** self.get_combo_value(operand))
            elif opcode == 7:  # cdv
                self.registers['C'] = self.registers['A'] // (2 ** self.get_combo_value(operand))
            
            self.ip += 2
        return self.output

def solve_part2():
    program = [2,4,1,5,7,5,1,6,0,3,4,0,5,5,3,0]
    reg_a = 24847151  # Register A initial value
    reg_b = 0         # Register B initial value
    reg_c = 0         # Register C initial value

    print(f"Program to match: {program}")
    
    # Start from the given Register A value
    a = reg_a
    found = False
    attempts = 0
    
    while not found:
        computer = Computer(program, reg_a=a, reg_b=reg_b, reg_c=reg_c)
        output = computer.run()
        
        attempts += 1
        
        # Debug printing every 100000 attempts
        if attempts % 100000 == 0:
            print(f"Tried A = {a}")
            print(f"Current output: {output}")
        
        if output == program:
            print(f"\nFound matching output!")
            print(f"A = {a}")
            print(f"Output: {output}")
            found = True
        else:
            a += 1
    
    return a

# Run the solution
result = solve_part2()
print(f"\nLowest working value for register A: {result}")
