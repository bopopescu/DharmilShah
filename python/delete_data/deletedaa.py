import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["jbsl"]
print(myclient.list_database_names())

mycol = mydb["sample"]
collist = mydb.list_collection_names()

print(collist)
if "sample" in collist:
    print("collection exist")


for result in mycol.find({}, {"_id" : 0}):
    print(result)
print('--------------delete----------')

myquery = {"address" : "rto"}
mycol.delete_one(myquery)
print('printing the data after deletion')
for result in mycol.find({}, {"_id" : 0}):
    print(result)

print('deleting more than 1 docs')
myquery2 = {"address": {"$regex":"^m"}}
x = mycol.delete_many(myquery)
print(x.deleted_count,'documments deleted')
print('----------------')


print(' delete all documents in the collection ' )
x = mycol.delete_many({})
print(x.deleted_count, "documents deleted")

for result in mycol.find({},{"_id":0}):
    print(result)

