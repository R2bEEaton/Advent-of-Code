x = 0
for i in range(372037, 905157):
    dup = 0
    inc = 0
    for j in range(0, len(str(i))):
        try:
            if str(i)[j] == str(i)[j+1]:
                dup = 1
            if int(str(i)[j+1]) < int(str(i)[j]):
                inc = 1

        except:
            None
    if dup == 1 and inc != 1:
        print(i)
        x += 1

print(x)
