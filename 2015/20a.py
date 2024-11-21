def divisors(n):
    divisors = [1]
    for i in range(2, n):
        if (n % i) == 0:
            divisors.append(i)
    return sum(divisors)


i = 1
while True:
    num = divisors(i)*10
    if num >= 33100000:
        print(i)
        exit()
    i += 1
