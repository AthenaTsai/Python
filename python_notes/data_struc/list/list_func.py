# zip
a = [1, 2, 3]
b = ['x', 'y', 9]
c = list(zip(a, b, b))
print(c)
for i, j, k in c:
    print(i / 2, str(j) + 'ok', str(k))

# map
print(tuple(map(lambda x: x ** 2 + 3 * x + 1, [1, 2, 3, 4])))
print(list(map(lambda x: x ** 2 + 3 * x + 1, [1, 2, 3, 4])))
print(list(map(lambda x: x ** 2 + 3 * x + 1, (1, 2, 3, 4))))

# filter
print(list(filter(lambda x: x <4, [1,2,3,4,5,6,3,1,0,-1])))

# redult
import functools
print(functools.reduce(lambda x,y: x*y, [1,2,3,4]))