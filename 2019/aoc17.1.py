thing = "input redacted"
thing = thing.split(",")

class MyIter:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        self.cur = self.start
        while self.cur < self.stop:
            yield self.cur
            self.cur += 1


def find_thing():
    output = []
    list2 = {}
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
            print("INPUT!")
            inp = input("Input: ")
            list2[x] = int(inp)
            m.cur += 1
        elif opcode == "04" or opcode == "4":
            #print("OUTPUT!")
            output.append(str(list2[x]))
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


map = []
m = []
for test in find_thing():
    print(chr(int(test)), end="")
    if int(test) != 10:
        m.append(chr(int(test)))
    else:
        map.append(m)
        m = []

print(map)

def check_around(x, y):
    try:
        if map[x+1][y] == "#" and map[x-1][y] == "#" and map[x][y+1] == "#" and map[x][y-1] == "#" and map[x][y] == "#":
            return True
    except:
        return False
    return False

ans = 0

for x in range(0, len(map)-1):
    for y in range(0, len(map[0])-1):
        if check_around(x, y):
            ans += x*y

print(ans)

