x, y, w, h = map(int,input().split())

if x >= (0.5*w):
    garo = abs(x-w)
else:
    garo = x

if y >= (0.5*h):
    sero = abs(y-h)
else:
    sero = y

result1 = ((x-w)**2 + (y-h)**2)**(1/2)
result2 = (x**2 + y**2)**(1/2)
linear = min(result1, result2)

print(min(garo, sero, linear))
