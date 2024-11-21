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

marks = boards.copy()
#print(boards)
#print(marks)


def is_winner(marked):
    if marked[0][0] == "X" and marked[0][1] == "X" and marked[0][2] == "X" and marked[0][3] == "X" and marked[0][4] == "X":
        return True
    elif marked[1][0] == "X" and marked[1][1] == "X" and marked[1][2] == "X" and marked[1][3] == "X" and marked[1][4] == "X":
        return True
    elif marked[2][0] == "X" and marked[2][1] == "X" and marked[2][2] == "X" and marked[2][3] == "X" and marked[2][4] == "X":
        return True
    elif marked[3][0] == "X" and marked[3][1] == "X" and marked[3][2] == "X" and marked[3][3] == "X" and marked[3][4] == "X":
        return True
    elif marked[4][0] == "X" and marked[4][1] == "X" and marked[4][2] == "X" and marked[4][3] == "X" and marked[4][4] == "X":
        return True
    elif marked[0][0] == "X" and marked[1][0] == "X" and marked[2][0] == "X" and marked[3][0] == "X" and marked[4][0] == "X":
        return True
    elif marked[0][1] == "X" and marked[1][1] == "X" and marked[2][1] == "X" and marked[3][1] == "X" and marked[4][1] == "X":
        return True
    elif marked[0][2] == "X" and marked[1][2] == "X" and marked[2][2] == "X" and marked[3][2] == "X" and marked[4][2] == "X":
        return True
    elif marked[0][3] == "X" and marked[1][3] == "X" and marked[2][3] == "X" and marked[3][3] == "X" and marked[4][3] == "X":
        return True
    elif marked[0][4] == "X" and marked[1][4] == "X" and marked[2][4] == "X" and marked[3][4] == "X" and marked[4][4] == "X":
        return True
    else:
        return False


for num in moves:
    for board in range(0, len(boards)):
        for y in range(0, 5):
            for x in range(0, 5):
                if boards[board][x][y] == int(num):
                    marks[board][x][y] = "X"
                    if is_winner(marks[board]):
                        print("FOUND WINNER!")
                        total = 0
                        for i in range(0, 5):
                            for j in range(0, 5):
                                if marks[board][i][j] != "X":
                                    total += int(marks[board][i][j])
                        print(total * int(num))
                        exit()
