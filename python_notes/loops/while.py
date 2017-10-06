# While loops
print('TEST normal while:')
c = 0
while c < 5:  # make sure condition will become false at one point
    print(c)
    c = c + 1
print('now c is:', c)
# break: get here, stop the whole loop
print('TEST break:')
d = 0
while d < 5:
    print(d)
    if d == 3:
        break
    d = d + 1
    print('in while')
print('now d is:', d)
# continue: get here, stop this single loop and run next one
print('TEST continue:')
e = 0
while e < 5:
    e = e + 1
    if e == 3:
        continue
    print(e, 'in while')
print('now e is:', e)
# False
print('TEST false')
n = 0
while n < 5:
    print(n)
    if n == 3:
        n = 5
    else:
        pass
    n = n + 1
    print('in while')
print('now n is:', n)
# pass: used in while, for loops, just to put something later here
print('TEST pass')
f = 0
while f < 5:
    f = f + 1
    if f == 3:
        pass
    print(f)
print('now f is:', f)