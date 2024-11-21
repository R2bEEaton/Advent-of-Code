inp = "3113322113" + "R"

for iter in range(40):
    i = 0
    inp2 = ""
    while i < len(inp)-1:
        t = 0
        while inp[i+t] == inp[i]:
            t += 1
        inp2 += str(t) + str(inp[i])
        i += t
    inp = inp2 + "R"

print(len(inp) - 1)
