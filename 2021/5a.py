board = []
for i in range(1000):
    temp = []
    for j in range(1000):
        temp.append(0)
    board.append(temp)

with open("input5.txt") as f:
    for line in f.readlines():
        x1 = int(line.split(" ")[0].split(",")[0])
        y1 = int(line.split(" ")[0].split(",")[1])
        x2 = int(line.split(" ")[2].split(",")[0])
        y2 = int(line.split(" ")[2].split(",")[1])

        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1+1, x2+1)):
                for y in range(min(y1, y2), max(y1+1, y2+1)):
                    board[x][y] += 1

c = 0
for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] > 1:
            c += 1

print(c)
