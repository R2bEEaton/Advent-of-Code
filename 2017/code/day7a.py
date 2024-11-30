from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)

supported_by = {}

for line in din:
    if line.split()[0] not in supported_by:
        supported_by[line.split()[0]] = ""
    if "-" not in line:
        continue
    for on in line.split('-> ')[1].split(", "):
        supported_by[on] = line.split()[0]

for disc, supp in supported_by.items():
    if supp == "":
        aocd_submit(disc)
        break