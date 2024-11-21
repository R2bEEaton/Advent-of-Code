input = """input redacted"""

ans = 0
import math

for thing in input.split("\n"):
    new = int(thing)
    while new > 0:
        ans += math.floor((int(new)/3)-2)
        new = math.floor((int(new)/3)-2)
        print(new)
    ans -= new

print(ans)
