# Variables
Sarah, Bob, Mike = 16, 21, 17
print(Sarah + Mike)
Name, age = 'Athena', 28
print(Name, age)
A = B = C = 99
print(A, B, C)

# Variables : local(lower_case), global(upper_case)
APPLE = 100  # this is global variable


def func():
    a = 10  # this is local variable
    global b  # b becomes global variable once the func is run
    b = 'global_b'
    print(a)
    print(APPLE)
    return a + 100


print(func())
print(b)
