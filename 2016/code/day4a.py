from helpers.datagetter import aocd_data_in
from collections import defaultdict

din, aocd_submit = aocd_data_in(split=True, numbers=False)

ans = 0
for line in din:
    letters = defaultdict(int)
    for c in line:
        if c.isalpha():
            letters[c] += 1
        elif c == '[':
            break

    chk = line[-6:-1]
    id = int(line[-10:-7])

    checksum = list(letters.items())
    checksum.sort(key = lambda x : x[1] * 100 + 65 - ord(x[0]), reverse=True)
    checksum = "".join([x[0] for x in checksum][:5])
    
    if checksum == chk:
        ans += id

aocd_submit(ans)