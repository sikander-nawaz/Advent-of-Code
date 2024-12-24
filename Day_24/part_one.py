def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

    wire_values = {}
    gates = []

    for line in lines:
        if ":" in line:
            wire, value = line.split(": ")
            wire_values[wire] = int(value)
        elif "->" in line:
            gates.append(line)

    return wire_values, gates

def evaluate_gate(gate, wire_values):
    parts = gate.split()

    if "AND" in parts:
        a, _, b, _, out = parts
        wire_values[out] = wire_values.get(a, 0) & wire_values.get(b, 0)
    elif "OR" in parts:
        a, _, b, _, out = parts
        wire_values[out] = wire_values.get(a, 0) | wire_values.get(b, 0)
    elif "XOR" in parts:
        a, _, b, _, out = parts
        wire_values[out] = wire_values.get(a, 0) ^ wire_values.get(b, 0)

    return wire_values

def simulate_gates(wire_values, gates):
    unresolved_gates = gates[:]

    while unresolved_gates:
        next_unresolved = []

        for gate in unresolved_gates:
            parts = gate.split()
            a, _, b, _, out = parts

            if a in wire_values and b in wire_values:
                wire_values = evaluate_gate(gate, wire_values)
            else:
                next_unresolved.append(gate)

        unresolved_gates = next_unresolved

    return wire_values

def get_output(wire_values):
    z_wires = {k: v for k, v in wire_values.items() if k.startswith('z')}
    sorted_z_wires = [v for k, v in sorted(z_wires.items())]
    binary_output = ''.join(map(str, sorted_z_wires[::-1]))
    return int(binary_output, 2)

if __name__ == "__main__":
    input_file = "input.txt"
    wire_values, gates = parse_input(input_file)
    wire_values = simulate_gates(wire_values, gates)
    result = get_output(wire_values)
    print(result)
