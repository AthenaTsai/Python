# Variables
Sarah, Bob, Mike = 16, 21, 17
print (Sarah + Mike)
Name, age = 'Athena', 28
print (Name, age)
A = B = C = 99
print (A, B, C)

# Variables : local(lower_case), global(upper_case)
APPLE = 100 #this is global variable
def func():
    a = 10 #this is local variable
    global b #b becomes global variable once the func is run
    b = 'global_b'
    print(a)
    print(APPLE)
    return a+100
print(func())
print(b)

# String
firstName = 'Athena'
lastName = "Tsai" # '', "" both ok
print (firstName + ' ' + lastName)
print ((firstName + ' ' )*3)
print ('I\'m Athena.')
print ('Apple'+'4')
print ('Apple'+str(4))
print (int('1') +2)
print (int(1.4) +3)

# Calculation
print(1+1)
print(5-1)
print(2*10)
print(2**4)
print(8%3)
print(9/4)
print(9//4)

# Position
sent1 = 'Athena is learning Python'
print (sent1[0], sent1[1])
print (sent1[0:5])
print (sent1[:3])
print (sent1[:-2])

# Placeholder
nameA = 'Athena'
sent2 = '%s is 15 years old.'
print (sent2)
print (sent2%nameA)
print (sent2%'Ashe')
#
sent3 = '%s %s is the president of the US.'
print (sent3%('Barack', 'Obama'))
#
sent4 = '%s is %d years old.'
print (sent4%('John', 33))
sent5 = sent4%('Jay', 50)
print (sent5)

# Lists
shopList = ['Apples', 'Bananas', 'Orange', 'Peach', 'Peach', 'Peach']
print (shopList [0])
print (shopList [0:2])
print (shopList[-3:])
shopList.append('Bluberries') # add item to last
shopList.insert(3,'9999') # add item to assigned position
print (shopList)
shopList[0] = 'Lolllll' # change item
print (shopList)
del shopList[2] # delete item no.
print (shopList)
shopList.remove('Peach') # remove item name, only the first found
print (shopList)
print (len(shopList)) # calculate list length
# add lists
shopList2 = ['shampoo', 'tempon', 'soap']
print (shopList + shopList2) 
print (shopList*2) # multiply list
print(shopList.index('Peach'))
print(shopList.count('Peach'))
# find value in list
listNum = [1,3, 5, 7, 23, 4, -1, 0]
print (max (listNum))
print (min (listNum))
listNum.sort(reverse=True) # reverse order
print(listNum)
# Lists : multi-dimension
a_mult_dim = [ [1,2,3],
               [8,9,11],
               ['2','r',999]]
print(a_mult_dim[2][2])

# List: zip
a = [1,2,3]
b = ['x','y',9]
c = list(zip(a,b,b))
print(c)
for i,j,k in c:
    print(i/2, str(j)+'ok', str(k))
##
# Set
sentence = "Welcome Back to This Tutorial"
print(set(sentence))
#
char_list =('a','b','c','c','d','d','d')
unique_char = set(char_list)
unique_char.add('s')
unique_char.discard('x') # remove will appear error if not exist
print (unique_char)
# unique_char.clear() # remove all items
set1 = unique_char
set2 = {'a','e','i'}
print(set1.difference(set2))
print(set1.intersection(set2))

# Dictionaries
Dict1 = {'Athena':28, 'Kevin':27, 'Tony':50}
print (Dict1)
print (Dict1['Athena'])
print (len(Dict1))
Dict1['Athena']=18 # Change Dict item value
print (Dict1)
del Dict1['Tony'] # delete Dict item
Dict1['Dav'] = {'x':33, 'y':434} # add Dict item
print (Dict1)
print(Dict1['Dav']['x'])
# dont repeat keys
Dict2 = {'Bob':12, 'Bob':13, 'Bob': 18} 
print (Dict2['Bob'])

# Tuple
tup1 = ('pen', 'pencil', 'paper')
print (tup1)
print (tup1[0:2])
print (len(tup1))
# neither modify nor delete
##tup1[0] = 'email'
##print (tup1)
# can add up tuples
tup2 = (23,55,30,1)
tup3 = tup1 + tup2
print (tup3)
# can delete the whole tuple
##del tup3
##print (tup3)
# multiply
tup5 = 'hi'
print (tup5 *4)

# If else
print (2 ==2) # use == to compare, = means assigning a value
print (3!=2)
if (5>3 or 1>2): # 'or' statement
    print ('(5>3 or 1>2, yes!')
else:
    print ('(5>3 or 1>2,no!')
if (4>2 and 4>5):
    print('4>2 and 4>5, yes!!')
else:
    print ('4>2 and 4>5, no!!!')
# if, elif, else
age = 16
if (age < 13):
    print ('you are young')
elif (age >= 13 and age < 18):
    print ('you are a teenageer') # once meet, exit if-else loop
elif (age < 20):
    pritn ('still no power')
else:
    print ('you are an adult')    

# For loops
listA = ['cat', 'dog', 'goat']
tupA = (1,3,23)
for item in listA:
    print(item)
    print('next')
for item in tupA:
    print(item)
for i in range(0,10): # range function
    print (i)
a5 = range(0,51,5) # skip function
for i in a5:
    print(i)
for i in range(0,10,3): # nested for loops
    for j in range(0,21,10):
        print(i*j)

# While loops
print('TEST normal while:')
c = 0
while c < 5: # make sure condition will become false at one point
    print(c)
    c = c + 1
print('now c is:', c) 
# break: get here, stop the whole loop
print('TEST break:')
d = 0
while d < 5:
    print(d)
    if d == 3:
        break
    d = d + 1
    print('in while')
print('now d is:', d)   
# continue: get here, stop this single loop and run next one
print('TEST continue:')
e = 0
while e < 5:
    e = e + 1
    if e == 3:
        continue
    print(e, 'in while')
print('now e is:', e)     
# False
print('TEST false')
n = 0
while n <5:
    print (n)
    if n ==3:
        n=5
    else:
        pass
    n = n+1
    print('in while')
print('now n is:', n)                
# pass: used in while, for loops, just to put something later here
print('TEST pass')
f = 0
while f < 5:
    f = f + 1
    if f == 3:
        pass
    print(f)
print('now f is:', f) 

# Try, if not work, go to except
try:
    file = open('eeee','r+') # r+ means read and write
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

# Function: basic
def helloW(): 
    print('hello world')
helloW()
def Greeting(userName):
    print('hello ' + userName + '!')
Greeting('Athnea')
def SumNo(no1, no2):
    print(no1 + no2)
SumNo(3,5)
def returnA (no3, no4):
    return (no3 + no4)
    print ('this line wont be printed, cuz return then skip rest')
sum = returnA (12, 34)
print(sum)

# Function: default value, undefined values put in front
def sale_car(price, colour='red', brand='camry', is_second_hand=True):
    print('price:', price, 'colour:', colour, 'brand:', brand,
          'is_second_hand:', is_second_hand)
sale_car(1000)
sale_car(1000, 'white')
sale_car(1000, brand='bmw')

# Functions: In-built
print(abs(-3))
print(bool(3>5))
print(bool(5>3))
print(bool(None))
print(bool(0))
# dir: all the functions i can use with this item
print(dir ('hello'))
# help: tells work how
sent = "hello"
help(sent.upper)
help(sent.splitlines)
# Eval function:
sent = 'print("hi")'
eval(sent) # one line code
exec(sent) # more complicated multi lines python code
# other funcs
a = 1
print(str(a))
print(float(a))
print(int(a))

# Function vs Lambda vs map
def func1(x,y):
    return(x+y)
print(func1(3,7))
func2 = lambda f,g: f*g # lambda = short version function
print(func2(4,8))
print(list(map(func1,[1],[2]))) # mapped processing
print(list(map(func1,[3,300,40000],[4,400,50000])))

# Class: object-oriented programming, inheritance
class Parent: # parent class, class is a structure, start with uppercase
    def __init__(self, name, age, hight = 168): # self tells the function is for which class
        self.name = name
        self.age = age
        self.hight = hight
        print('this is the parent class')
    def parentFunc(self):
        print('your name is:' + self.name)
    def test(self):
        print('parent_before')
p = Parent('athena', 18) # now creating an object
p.parentFunc()
#
class Child(Parent): # inherit contents from Parent class
    def childFunc(self):
        print('this is the child func')
    def test(self): # will overwrite parent methods 
        print('child_after')
c = Child('Kev', 23) # inherit this from Parent class
c.childFunc()
c.parentFunc() # inherit this from Parent class
c.test() # overwrite Parent class version
print(c.hight)

# Creat file and write
text = 'This is my 1st line.\nThis is 2nd line.\n3rd line here.'
append_text = '\nThis is appended text.'
my_file = open('my file.txt', 'w')
my_file.write(text) # creat / over-write all
my_file.close()
my_file = open('my file.txt', 'a') # append content
my_file.write(append_text)
my_file.write(append_text)
my_file.close()
file = open('my file.txt', 'r') # read content
content = file.read()
print(content)
my_file.close()
file = open('my file.txt', 'r') # read line
line1 = file.readline() # read line 1
line2 = file.readline() # read line 2
line3 = file.readline() # read line 3
lineall = file.readlines() # read the rest lines
print(line1,line2, line3, lineall)
my_file.close()
file = open('my file.txt', 'r') # read line
line = file.readlines()
print(line)
my_file.close()

# Input
a_input = input('Age?')
if int(a_input) < 7:
    print('Go away')
elif (int(a_input) >= 7 and int(a_input) < 18):
    print('Still go away')
else:
    print('Enjoy!')

# Modules
import time
print(time.localtime())
import time as t # shorten the name of a module
print(t.localtime())
from time import time, localtime # only import parts of time module
print(time())
from time import *  # import all functions of time module
print(time())

# Module: self-defined
import mod1 #saved in the same folder named 'mod1.py'
mod1.printdata('Athena')

# Copy: deep vs shallow
import copy
a = [1,2,[7,8]]
b = a
print('\nb equals to a:', b, '\n')
print ('a, b ID same?', id(a) == id(b))
print ('a[1], b[1] ID same?', id(a[1]) == id(b[1]))
print ('a[2], b[2] ID same?', id(a[2]) == id(b[2]))
print ('a[2][0], b[2][0] ID same?', id(a[2][0]) == id(b[2][0]), '\n')
b[0] = 'b99'
print ('b[0] modified to: b99\n','a=',a,'\nb=',b)
b = [6,6,[7,8]]
print ('\nb modified to:[6,6,[7,8]]\n','a=',a,'\nb=',b)

c = copy.copy(a)
print('\nc shallow copy from a:', c)
c[2][0] = 'ccyy'
print ('\nc[2][0] modified to: ccyy\n','a=',a,'\nc=',c)
c[2] = ['cc', 'cccc']
print ('\nc[2] modified to: [\'cc\', \'cccc\']\n','a=',a,'\nc=',c)

d = copy.deepcopy(a)
print('\nd deep copy from a:', d)
print('\na[2][1] and d[2][1] ID same?', id(a[2][1]) == id(d[2][1]))
d[2][1] = 'dd'
print ('\nd[2][1] modified to: dd\n','a=',a,'\nd=',d)

'''
install modules
terminal: "sudo pip3 install numpy"
terminal: "sudo pip3 uninstall numpy"
'''



