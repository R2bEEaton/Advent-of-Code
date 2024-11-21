x = "input redacted"
n=150

list=[]
for i in range(0,len(x),n):
    list.append(x[i:i+n])
print(list)

new_list = {}

for i in range(0, len(list)):
    for j in range(0, len(list[i])):
        if list[i][j] != "2":
            try:
                print(new_list[j])
            except:
                print(list[i][j])
                new_list[j] = list[i][j]

string = ""

for thing in sorted(new_list):
    string += str(new_list[thing])

print(string)

x = string
n=25

list=[]
for i in range(0,len(x),n):
    list.append(x[i:i+n])
print(list)

list2 = []

for i in range(0, len(list)):
    list2.append([])
    for char in list[i]:
        list2[i].append(int(char))

list = list2
print(list)

import matplotlib.pyplot as plt
import numpy as np

X = np.array(list)

print(X)
plt.imshow(X, cmap="gray")
plt.show()