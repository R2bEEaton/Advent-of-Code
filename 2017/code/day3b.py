from helpers.datagetter import aocd_data_in
from helpers.matrix import Matrix

din, aocd_submit = aocd_data_in(split=False, numbers=False)
din = int(din)

G = Matrix((101, 101))

def conv_to(pos):
    center = (G.size[0] // 2, G.size[1] // 2)
    return (pos[0] + center[0], pos[1] + center[1])

dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
facing = 0

G[conv_to((0, 0))] = 1

curr = [0, 0]
each = 0
cnt = 0
reset = False

while True:
    if curr[0] == curr[1] and curr[0] >= 0:
        reset = True
        #curr[1] += 1

    tot = max(sum([val for val, n in G.neighbors(conv_to(curr), diag=True)]), 1)
    
    if tot > din:
        aocd_submit(tot)
        exit()
    
    G[conv_to(curr)] = tot
    print(cnt, curr, tot)
 
    cnt += 1
    if each != 0 and cnt % each == 0:
        facing += 1

    if not reset:
        curr[0] += dirs[facing % len(dirs)][0]
        curr[1] += dirs[facing % len(dirs)][1]
    else:
        print(reset)
        curr[1] += 1
        each += 2
        facing = 0
        cnt = 0
        reset = False