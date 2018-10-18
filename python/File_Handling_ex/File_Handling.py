
f_open = open('test_file', 'r')
print(f_open.read())
print('')

f_open1 = open('test_file_2', 'r')
print(f_open1.readline()) # print only 1st line from the particular file if we used readline function

print('Using Write Function in test file 3 ')

f_write = open('test_file_3', 'w')
print()
f_write.write('adding data to test file 3') # this will erase all data of that file while using 'w' mode

print('')
f_write1 = open('test_file_3', 'a')
f_write.write('appending the data to filee 3 ') # this will append the data to that file while using 'a' mode and does not erase all the data

print('copying 1 file of the data to other file ')

for i in f_open1:
    f_write.write(i)