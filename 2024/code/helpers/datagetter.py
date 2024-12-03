import keyboard
import re


def aocd_data_in(split=True, numbers=False, n_type=int):
    print("| CTRL Ex  |  SHFT R |")
    key = keyboard.read_key()
    data_ver = "Real"

    if key == 'ctrl':
        data = open("testdata1.txt").read()
        data_ver = "Test"
    else:
        import aocd
        with open("helpers/sess") as f:
            sess = f.readline()
        dy = aocd.get_day_and_year()
        data = aocd.get_data(session=sess, day=dy[0], year=dy[1])
        with open("aoc.txt", "w+") as f:
            f.write(data)

    # Parse
    if split:
        data = data.splitlines()
    if numbers:
        out = []
        for line in (data if type(data) == list else data.splitlines()):
            out.append(get_numbers(line, n_type))
        data = out

    print("| %s Data loaded.  |\n|====================|" % data_ver)
    return data, submit if data_ver == "Real" else dummy_submit


def submit(ans):
    print("Submitting:", ans)
    import aocd
    with open("helpers/sess") as f:
        sess = f.readline()
    dy = aocd.get_day_and_year()
    aocd.submit(answer=ans, session=sess, day=dy[0], year=dy[1])


def dummy_submit(a):
    print("Answer:", a)
    print("Answer printed, not submitted.")


def get_numbers(a, t):
    return list(map(t, re.findall(r'(?:-)?\d+(?:\.\d+)?', a)))