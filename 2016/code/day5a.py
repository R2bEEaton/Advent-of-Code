from helpers.datagetter import aocd_data_in
import hashlib

din, aocd_submit = aocd_data_in(split=False, numbers=False)

index = 0
pwd = ""
while True:
    hash = hashlib.md5(bytes(din + str(index), encoding="UTF-8")).hexdigest()
    if str(hash)[:5] == "00000":
        pwd += str(hash)[5]
        if len(pwd) == 8:
            break
    index += 1

aocd_submit(pwd)