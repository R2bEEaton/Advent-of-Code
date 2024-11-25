from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=False)

line = list('.' + din + '.')
safe = 0

for _ in range(40):
    new_line = line.copy()
    safe += new_line.count('.') - 2
    for i in range(1, len(line) - 1):
        if line[i - 1] == '^' and line[i] == '^' and line[i + 1] == '.':
            new_line[i] = '^'
            continue
        if line[i - 1] == '.' and line[i] == '^' and line[i + 1] == '^':
            new_line[i] = '^'
            continue
        if line[i - 1] == '^' and line[i] == '.' and line[i + 1] == '.':
            new_line[i] = '^'
            continue
        if line[i - 1] == '.' and line[i] == '.' and line[i + 1] == '^':
            new_line[i] = '^'
            continue
        new_line[i] = '.'
    line = new_line

aocd_submit(safe)