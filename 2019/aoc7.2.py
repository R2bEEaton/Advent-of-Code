thing = "input redacted"

list3 = thing.split(",")


class MyIter:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        self.cur = self.start
        while self.cur < self.stop:
            yield self.cur
            self.cur += 1


def find_thing(inp1, inp2):
    o = 0
    output = 0
    global adv
    list2 = {}
    for i in range(0, len(list3)):
        list2[int(i)] = int(list3[i])

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
        else:
            x = t+1
        if modes[1] == 0:
            y = list2[t+2]
        else:
            y = t+2
        if modes[2] == 0:
            z = list2[t+3]
        else:
            z = t+3

        if opcode == "01" or opcode == "1":
            list2[z] = list2[x]+list2[y]
            m.cur += 3
        elif opcode == "02" or opcode == "2":
            list2[z] = list2[x]*list2[y]
            m.cur += 3
        elif opcode == "03" or opcode == "3":
            #print("INPUT!")
            if o == 0:
                inp = inp1
            elif o == 1:
                inp = inp2
            list2[x] = int(inp)
            m.cur += 1
            o += 1
        elif opcode == "04" or opcode == "4":
            #print("OUTPUT %s" % list2[x])
            output = list2[x]
            #print("out")
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
        else:
            break

    #print(o)
    return output


def isUniqueChars(st):
    # String length cannot be more than
    # 256.
    if len(st) > 256:
        return False

    # Initialize occurrences of all characters
    char_set = [False] * 128

    # For every character, check if it exists
    # in char_set
    for i in range(0, len(st)):

        # Find ASCII value and check if it
        # exists in set.
        val = ord(st[i])
        if char_set[val]:
            return False
        if int(st[i]) < 5:
            return False

        char_set[val] = True

    return True

nummm = 0

import tqdm

done = 0
test = 0
while done == 0:
    test += find_thing(5, find_thing(6, find_thing(7, find_thing(8, find_thing(9, test)))))
    print(test)


"""for i in tqdm.tqdm(range(99999)):
    num = ""
    for j in range(5-len(str(i))):
        num += "0"
    num = num + str(i)
    if isUniqueChars(num):
        test = 0
        done = 0
        while done == 0:
            test = find_thing(num[4], find_thing(num[3], find_thing(num[2], find_thing(num[1], find_thing(num[0], test)))))

        if test > nummm:
            nummm = test

print(nummm)
"231864"""""