scanners = []
import math
import numpy as np
import superpose3d

with open("input19.txt") as f:
    temp = []
    for line in f.readlines():
        line = line.strip()
        if "," in line:
            temp.append(list(map(int, line.split(","))))
        elif line == "":
            scanners.append(temp)
            temp = []
    scanners.append(temp)

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)


def get_dists(a):
    dists = []
    points = []
    for point1 in a:
        distz = []
        pointz = []
        for point2 in a:
            distz.append(dist(point1, point2))
            pointz.append((point1, point2))
        dists.append(distz)
        points.append(pointz)
    return dists, points


class Transform:
    def __init__(self, start, end, rotation, translation):
        self.start = start
        self.end = end
        self.rotation = np.round(rotation).astype(int)
        self.translation = np.round(translation).astype(int)

        #print(self.rotation)
        #print(self.translation)

    def apply(self, b):
        return (np.dot(self.rotation, np.array(b).T) + self.translation.reshape(-1, 1)).T.astype(int)


pairs = [[i, j] for i in range(len(scanners)) for j in range(i+1, len(scanners))]
pair_transforms = {}

new_pairs = []
for i, j in pairs:
    scanner1, points1 = get_dists(scanners[i])
    scanner2, points2 = get_dists(scanners[j])

    beacons1 = []
    beacons2 = []

    for dist1, point1 in zip(scanner1, points1):
        for dist2, point2 in zip(scanner2, points2):
            intersection = list(set(dist1).intersection(set(dist2)))
            if len(intersection) >= 12:
                if i != j:
                    if [i, j] not in new_pairs:
                        new_pairs.append([i, j])
                    for disty in intersection:
                        if point1[dist1.index(disty)][0] not in beacons1:
                            beacons1.append(point1[dist1.index(disty)][0])
                        if point2[dist2.index(disty)][0] not in beacons2:
                            beacons2.append(point2[dist2.index(disty)][0])

    if beacons1 and beacons2:
        beacons1 = np.array(beacons1)
        beacons2 = np.array(beacons2)

        RMSD, R, T, c = superpose3d.Superpose3D(beacons1, beacons2, allow_rescale=False)
        pair_transforms[f"{i} {j}"] = Transform(i, j, R, T)
        RMSD, R, T, c = superpose3d.Superpose3D(beacons2, beacons1, allow_rescale=False)
        pair_transforms[f"{j} {i}"] = Transform(j, i, R, T)

path_to_zero = [0, 23, 18, 13, 21, 16, 11, 11, 12, 12, 17, 21, 3, 18, 12, 2, 24, 21, 24, 1, 7, 2, 14, 17, 0]
#path_to_zero = [0, 0, 4, 1, 1] # For the example problem

pts = []

for i in range(len(scanners)-1):
    imd = i
    after = scanners[i]
    while imd != 0:
        imd2 = path_to_zero[imd]
        after = pair_transforms[f"{imd2} {imd}"].apply(after)
        imd = imd2
    for thing in after:
        pts.append(" ".join(list(map(str, thing))))

print(len(set(pts)))

best = 0
for a in pts:
    for b in pts:
        c = list(map(float, a.split(" ")))
        d = list(map(float, b.split(" ")))
        best = max((c[0] - d[0]) + (c[1] - d[1]) + (c[2] - d[2]), best)

print(best)