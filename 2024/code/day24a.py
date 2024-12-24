from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)

wires = {}
gates = []

initial = True
for line in din:
    if line == "":
        initial = False
        continue
    
    if initial:
        wire, val = line.split(": ")
        wires[wire] = int(val)
    else:
        wire_a, gate, wire_b, _, wire = line.split(" ")
        gates.append((wire_a, gate, wire_b, wire))


def do_gate(a, g, b):
    if g == "AND":
        return a & b
    elif g == "XOR":
        return a ^ b
    elif g == "OR":
        return a | b


while gates:
    for gate_x in gates:
        wire_a, gate, wire_b, wire = gate_x
        if wire_a in wires and wire_b in wires:
            wires[wire] = do_gate(wires[wire_a], gate, wires[wire_b])
            gates.remove(gate_x)
            break

print(wires)

zs = []
for wire in wires:
    if wire.startswith("z"):
        zs.append(wire)

zs.sort()
zs.reverse()

print(zs)
ans = 0
for wire in zs:
    print(wires[wire])
    ans |= wires[wire]
    ans <<= 1
ans >>= 1

aocd_submit(ans)