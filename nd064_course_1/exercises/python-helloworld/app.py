from flask import Flask
from flask import json
import logging
import inspect
from datetime import datetime
app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.debug(TimeAndFuncLog())
    return "Hello World!"

@app.route("/status")
def healthcheck():
    response = app.response_class(
        response=json.dumps({"results":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.debug(TimeAndFuncLog())
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({
            "status":"success",
            "code": 0,
            "data": {
                "UserCount":140,
                "UserCountActive":23
            }
            }),
        status=200,
        mimetype='application/json')
    app.logger.debug(TimeAndFuncLog())
    return response

def TimeAndFuncLog():
    now = datetime.now()
    
    who = inspect.stack()[1][3]
    message=f"{now} {who} endpoint was reached"
    return message

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', encoding="utf-8", level=logging.DEBUG)
    app.run(host='127.0.0.1')
