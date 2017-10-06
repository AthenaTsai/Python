# Copy: deep vs shallow
import copy

a = [1, 2, [7, 8]]
b = a
print('\nb equals to a:', b, '\n')
print('a, b ID same?', id(a) == id(b))
print('a[1], b[1] ID same?', id(a[1]) == id(b[1]))
print('a[2], b[2] ID same?', id(a[2]) == id(b[2]))
print('a[2][0], b[2][0] ID same?', id(a[2][0]) == id(b[2][0]), '\n')
b[0] = 'b99'
print('b[0] modified to: b99\n', 'a=', a, '\nb=', b)
b = [6, 6, [7, 8]]
print('\nb modified to:[6,6,[7,8]]\n', 'a=', a, '\nb=', b)

c = copy.copy(a)
print('\nc shallow copy from a:', c)
c[2][0] = 'ccyy'
print('\nc[2][0] modified to: ccyy\n', 'a=', a, '\nc=', c)
c[2] = ['cc', 'cccc']
print('\nc[2] modified to: [\'cc\', \'cccc\']\n', 'a=', a, '\nc=', c)

d = copy.deepcopy(a)
print('\nd deep copy from a:', d)
print('\na[2][1] and d[2][1] ID same?', id(a[2][1]) == id(d[2][1]))
d[2][1] = 'dd'
print('\nd[2][1] modified to: dd\n', 'a=', a, '\nd=', d)
