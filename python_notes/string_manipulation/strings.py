# String
firstName = 'Athena'
lastName = "Tsai"  # '', "" both ok
wholeName = 'Athena' + ' Tsai'
print(wholeName)
print('con' 'catenation')
print(firstName + ' ' + lastName)
print((firstName + ' ') * 3)
print('I\'m Athena.')
print('Apple' + '4')
print('Apple' + str(4))
print(int('1') + 2)
print(int(1.4) + 3)
print(firstName[0])  # cannot assign value to string position, imuttable type
print('Today I had {0} cups of {1}'.format(3, 'coffee'))
print('prices: ({x}, {y}, {z})'.format(x=2.0, y=1.5, z=5))
print('the {vehicle} had {0} crashes in {1} months'.format(5, 6, vehicle='car'))
print('{:<20}'.format('text'))
print('{:>20}'.format('text'))
print('{:b}'.format(21))
print('{:x}'.format(21))
print('{:o}'.format(21))
print(r'c:\number\nan')
print("""\
    Hello:
            User defined look
            Python output
    """)
