import hashlib

i = 0

with open("input4.txt") as f:
    text = f.read()
    while True:
        if hashlib.md5(bytes(text + str(i), 'utf-8')).hexdigest().startswith("00000"):
            print(i)
            break
        i += 1
