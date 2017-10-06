# hiding info
# encapsulation
# inheritance
# polymorphism

# methods are special functions inside the body of a class
# __ this will become private
# property can be decorator
# There should be only one obvious way to do something

import math


class Complex(object):
    'this class simulates complex numbers'

    def __init__(self, real=0, imag=0):
        if (type(real) not in (int, float)) or type(imag) not in (int, float):
            raise Exception('Args are not numbers!')
        self.SetReal(real)
        self.SetImag(imag)

    def GetReal(self):
        return self.__real

    def GetImag(self):
        return self.__imag

    def GetModulus(self):
        return math.sqrt(self.GetReal() * self.GetReal() + self.GetImag() * self.GetImag())

    def GetPhi(self):
        return math.atan2(self.GetImag(), self.GetReal())

    def SetReal(self, val):
        if type(val) not in (int, float):
            raise Exception('real part must be a number')
        self.__real = val

    def SetImag(self, val):
        if type(val) not in (int, float):
            raise Exception('imag part must be a number')
        self.__imag = val

    def __str__(self):
        return str(self.GetReal()) + '+' + str(self.GetImag()) + 'i'

    def __add__(self, other):
        return Complex(self.GetReal() + other.GetReal(), self.GetImag() + other.GetImag())

    def __mul__(self, other):
        if type(other) in (int, float):
            return Complex(self.GetReal() * other, self.GetImag() * other)
        else:
            return Complex(self.GetReal() * other.GetReal() - self.GetImag() * other.GetImag(),
                           self.GetImag() * other.GetReal() + self.GetReal() * other.GetImag())

    def __truediv__(self, other):
        if type(other) in (int, float):
            return Complex(self.GetReal() / float(other), self.GetImag() / float(other))
        else:
            a, b, c, d = self.GetReal(), self.GetImag(), other.GetReal(), other.GetImag()
            nominator = c * c + d * d
            return Complex((a * c + b * d) / nominator, (b * c - a * d) / nominator)






c = Complex()
print(c.GetReal(), c.GetImag())
c.SetImag(1)
c.SetReal(2)
print(c.GetReal(), c.GetImag())

d = Complex(-3, 4)
print(d.GetModulus(), d.GetPhi())

e = Complex(5, 0.3)
f = Complex(-3, 4)
print(e + f)
print(e * f)
print(e / f)
print(e)

try:
    print(c.__real)  # cannot use .__real
except Exception as e:
    print(e)

try:
    c = Complex((1, 2, 3), [1, 2, 3])
    print(c.real, c.imag)
except Exception as e:
    print(e)
