from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=False)

def good(x, y):
    return str(bin(x*x + 3*x + 2*x*y + y + y*y + int(din))[2:]).count('1') % 2 == 0

seen = set()

steps = 0
visit_next = set()
init = (1, 1)
visit_next.add(init)
while steps <= 50:
    new_visit_next = set()
    for pos in visit_next:
        if pos in seen:
            continue
        seen.add(pos)
        x, y = pos
        new_visit_next.update([(nx, ny) for nx, ny in[(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]if 0 <= nx and 0 <= ny and good(nx, ny)])
    visit_next = new_visit_next
    steps += 1


aocd_submit(len(seen))