diagram = {}

with open("input7.txt") as f:
    for lines in f.readlines():
        lines = lines.split()
        diagram[lines[len(lines)-1]] = " ".join(lines[0:len(lines)-2])


print(diagram)
diagram['b'] = '3176'


def get_value(name):
    if name.isnumeric():
        return int(name)
    else:
        line = diagram[name].split()
        if "AND" in line:
            ans = get_value(line[0]) & get_value(line[2])
        elif "OR" in line:
            ans = get_value(line[0]) | get_value(line[2])
        elif "LSHIFT" in line:
            ans = get_value(line[0]) << int(line[2])
        elif "RSHIFT" in line:
            ans = get_value(line[0]) >> int(line[2])
        elif "NOT" in line:
            ans = ~ get_value(line[1])
        else:
            ans = get_value(line[0])
        diagram[name] = str(ans)
        return ans


print(get_value('a'))
