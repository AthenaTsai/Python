# For loops
listA = ['cat', 'dog', 'goat']
tupA = (1, 3, 23)
for item in listA:
    print(item)
    print('next')
for item in tupA:
    print(item)
for i in range(0, 10):  # range function
    print(i)
a5 = range(0, 51, 5)  # skip function
for i in a5:
    print(i)
for i in range(0, 10, 3):  # nested for loops
    for j in range(0, 21, 10):
        print(i * j)

# For: 10 x 10 multiplication table
for i in range(1, 11):
    print('{:<3}|'.format(i), end="")
    for j in range(1, 11):
        print('{:>4}'.format(i * j), end="")
    if i == 1:
        print('\n{:#^44}'.format(""), end="")
    print("")