c = 0


def escape(text):
    s = "\"\""
    for char in text:
        if char.isalpha() or char.isnumeric():
            s += char
        else:
            s += "\\%s" % char
    return s


with open('input8.txt') as f:
    for line in f.readlines():
        line = line.strip()
        c += len(escape(line)) - len(line)

print(c)
