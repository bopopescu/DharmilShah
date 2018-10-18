print('To read Image File')

f_open = open('i.JPG', 'rb')
# the for loop will read the file and print the hexa code of the image file


f_open1 = open('i2.JPG', 'wb')

for j in f_open:
    f_open1.write(j)
