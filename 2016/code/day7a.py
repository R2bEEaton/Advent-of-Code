from helpers.datagetter import aocd_data_in
import re

din, aocd_submit = aocd_data_in(split=True, numbers=False)

ans = 0
for line in din:
    matches_inside = re.findall(r'(.)(.)(?=\2\1)', re.sub(r'\][^]]*\[|^[^\]]*\[|\][^\[]*$', ' ', line))
    matches_inside = list(filter(lambda x: x[0] != x[1], matches_inside))

    matches = re.findall(r'(.)(.)(?=\2\1)', re.sub(r'\[[^\[]*\]', ' ', line))
    matches = list(filter(lambda x: x[0] != x[1], matches))
    
    ans += 1 if len(matches) and not len(matches_inside) else 0

aocd_submit(ans)