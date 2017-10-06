# Function vs Lambda vs map
def func1(x, y):
    return x + y


print(func1(3, 7))
func2 = lambda f, g: f * g  # lambda = short version function
print(func2(4, 8))
print(list(map(func1, [1], [2])))  # mapped processing
print(list(map(func1, [3, 300, 40000], [4, 400, 50000])))

# lambda nested
f = lambda a: lambda b: lambda c: a * b * c
print(f(5)(3)(2))

f = lambda c: lambda a, b: lambda d: (c * (a + b)) % d
print(f(2)(4, 3)(11))