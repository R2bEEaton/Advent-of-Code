# Ryan Eaton 2024-11-21

n = 33100000
house = [0] * (n // 10)

for i in range(1, n // 10):
    for j in range(i, min(n // 10, i + i * 50), i):
        house[j] += i * 11

for i, h in enumerate(house):
    if h >= n:
        print(i)
        break