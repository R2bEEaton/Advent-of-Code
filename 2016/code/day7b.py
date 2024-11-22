from helpers.datagetter import aocd_data_in
import re

din, aocd_submit = aocd_data_in(split=True, numbers=False)

ans = 0
for line in din:
    matches_inside = re.findall(r'(?=((.)(?!\2).\2))', re.sub(r'\][^]]*\[|^[^\]]*\[|\][^\[]*$', '  ', line))
    matches_inside = [x[0] for x in matches_inside]

    matches = re.findall(r'(?=((.)(?!\2).\2))', re.sub(r'\[[^\[]*\]', '  ', line))
    matches = [x[0] for x in matches]

    for inside in matches_inside:
        if f"{inside[1]}{inside[0]}{inside[1]}" in matches:
            ans += 1
            break

aocd_submit(ans)