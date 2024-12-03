from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=False)

ans = 0
nest = 0
ignore = False
garbage = False

for i in range(len(din)):
    if ignore:
        ignore = False
        continue

    if din[i] == "{" and not garbage:
        nest += 1
        ans += nest
    if din[i] == "}" and not garbage:
        nest -= 1

    if din[i] == "<":
        garbage = True
    if din[i] == ">":
        garbage = False
    
    if din[i] == "!":
        ignore = True


aocd_submit(ans)