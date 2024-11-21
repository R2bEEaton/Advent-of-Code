instructions = []

with open("input24.txt") as f:
    for line in f.readlines():
        line = line.strip()
        instructions.append(line.split(" "))


def check(num):
    data = {"w": 0, "x": 0, "y": 0, "z": 0}
    n = 0
    for i in instructions:
        try:
            val = int(i[2])
        except IndexError:
            val = 0
        except ValueError:
            val = int(data[i[2]])
        match i[0]:
            case "inp":
                if n > 0 and data["z"] == 0:
                    print(data)
                data[i[1]] = int(str(num)[n])
                n += 1
            case "add":
                data[i[1]] += val
            case "mul":
                data[i[1]] *= val
            case "div":
                if val == 0:
                    print("div by zero")
                    return
                data[i[1]] /= val
            case "mod":
                if data[i[1]] < 0 or val <= 0:
                    print("bad mod")
                    return
                data[i[1]] %= val
            case "eql":
                if data[i[1]] == val:
                    data[i[1]] = 1
                else:
                    data[i[1]] = 0

    if data["z"] == 0:
        print("FOUND!!")
        print(num)
        exit()


for i in range(99999999999999, 10000000000000, -1):
    if "0" not in str(i):
        check(i)