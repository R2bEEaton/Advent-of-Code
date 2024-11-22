from helpers.datagetter import aocd_data_in
import hashlib

din, aocd_submit = aocd_data_in(split=False, numbers=False)

index = 0
pwd = [0] * 8
inserted = 0
while True:
    hash = hashlib.md5(bytes(din + str(index), encoding="UTF-8")).hexdigest()
    if str(hash)[:5] == "00000":
        try:
            if pwd[int(str(hash)[5])] == 0:
                pwd[int(str(hash)[5])] = str(hash)[6]
                inserted += 1
                if inserted == 8:
                    break
        except:
            None
    index += 1

aocd_submit("".join(pwd))