p1 = input().split(" ")
a, b, c = p1
a = int(a)
b = int(b)
c = int(c)
a_b = int((a+b+abs(a-b))/2)
maxabc = int((a_b+c+abs(a_b-c))/2)
print("{} eh o maior".format(maxabc))
