# Ryan Eaton 2024-11-21

import math

def divisors(n):
    sum = 0
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if (n % i) == 0:
            sum += i + n / i
    if math.sqrt(n).is_integer():
        sum -= math.sqrt(n)
    return sum


i = 2
while True:
    num = divisors(i)*10
    if num >= 33100000:
        print(i)
        break
    i += 1
