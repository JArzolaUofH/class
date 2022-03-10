# Justine Arzola 1804667
a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

finalsolution = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if a * x + b * y == c and d * x + e * y == f:
            print('{} {}'.format(x, y))
            finalsolution = True

if not finalsolution:
    print("No solution")
