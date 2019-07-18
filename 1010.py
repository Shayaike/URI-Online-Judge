p1 = input().split(" ")
p2 = input().split(" ")

id1, q1, v1 = p1
id2, q2, v2 = p2

total = (int(q1) * float(v1)) + (int(q2) * float(v2))

print("VALOR A PAGAR: R$ {0:.2f}".format(total))
