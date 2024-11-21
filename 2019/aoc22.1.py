inp = """input redacted"""

inp = inp.split("\n")

def deal_into(l):
    l.reverse()
    return l

def deal_with(l, n):
    new = {}
    j = n
    x = 0
    while len(new) < len(l):
        for i in range(0, len(l)*n, n):
            num = i%len(l)
            new[num] = l[x]
            x += 1
        j += 1

    thing = []
    for i in range(len(new)):
        thing.append(new[i])
    return thing

def cut(l, n):
    return l[n:] + l[:n]

cards = []
cardorig = []

for i in range(10007):
    cards.append(i)
    cardorig.append(i)

for x in range(119315717514047):
    if cards == cardorig and x != 0:
        print("WOAH!!", x)
        break
    else:
        print(x)
    for thing in inp:
        if thing.startswith("deal into"):
            cards = deal_into(cards)
        elif thing.startswith("deal with"):
            cards = deal_with(cards, int(thing.split(" ")[-1]))
        else:
            cards = cut(cards, int(thing.split(" ")[-1]))

        #print(cards)

print(cards[2020])