# tuples
# an immutable data type, similar to strings

tup = (1, 'abc', 2, 'cde')
tup1 = 3, 'efd', True
tup2 = 'A'
tup3 = ('B',)
tup4 = tup1[0:2] + tup3 + ('star',)
tup5 = (3,5,9,4,1)


print(tup[1])
print(len(tup1))
print(tup[1:4])
print(tup[:3])
print('5min: ', min(tup5))
print('5max:', max(tup5))

# Check elements
print(3 in tup)
print('efd' in tup1)

# print elements
for x in tup1:
    print(x)

# cannot assign new values
try:
    tup2[0] = 9
except Exception as e:
    print(e)

# return a tuple as a result of a function
def multiple_result():
    return(1,2,'a')
print(multiple_result())

# match tuples
print((1,2,3) == (1,2))