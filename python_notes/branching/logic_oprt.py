# Logic operators: not > and > or
d = 5
e = 1
f = False
g = 'python'
h = 'some'
z = not ((not (e <= d) and (g >= h)) or f) and 1
print(bool(z))