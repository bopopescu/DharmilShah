print ('Lambda Function')


val1 = int(input('enter value 1 :'))
val2 = int(input('enter value 2 :'))

add = lambda a ,b : a + b
sub = lambda a, b : a - b
mul = lambda a, b : a * b
div = lambda a, b : a / b
mod = lambda a, b : a % b
square = lambda a : a * a
cube = lambda a : a * a * a

result_add = add(val1, val2)
print(result_add)
result_sub = sub(val1, val2)
print(result_sub)
result_mul = mul(val1, val2)
print(result_mul)
result_div = div(val1, val2)
print(result_div)
result_mod = mod(val1, val2)
print(result_mod)
result_square = square(val1)
print(result_square)
result_cube = cube(val1)
print(result_cube)