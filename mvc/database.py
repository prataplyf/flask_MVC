from mvc import module as ml

myclient = ml.pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient.company
user = mydb["employee"]