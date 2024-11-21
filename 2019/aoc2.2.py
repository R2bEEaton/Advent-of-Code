thing = "input redacted"

list = thing.split(",")

def findthing(x, y):
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

    if ans == 19690720:
        print(x, y)

for x in range(0, 99):
    for y in range(0, 99):
        findthing(x, y)

"""
end_str = ""
print(list2)
for thing in sorted(list2):
    end_str += str(list2[thing]) + ","

print(end_str.rstrip(","))
print(ans)
"""