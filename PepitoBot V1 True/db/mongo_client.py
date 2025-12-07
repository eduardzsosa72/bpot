import pymongo
import datetime
import time
import threading
import requests

class MongoDB(object):
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client["bot"]
        self.user = self.db["user"]
        self.group = self.db["group"]
        self.key = self.db["keys"]


    def query_user(self, id:int=None):
        if id:return self.user.find_one({"id":id})
        else:return self.user.find()

    def query_group(self, id:int=None):
        if id:return self.group.find_one({"id":id})
        else:return self.group.find()

    def query_key(self, key=None):
        if key:return self.key.find_one({"key":key})
        else:return None

    def insert_user(self, data:dict):
        self.user.insert_one(data)
        return True
    
    def key_add(self,key,dias):
        self.key.insert_one({"key":key,"dias":dias})
        return True
    
    def update_user(self,idw,dia):

        tiempo_futuro = datetime.datetime.now() + datetime.timedelta(days=dia)
        times = tiempo_futuro.timestamp()
        
        self.user.update_one({"id": idw}, {"$set": {"plan": "premium"}})
        self.user.update_one({"id": idw}, {"$set": {"since": times}})
        self.user.update_one({"id": idw}, {"$set": {"antispam": 20}})

    def delete_user_p(self,idw,):
        self.user.update_one({"id": idw}, {"$set": {"plan": "free"}})
        self.user.update_one({"id": idw}, {"$set": {"since": None}})
        self.user.update_one({"id": idw}, {"$set": {"antispam": 40}})

    def add_antispam(self, id,ant):
        self.user.update_one({"id": id}, {"$set": {"antispam": ant}})

    def add_crdits(self, id,crdit):
        query = MongoDB().query_user(id)
        credits = query['credits'] + crdit
        self.user.update_one({"id": id}, {"$set": {"credits": credits}})
        
    def update_group(self,idw,dias):
        tiempo_futuro = datetime.datetime.now() + datetime.timedelta(days=dias)
        times = tiempo_futuro.timestamp()

        self.group.insert_one({"id":idw,"dias":times})
        
    def key_delete(self,key):

        self.key.delete_one({"key":key})
        return True
    
    def delete_chat(self,id):
        self.group.delete_one({"id":id})
        return True

    def ban(self,id):
        self.user.update_one({"id": id}, {"$set": {"role": 'baneado'}})

    def unban(self,id):
        self.user.update_one({"id": id}, {"$set": {"role": 'user'}})
    
    def add_role(self,id,role):
        self.user.update_one({"id": id}, {"$set": {"role": role}})
        
    def save_key(self,key,dias):
        data = {"key":key,"dias":dias}
        self.key.insert_one(data)
        return True
        
    def admin(self,id):
        query = MongoDB().query_user(id)
        if query['role'] == 'admin': return True
        if query['role'] == 'seller': return True
        elif query['role'] == 'owner': return True
        elif query['role'] == 'co-funders': return True
        else: return False

    def owner(self,id):
        query = MongoDB().query_user(id)
        if query['role'] == 'owner': return True
        elif query['role'] == 'co-funders': return True
        else: return False


def expulse_user():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["bot"]
    collection = db["user"]
    collection1 = db["group"]


    while True:

        for user in collection1.find({"dias": {"$lt": time.time()}}):
            MongoDB().delete_chat(user['id'])

            url = f'https://api.telegram.org/bot7881423666:AAHP7bFM_fANene68KSKNj_HRYg_BmKWQdA/sendMessage'
            params = {'chat_id': user['id'],'text': '<b>Se acabo tu acceso al grupo de usar nuestro bot.❗️</b>','parse_mode': 'HTML'}
            
            requests.post(url=url, params=params)

            url = f'https://api.telegram.org/bot7881423666:AAHP7bFM_fANene68KSKNj_HRYg_BmKWQdA/sendMessage'
            params = {'chat_id': -1002058267689,'text': f'<b>Se le acabo el acceso de dias al chat con id :( {user["id"]}  )❗️</b>','parse_mode': 'HTML'}
            
            requests.post(url=url, params=params)
    

        for user in collection.find({"since": {"$lt": time.time()}}):
            
            collection.update_one({"_id": user["_id"]},{"$set": {"plan": "free","antispam": 40,"key": None,"since": None}})
            collection1.delete_one({ "id": user['id'] })     
            
            url = f'https://api.telegram.org/bot7881423666:AAHP7bFM_fANene68KSKNj_HRYg_BmKWQdA/sendMessage'
            params = {'chat_id': user['id'],'text': '<b>Se acabo tu plan premium con nuestro bot.❗️</b>','parse_mode': 'HTML'}
            
            requests.post(url=url, params=params)

            url = f'https://api.telegram.org/bot7881423666:AAHP7bFM_fANene68KSKNj_HRYg_BmKWQdA/sendMessage'
            params = {'chat_id': -1002058267689,'text': f'<b>Se le acabo el plan premium al usuario( {user["id"]}  )❗️</b>','parse_mode': 'HTML'}
            
            requests.post(url=url, params=params)



        time.sleep(20)

thread2 = threading.Thread(target=expulse_user)
thread2.start()
