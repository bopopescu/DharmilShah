print('using list')
print('list are mutable means we can modify the list data')
numb = [10,20,30,40,50,60,70]
print (numb)
print('')

print('printing list in ascedning order having started 0')
print(numb[0])
print(numb[0:2])
print(numb[0:8])
print(numb[0:5])
print(numb[0:])
print('')

print('printing list in decending order having started -1')
print(numb[-1])
print(numb[-3])
print('')

print(numb[-7:])
print(numb[-7:-3])
print('')

alphanum = [10,'xyz',10.5]
print(alphanum)
print('')

combine = [numb,alphanum]
print(combine)
print('')

numb.append(80)
print(numb)

alphanum.append('abc')
print(alphanum)

numb.insert(3,35)
print(numb)

numb.remove(35)
print(numb)

numb.pop(7)
print(numb)

numb.pop()
print(numb)
print('')

print('to delete multiple values at specific location')
del numb[3:5]
print(numb)

print('to del multiple value without specofying any locations')
del numb[2:]
print(numb)
print('')

print('to add multiple values')
numb.extend([30,40,50,60,70])
print(numb)
print('')

print('List using In-built function')
print(min(numb))
print(max(numb))
print(sum(numb))
n=[10,3,50,2,1]
print(sorted(n))
print('')

