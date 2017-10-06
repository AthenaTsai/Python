# Creat file and write

# define variables
text = 'This is my 1st line.\nThis is 2nd line.\n3rd line here.'
append_text = '\nThis is appended text.'

# creat / over-write all
my_file = open('file_a.txt', 'w')
my_file.write(text)
my_file.close()

# append content
my_file = open('file_a.txt', 'a')
my_file.write(append_text * 2)
my_file.close()

# read content
my_file = open('file_a.txt', 'r')
content = my_file.read()
print('print content:\n ',content, '\n\n')
my_file.close()

# read each line
my_file = open('file_a.txt', 'r')
line1 = my_file.readline()  # read line 1
line2 = my_file.readline()  # read line 2
line3 = my_file.readline()  # read line 3
lineall = my_file.readlines()  # read the rest lines
print('readline_line1:\n ',line1, 'line2:\n ',line2,
      'line3:\n ',line3, 'print rest lines:\n ',lineall, '\n\n')
my_file.close()

# read lines
my_file = open('file_a.txt', 'r')
line = my_file.readlines()
print('\nuse readLines:\n'
      ' ',line)
my_file.close()

# for line to print
my_file = open('file_a.txt', 'r')
print('\n\nFOR to print lines:\n')
for line in my_file:
    print(line)
my_file.close()

# further control
my_file = open('file_a.txt', 'r')
print('\n\nFile name: ', my_file.name)
print('Is closed? ', str(my_file.closed))
print('Mode: ', my_file.mode)
my_file.close()
print('Is closed? ', str(my_file.closed))

