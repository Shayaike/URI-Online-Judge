amount = int(input())


if amount >= 365:
    h = (int(amount/365))
    amount = amount % 365
else:
    h = 0
if amount >= 30:
    m = (int(amount/30))
    amount = amount % 30
else:
    m = 0
if amount >= 1:
    s = (int(amount/1))

else:
    s = 0

print("{} ano(s)".format(h))
print("{} mes(es)".format(m))
print("{} dia(s)".format(s))
