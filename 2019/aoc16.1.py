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


input = """input redacted"""

pattern = [0, 1, 0, -1]

end = []

for i in range(len(input)):
    pat = []
    for x in range(len(input)):
        for thing in pattern:
            for j in range(i + 1):
                pat.append(thing)
                if len(pat) > len(input):
                    break
    pat.pop(0)
    end.append(pat[:len(input)])


def do(inp):
    endans = ""

    for k in range(len(end)):
        ans = 0
        for i in range(len(inp)):
            ans += int(str(inp[i])[-1])*end[k][i]
        endans += str(ans)[-1]

    #print(endans)
    return endans


import tqdm

for x in tqdm.tqdm(range(100)):
    input = do(input)

print(input)
