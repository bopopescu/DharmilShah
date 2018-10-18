import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["jbsl"]
print(myclient.list_database_names())

mycol = mydb["student"]
collist = mydb.list_collection_names()
print(collist)
if "student" in collist:
    print (" the collection exist ")

ins_data = {"name" : "dharmil", "mno" : 9408572992}
x = mycol.insert_one(ins_data)
print(x.inserted_id)

manydata = [
     { "_id": 1, "name " : "abc", "mno" : 123456, "class " : "8 sem"},
     { "_id": 2, "name " : "xyz", "mno" : 1456, "class " : "7 sem"},
     { "_id": 3, "name " : "c", "mno" : 2346, "class " : "6 sem"},
     { "_id": 4, "name " : "c", "mno" : 346, "class " : "5 sem"},

]
x1 = mycol.insert_many(manydata)
print(x1.inserted_ids)
print('-----------------------')
findone = mycol.find_one()
print(findone)

print('----------------------------')
for findall in mycol.find():
    print(findall)
print('----------------------------')
for specificcl in mycol.find({}, {"_id" : 0}):
    print(specificcl)













