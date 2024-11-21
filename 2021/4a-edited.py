boards = []

with open("input4.txt") as f:
    lines = f.readlines()
    moves = lines[0].split(",")
    for i in range(2, len(lines), 6):
        board = []
        for j in range(0, 5):
            line = []
            for k in range(0, 5):
                line.append(int(lines[i+j].split()[k]))
            board.append(line)
        boards.append(board)

for num in moves:
    for board in range(len(boards)):
        for y in range(5):
            for x in range(5):
                if boards[board][x][y] == int(num):
                    boards[board][x][y] = True
                    if any(all(boards[board][x][y] == True for x in range(5)) for y in range(5)):
                        total = 0
                        for i in range(5):
                            for j in range(5):
                                if boards[board][i][j] != True:
                                    total += int(boards[board][i][j])
                        exit(print(total * int(num)))
