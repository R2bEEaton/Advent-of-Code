thing = "input redacted"

list = thing.split(",")


def find_thing(x, y):
    list2 = {}
    for i in range(0, len(list)):
        list2[int(i)] = int(list[i])

    ans = 0

    list2[1] = x
    list2[2] = y

    for t in range(0, len(list2), 4):
        if list2[t] == 1:
            ans = list2[list2[t+1]]+list2[list2[t+2]]
            list2[list2[t+3]] = list2[list2[t+1]]+list2[list2[t+2]]
        elif list2[t] == 2:
            ans = list2[list2[t+1]]*list2[list2[t+2]]
            list2[list2[t+3]] = list2[list2[t+1]]*list2[list2[t+2]]
        else:
            break

    return ans


print(find_thing(12, 2))
