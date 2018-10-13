print('Using Try and Except for Exception Handling')

val1 = int(input('enter the 1st value : '))
val2 = int(input('enter the 2nd value : '))

try:
    val3 = int(input('enter the value'))
except ValueError as e:
    print(e)


try:
    print(val1 / val2)

except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print('error : ', e)
finally:
    print('finally block executed')



