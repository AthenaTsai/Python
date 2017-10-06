# Set

sentence = "Welcome Back to This Tutorial"
print(set(sentence))

# check sets
set1 = {1,2,3,4,5,6,7,7,7}
set2 = {6,6,7,8,9}
set3 = {2,3}
set4 = {'x','y'}

set1.add(8)
set1.remove(8)   # error if not exist
set1.discard(9)
set4.clear()

print(set1.difference(set2))
print(set1-set2)

print(set2.difference(set1))
print(set2-set1)

print(set1.intersection(set2))

print(set1 | set2)
print(set.union(set1,set2))

# check sub-set
print(set3 <= set1)