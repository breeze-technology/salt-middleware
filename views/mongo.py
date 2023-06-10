from main import app
from models.mongo import MongoMiddleware

@app.route("/api/v1/salt/grains")
def grains():
    mongo = MongoMiddleware()

    return {
        'data' : mongo.grains()
    }

@app.route("/api/v1/salt/grains/<minion>")
def grains_by_minion(minion):
    mongo = MongoMiddleware()
    return {
        'data' : mongo.grains(minion=minion)
    }

@app.route("/api/v1/salt/minions")
def minions():
    mongo = MongoMiddleware()
    return {
        'data' : mongo.minions()
    }

@app.route("/api/v1/salt/minions/<minion>")
def minions_by_minion(minion):
    mongo = MongoMiddleware()
    return {
        'data' : mongo.minions(minion=minion)
    }

@app.route("/api/v1/salt/jobs")
def jobs():
    mongo = MongoMiddleware()
    return {
        'data' : mongo.jobs()
    }