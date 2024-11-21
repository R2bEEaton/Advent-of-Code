input = """input redacted"""
input = input.split("\n")


def every(list, n, type):
    ret = []
    for i in range(0, len(list), n):
        app = []
        for j in range(n):
            try:
                app.append(type(list[i+j]))
            except:
                None
        ret.append(app)
    return ret


def sloop(list, type):
    list_out = []
    for a in list:
        for b in list:
            list_out.append((type(a), type(b)))
    return list_out


#print(every(input, 4, int))
#print(sloop(input, int))

dicty = {}

for thing in input:
    dicty[thing.split(" => ")[1]] = thing.split(" => ")[0]

def recurse(elem):
    for thing in dicty.keys():
        if elem in str(thing):
            return int(str(thing).split(" ")[0]), "".join([i for i in dicty[thing] if (i.isdigit() or i is ",")]).replace(" ", "").split(","), "".join([i for i in dicty[thing] if not i.isdigit()]).replace(" ", "").split(",")


# replaced with
leftovers = {x.split(" ")[1] : 0 for x in dicty.keys()}
item = ["FUEL"]
ore = 0

import math

while item != []:
    newitem = []
    for thing in item:
        if leftovers[thing]: # this works because 0 is considered False in Python
            leftovers[thing] -= 1 # we already have one "thing", no need to make more
        else:
            rec = recurse(thing)
            leftovers[thing] = rec[0] - 1 # we created "rec[0]" of "thing", and we just used one, leaving "rec[0] - 1" leftovers
            for i in range(len(rec[2])):
                if rec[2][i] == "ORE":
                    ore += int(rec[1][i])
                else:
                    for j in range(math.ceil(int(rec[1][i]))):
                        newitem.append(rec[2][i])
    item = newitem
    print(item)
    print("=====================")

print(ore)
