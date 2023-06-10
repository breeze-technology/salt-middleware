from flask import Flask

app = Flask(__name__)

@app.route("/api/v1")
def api_v1_test():
    return {
        'status' : 'Success!'
    }

import views.mongo