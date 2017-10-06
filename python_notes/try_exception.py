# Try, if not work, go to except
try:
    file = open('eeee', 'r+')  # r+ means read and write
except Exception as e:
    print('there is no such file')
    response = input('creat this file? press \'y\'')
    if response == 'y':
        file = open('eeee', 'w')
    else:
        print('fine,whatever..')
else:
    file.write('new things')
    file.close()

# Exception Handling
try:
    n = int(input('Enter an integer:'))
except ValueError:
    print('That is not an integer')

try:
    sum = 0
    file = open('numbers.txt', 'r')
    for number in file:
        sum = sum + 1.0 / int(number)
    print(sum)
except ZeroDivisionError:
    print('Number in file equal to zero!')
except IOError:
    print('File doesn\'t exit')
finally:
    print('sum =', sum)

# Raise exception
a = 1


def RaiseException(a):
    if type(a) != type('a'):
        raise ValueError('This is not string')


try:
    RaiseException(a)
except ValueError as e:
    print(e)


# Raise exception, assert sth happens then do sth following
def test_case(a, b):
    assert a < b, 'a is greater than b'


try:
    test_case(2, 1)
except AssertionError as e:
    print(e)