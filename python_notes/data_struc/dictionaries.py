# Dictionaries: paring keys and values
# cannot use Dict[3] to refer to dict position, has to use key

Dict1 = {'Athena': 28, 'Kevin': 27, 'Tony': 50, ('k','e','y'): 3}

print(Dict1['Athena'])
print(len(Dict1))
Dict1['Athena'] = 18  # Change Dict item value
del Dict1['Tony']  # delete Dict item
Dict1['Dav'] = {'x': 33, 'y': 434}  # add Dict item to Dict
print(Dict1)
print(Dict1['Dav']['x'])
print(Dict1.keys())
print(Dict1.values())
Dict1.clear()
print(Dict1)

my_dictionary = {x: x+1 for x in range(10)}
print(my_dictionary)