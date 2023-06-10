from pymongo import MongoClient
from utils.environments import Environments
from utils.date_utils import DateUtils
from datetime import datetime, timezone

class MongoMiddleware(object):
    
    def __init__(self):
        client = MongoClient(
            'salt-returner',
            username='root',
            password=Environments.SALT_RETURNER_PASSWORD)
        db = client['salt']
        self.salt_returns_collection = db['saltReturns']
        
        
    def grains(self, **kwargs):
        if len(kwargs) == 0:
            find_query = {'fun':'grains.items'}
        else:
            find_query = {
                'fun':'grains.items', 
                'minion' : kwargs['minion'] }
        collection = self.salt_returns_collection
        grains = {}
        for ret in collection.find(find_query):
            minion = ret['minion']
            if minion not in grains:
                grains[minion] = ret['full_ret']
            else:
                existent_jid = int(grains[minion]['jid'])
                new_jid = int(ret['jid'])
                if new_jid > existent_jid:
                    grains[minion] = ret['full_ret']
        return grains
    

    def minions(self, **kwargs):
        if len(kwargs) == 0:
            find_query = {'fun':'test.ping'}
        else:
            find_query = {
                'fun':'test.ping', 
                'minion' : kwargs['minion'] }
        collection = self.salt_returns_collection
        minions = {}
        date_utils = DateUtils()
        for ret in collection.find(find_query):
            minion = ret['minion']
            if minion not in minions:
                minions[minion] = ret['full_ret']
            else:
                existent_jid = int(minions[minion]['jid'])
                new_jid = int(ret['jid'])
                if new_jid > existent_jid:
                    minions[minion] = ret['full_ret']
        for minion in minions:
            _stamp = minions[minion]['_stamp']
            last_update = date_utils.compareTwoDates({
                'from' : _stamp,
                'until' : datetime.now()
            })
            minions[minion].update({
                'update_time_info' : last_update
            })
        return minions
    

    def jobs(self, **kwargs):
        
        skip = 0
        limit = 0
        collection = self.salt_returns_collection
        collection_count = collection.count_documents({})

        jobs = []

        for job in collection.find().skip(skip).limit(limit).sort('jid', -1):
            job.pop('_id')
            jobs.append(job)

        return {
            'count' : collection.count_documents({}),
            'documents' : jobs
        }
        
