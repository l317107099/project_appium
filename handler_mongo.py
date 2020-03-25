import pymongo
# from pymongo.collection import Collection


class Connect_mongo(object):
    def __init__(self):
        self.connect = pymongo.MongoClient(host="203.195.172.64", port=27017)
        self.client = self.connect['test2']


    def get_item(self):
        date = self.client['students'].find()
        return date
    def insert_item (self, item):
        self.collection = self.client[item['name']]
        self.collection.create_index([('id',pymongo.ASCENDING)])
        self.collection.update({'id':item.get('id')},
                               {'$addToSet':{
            'content':{'$each':item['']}
        }}, True)


if __name__ == '__main__':
    connect_mongodb = Connect_mongo()
    print(type(connect_mongodb.get_item()))
    data = connect_mongodb.get_item()
    for i in data:
        print(i['abc'])

