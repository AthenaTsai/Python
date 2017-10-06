# Class: object-oriented programming, inheritance
class Parent:  # parent class, class is a structure, start with uppercase
    def __init__(self, name, age, ht=168):  # self tells the function is for which class
        self.name = name
        self.age = age
        self.ht = ht
        print('this is the parent class')

    def parent_func(self):
        print('your name is:' + self.name)

    def test(self):
        print('parent_before')


p = Parent('athena', 18)  # now creating an object
p.parent_func()


#
class Child(Parent):  # inherit contents from Parent class
    def child_func(self):
        print('this is the child func')

    def test(self):  # will overwrite parent methods
        print('child_after')


c = Child('Kev', 23)  # inherit this from Parent class
c.child_func()
c.parent_func()  # inherit this from Parent class
c.test()  # overwrite Parent class version
print(c.ht)