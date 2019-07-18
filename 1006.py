a = float(input())
b = float(input())
c = float(input())
A = 2
B = 3
C = 5
if (a >= 0 and a <= 10.0) and (b >= 0 and b <= 10.0) and (c >= 0 and c <= 10.0):
    MEDIA = ((A*a)+(B*b)+(C*c))/(A+B+C)
    print("MEDIA = {:.1F}".format(MEDIA))
