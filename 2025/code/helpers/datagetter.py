import keyboard
import re
import time
import os

start_time = None


def aocd_data_in(split=True, numbers=False, n_type=int):
    print("| CTRL Ex  |  SHFT R |")
    key = keyboard.read_key()
    data_ver = "Real"

    # Get the directory where the calling script is located
    import inspect
    caller_frame = inspect.stack()[1]
    caller_dir = os.path.dirname(os.path.abspath(caller_frame.filename))

    if key == 'ctrl':
        testdata_path = os.path.join(caller_dir, "testdata1.txt")
        data = open(testdata_path).read()
        data_ver = "Test"
    else:
        import aocd
        sess_path = os.path.join(caller_dir, "helpers", "sess")
        with open(sess_path) as f:
            sess = f.readline()
        dy = aocd.get_day_and_year()
        data = aocd.get_data(session=sess, day=dy[0], year=dy[1])
        aoc_path = os.path.join(caller_dir, "aoc.txt")
        with open(aoc_path, "w+") as f:
            f.write(data)

    # Keep track of start time
    global start_time
    start_time = time.perf_counter()

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
    print("Answer:", ans, "\tTime:", time.perf_counter() - start_time)
    print("Submitting...")
    import aocd
    import inspect
    caller_frame = inspect.stack()[1]
    caller_dir = os.path.dirname(os.path.abspath(caller_frame.filename))
    sess_path = os.path.join(caller_dir, "helpers", "sess")
    with open(sess_path) as f:
        sess = f.readline()
    dy = aocd.get_day_and_year()
    aocd.submit(answer=ans, session=sess, day=dy[0], year=dy[1])


def dummy_submit(ans):
    print("Answer:", ans, "\tTime:", time.perf_counter() - start_time)
    print("Answer printed, not submitted.")


def get_numbers(a, t):
    return list(map(t, re.findall(r'(?:-)?\d+(?:\.\d+)?', a)))
