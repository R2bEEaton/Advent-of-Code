from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)

tot = 0
for line in din:
    words = ["".join(sorted(list(x))) for x in line.split()]
    for word in words:
        if words.count(word) > 1:
            break
    else:
        tot += 1

aocd_submit(tot)