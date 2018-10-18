print('using Dictionary example')
print('')

di={'abc':'1','x':'2','jkl':'3'}
print (di)
print(di.keys())
print(di.values())
print('to print particaular value of key then use this ')
print(di['abc'])
print(di['jkl'])
print('')
print('')
print('to print more than 1 key value then use this ')
print((di['abc']),(di['jkl']))
print('')

print(di.get('abc'))
print('')

print('to print whole dictionary use this ')
print(di.items())
print('')

di2=(di.copy())
print('use of the copy function')
print(di2)
print('')

print('setting new value to key temporary ')
print(di.fromkeys('x','demo'))
print('')

print(di.values())


