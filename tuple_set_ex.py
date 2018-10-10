print('Using Tuple and set example')
print('Tuple are immutable means we cannot change the value')
print('tuple example')
print('')

tup = (10,30,20,40,20)
print('uses round bracket to print or perform anything with type')
print(tup)
print('')

#tup[1]=15
#are used for commenting
#print(tup)
print('this will give error because we cant change value as tuple are immuatble')
print('')

print(tup.count(20))
print('this will print a number occuring for sometimes')
print('')

print(tup.index(20))
print('print first occurences of the number specifiec in index')
print('')

print('set example which uses curly bracket')
print('set uses Hash concept so sorting dosent matter')
s={10,30,20,50,40}
print (s)
print (s)
print('')

a={10,30,20,50,20,40}
print('set also removed the repeated number while displaying even though we have while initializing')
print(a)

a.add(5)
print (a)

a.clear()
print(a)

b={1,4,5,6,2,4,3}
print(b)

c=b.copy()
print(c)

c=s.difference(b)
print(c)

z=b.union(s)
print(z)

z=b.intersection(s)
print(z)


