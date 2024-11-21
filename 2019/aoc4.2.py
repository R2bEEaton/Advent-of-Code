x = 0
for i in range(372037, 905157):
    dup = 0
    inc = 1
    for j in range(0, len(str(i))):
        try:
            if str(i)[j] == str(i)[j + 1] and str(i)[j] != str(i)[j - 1] and str(i)[j] != str(i)[j + 2]:
                dup = 1
        except:
            try:
                if str(i)[j] == str(i)[j+1] and str(i)[j] != str(i)[j-1]:
                    dup = 1
            except:
                None

        try:
            if int(str(i)[j + 1]) < int(str(i)[j]):
                inc = 0
        except:
            None

    if dup == 1 and inc == 1:
        print(i)
        x += 1

print(x)
