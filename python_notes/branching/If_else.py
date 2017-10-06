# If else
print(2 == 2)  # use == to compare, = means assigning a value
print(3 != 2)
if 5 > 3 or 1 > 2:  # 'or' statement
    print('(5>3 or 1>2, yes!')
else:
    print('(5>3 or 1>2,no!')
if 4 > 2 and 4 > 5:
    print('4>2 and 4>5, yes!!')
else:
    print('4>2 and 4>5, no!!!')
# if, elif, else: each should be mutually exclusive
age = 16
if age < 13:
    print('you are young')
elif 18 > age >= 13:
    print('you are a teenageer')  # once meet, exit if-else loop
elif age < 20:
    pritn('still no power')
else:
    print('you are an adult')
# one line condition statement
passerby_speech = ""
me = 'Hi' if passerby_speech == 'Hello' or passerby_speech == 'Hi' else 'Hey'
print(me)
# another example
a = 7 if 3 ** 2 > 9 else 14
print(a)