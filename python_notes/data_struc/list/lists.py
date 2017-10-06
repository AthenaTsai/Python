# Lists

list_mult = ['Apples', 'Bananas', 'Orange', 'Peach', 'Peach', 'Peach']
list_num = [1, 3, 5, 7, 23, 4, -1, 0]

list_mult.append('Bluberries')  # add to last
list_mult[len(list_mult):] = ['lenadd']  # add to last
list_mult[len(list_mult):] = (2, 3)  # add to last
print(list_mult)

list_mult.insert(3, '9999')  # add to assigned position
list_mult[0] = 'Lolllll'
del list_mult[2]
list_mult.remove('Peach')  # remove only the first found
print(list_mult[-4:5])
print(list_mult.index('Peach'))
print(list_mult.count('Peach'))
print(list_mult)

print(max(list_num))
print(min(list_num))
list_num.sort(reverse=True)  # reverse order
print(list_num)

# multi-dimension list
list_mult_dim = [[1, 2, 3],
                 [8, 9, 11],
                 ['2', 'r', 999]]
print(list_mult_dim[2][2])

