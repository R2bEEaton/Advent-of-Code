thing = "input redacted"
thing = thing.split(",")

directions = [["n", "n"], ["n", "n", "e"], ["n", "e"], ["n", "e", "e", "n"], ["w", "w", "w"], ["e", "e"], ["e", "e", "e"], ["e", "e", "e", "e"]]

from itertools import permutations

dirs = []
for x in range(1, 8):

    # Get all permutations of length 2
    # and length 2
    dirs.append(list(permutations(directions, x)))

class MyIter:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        self.cur = self.start
        while self.cur < self.stop:
            yield self.cur
            self.cur += 1


def find_thing(dir):
    output = []
    list2 = {}
    inplist = []
    relbase = 0
    for i in range(0, len(thing)):
        list2[int(i)] = int(thing[i])

    m = MyIter(0, len(list2))
    for t in m:
    #for t in range(0, len(list2), adv):
        opcode = str(list2[t])[-2:]
        if len(str(list2[t])) > 2:
            mod = str(list2[t])[:-2]
        else:
            mod = ""
        modes = []
        for i in range(3-len(mod)):
            modes.append(0)
        for char in mod:
            modes.append(int(char))
        modes.reverse()

        #print("Opcode: " + opcode)
        #print(modes)

        if opcode == "99":
            break

        if modes[0] == 0:
            x = list2[t+1]
        elif modes[0] == 1:
            x = t+1
        else:
            x = list2[t+1]+relbase

        if modes[1] == 0:
            y = list2[t+2]
        elif modes[1] == 1:
            y = t+2
        else:
            y = list2[t+2]+relbase

        if modes[2] == 0:
            z = list2[t+3]
        elif modes[2] == 1:
            z = t+3
        else:
            z = list2[t+3]+relbase

        if opcode == "01" or opcode == "1":
            list2[z] = list2[x]+list2[y]
            m.cur += 3
        elif opcode == "02" or opcode == "2":
            list2[z] = list2[x]*list2[y]
            m.cur += 3
        elif opcode == "03" or opcode == "3":
            #print("INPUT!")

            import random
            if inplist == []:
                """l = []
                for elem in "".join(output).split("- ")[1:]:
                    test = elem.rstrip().split("\n")[0]
                    if test == "north" or test == "south" or test == "east" or test == "west":
                        l.append(elem.rstrip().split("\n")[0])
                    else:
                        if test != "escape pod" and test != "molten lava" and test != "photons" and test != "infinite loop" and test != "giant electromagnet":
                            l.append("take " + elem.rstrip().split("\n")[0])

                l.append("inv")


                inp = random.choice(l)"""
                try:
                    if dir[0] == "take":
                        for elem in "".join(output).split("- ")[1:]:
                            test = elem.rstrip().split("\n")[0]
                            if test != "north" and test != "south" and test != "east" and test != "west":
                                if test != "escape pod" and test != "molten lava" and test != "photons" and test != "infinite loop" and test != "giant electromagnet":
                                    inp = "take " + elem.rstrip().split("\n")[0]
                    else:
                        inp = dir[0]
                except:
                    if "typing" in "".join(output):
                        return True
                    else:
                        return False

                #print(inp, "THIS IS WHAT IS INPUTTED")
                dir.pop(0)

                for char in inp:
                    inplist.append(ord(char))
                inplist.append(10)

            list2[x] = int(inplist[0])
            inplist.pop(0)
            m.cur += 1
        elif opcode == "04" or opcode == "4":
            print(str(chr(list2[x])), end="")
            output.append(str(chr(list2[x])))
            m.cur += 1

        elif opcode == "05" or opcode == "5":
            if list2[x] != 0:
                m.cur = list2[y]-1
            else:
                m.cur += 2
        elif opcode == "06" or opcode == "6":
            if list2[x] == 0:
                m.cur = list2[y]-1
            else:
                m.cur += 2
        elif opcode == "07" or opcode == "7":
            if list2[x] < list2[y]:
                list2[z] = 1
            else:
                list2[z] = 0
            m.cur += 3
        elif opcode == "08" or opcode == "8":
            if list2[x] == list2[y]:
                list2[z] = 1
            else:
                list2[z] = 0
            m.cur += 3
        elif opcode == "09" or opcode == "9":
            relbase += list2[x]
            #print("relbase" + str(relbase))
            m.cur += 1
        else:
            break

    return output

def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

for elem in dirs:
    dir = []
    print(dir)
    for elem2 in elem:
        for elem3 in elem2:
            for elem4 in elem3:
                if elem4 == "n":
                    dir.append("north")
                if elem4 == "s":
                    dir.append("south")
                if elem4 == "e":
                    dir.append("east")
                if elem4 == "w":
                    dir.append("west")
        dir.append("take")
        for elem3 in elem2:
            for elem4 in Reverse(elem3):
                if elem4 == "n":
                    dir.append("south")
                if elem4 == "s":
                    dir.append("north")
                if elem4 == "e":
                    dir.append("west")
                if elem4 == "w":
                    dir.append("east")

    dir.append("east")
    dir.append("east")
    dir.append("east")
    dir.append("east")
    dir.append("north")
    dir.append("east")
    print(dir)

    if find_thing(dir):
        break