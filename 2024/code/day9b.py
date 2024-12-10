from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=False)

ans = 0

file = True
data = []
id = 0

for num in din:
    num = int(num)
    if file:
        data.append((id, num))
        id += 1
    else:
        data.append(("free", num))
    file = not file


seen = set()

r = len(data) - 1
while r >= 0:
    while data[r][0] == "free" or data[r][0] in seen:
        r -= 1
        if r == 0:
            idx = 0
            for thing in data:
                if thing[0] != "free":
                    for _ in range(thing[1]):
                        ans += thing[0] * idx
                        idx += 1
                else:
                    idx += thing[1]
            aocd_submit(ans)
            exit()
    seen.add(data[r][0])
    for l in range(r):
        if data[l][0] == "free" and data[l][1] >= data[r][1]:
            # print(f"found a spot for {data[r][0]} at {l}")
            remaining = data[l][1] - data[r][1]
            del data[l]
            data.insert(l, data[r - 1])
            data.insert(r + 1, ("free", data[r][1]))
            del data[r]
            if remaining > 0:
                data.insert(l+1, ("free", remaining))
            # print(data)
            break
