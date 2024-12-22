from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)


def mix(v, n):
    return v ^ n


def prune(n):
    return n % 16777216


ans = 0
for line in din:
    secret = line[0]
    for _ in range(2000):
        secret = mix(secret * 64, secret)
        secret = prune(secret)
        secret = mix(secret // 32, secret)
        secret = prune(secret)
        secret = mix(secret * 2048, secret)
        secret = prune(secret)
    ans += secret

aocd_submit(ans)