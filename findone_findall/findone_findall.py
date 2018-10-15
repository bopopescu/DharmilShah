print('using findone and findall method')

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
x = mycol.find_one()
print(x)

for y in mycol.find():
    print(y)


print(' To return data of the particular column ')

for y in mycol.find({},{"_id" : 0, "name" : 1, "roll no": 1}):
    print(y)


for y1 in mycol.find({}, {"name" :1, "roll no": 1}):
    print(y1)

print('-------------------------------------------------------')
for y2 in mycol.find({}, {"roll no":1}):
    print(y2)




