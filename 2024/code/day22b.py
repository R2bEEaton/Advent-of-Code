from collections import defaultdict
from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)


def mix(v, n):
    return v ^ n


def prune(n):
    return n % 16777216


windows = defaultdict(int)

for line in din:
    secret = line[0]
    prices = [secret % 10]
    for _ in range(2000):
        secret = mix(secret * 64, secret)
        secret = prune(secret)
        secret = mix(secret // 32, secret)
        secret = prune(secret)
        secret = mix(secret * 2048, secret)
        secret = prune(secret)
        prices.append(secret % 10)
    diffs = [prices[i] - prices[i-1] for i in range(1, len(prices))]
    seen = set()
    for i in range(len(diffs) - 4):
        if tuple(diffs[i:i+4]) in seen:
            continue
        seen.add(tuple(diffs[i:i+4]))
        windows[tuple(diffs[i:i+4])] += prices[i+4]

aocd_submit(max(windows.values()))