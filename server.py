import requests

from flask import Flask

import sentry_sdk
sentry_sdk.init(
    dsn="https://c65a02f670a844deac27c2b8373d8a45@o447951.ingest.sentry.io/4505160410333184",
    debug=True,
    release="0.0.0",
)

app = Flask(__name__)

@app.route('/<something>')
def hello_world(something):
    r = requests.get(f'http://localhost:5001/{something.upper()}')

    return {
        "given_by_you": f"{something}'",
        "returned_from_microservice": r.json(),
    }


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
    sentry_sdk.capture_message("server.py started")