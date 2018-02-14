def luhn(n):
    r = [int(ch) for ch in str(n)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d * 2, 10)) for d in r[1::2])) % 10 == 0

l=[49927398716, 499273, 123456, 123578]
for n in (l):
    print(n, luhn(n))

# === Output === #

# 49927398716 True
# 499273 False
# 123456 False
# 123578 False