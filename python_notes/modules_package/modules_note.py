# Modules
import time

print(time.localtime())
import time as t  # shorten the name of a module

print(t.localtime())
from time import time, localtime  # only import parts of time module

print(time())
from time import *  # import all functions of time module

print(time())

# Module: self-defined
import mod1  # saved in the same folder named 'mod1.py'

mod1.printdata('Athena')