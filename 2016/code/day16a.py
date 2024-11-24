from helpers.datagetter import aocd_data_in
import itertools

din, aocd_submit = aocd_data_in(split=False, numbers=False)
disk = 272

while len(din) < disk:
    a = din
    b = a[::-1]
    b = "".join(['0' if x == '1' else '1' for x in b])
    din = a + '0' + b

chk = din[:disk]
while len(chk) % 2 == 0:
    new_chk = ""
    for batch in itertools.batched(chk, 2):
        if "".join(batch) in ['00', '11']:
            new_chk += '1'
        else:
            new_chk += '0'
    chk = new_chk

aocd_submit(chk)
