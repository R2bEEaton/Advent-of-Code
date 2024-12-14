from helpers.datagetter import aocd_data_in
import random
import math

din, aocd_submit = aocd_data_in(split=True, numbers=True)
size = (101, 103)

i = 0
min_avg_dist = float('inf')

def avg_spread(data):
    robots = random.sample(data, len(data))
    dists = 0
    for i in range(len(robots) - 1):
        dists += math.dist(robots[i][:2], robots[i+1][:2])
    return dists / (len(robots)-1)


while True:
    for robot in din:
        robot[0] += robot[2]
        robot[0] %= size[0]
        robot[1] += robot[3]
        robot[1] %= size[1]
        
    i += 1
    dist = avg_spread(din)
    if dist < min_avg_dist:
        if i > 10 and dist / min_avg_dist < 0.85:
            aocd_submit(i)
            exit()
        min_avg_dist = dist