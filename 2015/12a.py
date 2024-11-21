import json

with open("input12.txt") as f:
    j = json.loads(f.read())

total = 0


def get_numbers(thing):
    global total
    if isinstance(thing, dict):
        for key in thing:
            get_numbers(thing[key])
    if isinstance(thing, list):
        for item in thing:
            get_numbers(item)
    if isinstance(thing, int):
        total += thing


get_numbers(j)
print(total)
