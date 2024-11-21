rs = {"a": 0, "b": 0}
ins = []

with open("input23.txt") as f:
    for line in f.readlines():
        line = line.strip()
        ins.append(line)

i = 0
while True:
    try:
        instr = ins[i].split(" ")[0]
        r = ins[i].split(" ")[1].replace(",", "")
        match instr:
            case "hlf":
                rs[r] /= 2
            case "tpl":
                rs[r] *= 3
            case "inc":
                rs[r] += 1
            case "jmp":
                i += int(r)-1
            case "jie":
                if rs[r] % 2 == 0:
                    i += int(ins[i].split(", ")[1])-1
            case "jio":
                if rs[r] == 1:
                    i += int(ins[i].split(", ")[1])-1
        i += 1
    except:
        break

print(rs["b"])
