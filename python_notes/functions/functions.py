# Function: basic
def hellow():
    print('hello world')


hellow()


def greeting(username):
    print('hello ' + username + '!')


greeting('Athnea')


def sum_no(no1, no2):
    print(no1 + no2)


sum_no(3, 5)


def returna(no3, no4):
    return no3 + no4


sumof = returna(12, 34)
print(sumof)


def f(a):
    def g(b):
        def h(c):
            return a * b * c

        return h

    return g


print(f(5)(2)(3))


# Function: default value, undefined values put in front
def sale_car(price, colour='red', brand='camry', is_second_hand=True):
    print('price:', price, 'colour:', colour, 'brand:', brand,
          'is_second_hand:', is_second_hand)


sale_car(1000)
sale_car(1000, 'white')
sale_car(1000, brand='bmw')

# Functions: In-built
print(abs(-3))
print(bool(3 > 5))
print(bool(5 > 3))
print(bool(None))
print(bool(0))
# dir: all the functions i can use with this item
print(dir('hello'))
# help: tells work how
sent = "hello"
help(sent.upper)
help(sent.splitlines)
# Eval function:
sent = 'print("hi")'
eval(sent)  # one line code
exec(sent)  # more complicated multi lines python code
# other funcs
a = 1
print(str(a))
print(float(a))
print(int(a))