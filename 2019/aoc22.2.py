inp = """input redacted"""

inp = inp.split("\n")

def deal_into(l):
    l.reverse()
    return l

def deal_with(l, n):
    new = {}
    x = 0
    for i in range(0, len(l)*n, n):
        num = i%len(l)
        new[num] = l[x]
        x += 1

    thing = []
    for i in range(len(new)):
        thing.append(new[i])
    return thing

def cut(l, n):
    return l[n:] + l[:n]

cards = []

for i in range(119315717514047):
    cards.append(i)



for x in range(0):
    for thing in inp:
        if thing.startswith("deal into"):
            cards = deal_into(cards)
        elif thing.startswith("deal with"):
            cards = deal_with(cards, int(thing.split(" ")[-1]))
        else:
            cards = cut(cards, int(thing.split(" ")[-1]))

        #print(cards)

print(cards[2020])