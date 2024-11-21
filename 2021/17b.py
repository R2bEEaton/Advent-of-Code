with open("input17.txt") as f:
    line = f.read()
    x_min = line.split("x=")[1].split(",")[0].split("..")
    x_min, x_max = int(x_min[0]), int(x_min[1])
    y_min = line.split("y=")[1].split("..")
    y_min, y_max = int(y_min[0]), int(y_min[1])


max_ys = []

for i in range(1, 1000):
    for j in range(-1000, 1000):
        x = 0
        y = 0
        x_vel = i
        y_vel = j
        ymax = []
        for its in range(1000):
            x += x_vel
            y += y_vel
            if x_vel > 0:
                x_vel -= 1
            elif x_vel < 0:
                x_vel += 1
            y_vel -= 1
            ymax.append(y)
            if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
                max_ys.append(max(ymax))
                break
            if x > x_max or y < y_min:
                break

print(len(max_ys))
