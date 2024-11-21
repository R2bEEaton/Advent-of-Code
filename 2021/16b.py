with open("input16.txt") as f:
    my_hexdata = f.read().strip()

data = ""
for char in my_hexdata:
    data += bin(int(char, 16))[2:].zfill(4)
print(data)


def gnl(bits):
    try:
        version = bits[0:3]
    except:
        return None
    try:
        type = bits[3:6]
    except:
        return None

    p = False
    vals = []
    j = 0
    while not p:
        try:
            if bits[6 + j] == '0':
                p = True
            vals.append(bits[7+j:11+j])
            j += 5
        except:
            p = True

    if version != "" and type != "" and len(vals) > 0:
        return [6+j] + [version, type] + vals
    return None


def gnop(bits):
    version, type = "", ""
    try:
        version = bits[0:3]
    except:
        return None
    try:
        type = bits[3:6]
    except:
        return None

    try:
        if bits[6] == '0':
            p = int(bits[7:22], 2)
            s = 15
        else:
            p = int(bits[7:18], 2)
            s = 11
    except:
        return None

    if s == 15:
        i = 0
        packets = []
        found = False
        while not found:
            if bits[7+s+i+3:7+s+i+6] == "":
                found = True
            else:
                if int(bits[7+s+i+3:7+s+i+6], 2) == 4:
                    packet = gnl(bits[7+s+i:7+s+p])
                else:
                    packet = gnop(bits[7+s+i:7+s+p])
                if packet == None:
                    found = True
                else:
                    i += packet[0]
                    packets.append(packet)
        return [7+s+i] + [version, type] + packets
    if s == 11:
        i = 0
        packets = []
        while p > 0:
            if bits[7+s+i+3:7+s+i+6] == "":
                found = True
            else:
                if int(bits[7+s+i+3:7+s+i+6], 2) == 4:
                    packet = gnl(bits[7+s+i:])
                else:
                    packet = gnop(bits[7+s+i:])
                i += packet[0]
                packets.append(packet)
                p -= 1
        return [7+s+i] + [version, type] + packets


version = int(data[3:6], 2)
packet = ""
if version == 4:
    packet = gnl(data)
else:
    packet = gnop(data)


def operate(packet):
    version = int(packet[2], 2)
    print(version)
    packets = []
    if version != 4:
        packets = [operate(x) for x in packet[3:]]
    match version:
        case 0:
            return sum(packets)
        case 1:
            t = 1
            for e in packets:
                t *= e
            return t
        case 2:
            return min(packets)
        case 3:
            return max(packets)
        case 4:
            return int("".join(packet[3:]), 2)
        case 5:
            return int(packets[0] > packets[1])
        case 6:
            return int(packets[0] < packets[1])
        case 7:
            return int(packets[0] == packets[1])


print(packet)
print("Answer: ", operate(packet))
