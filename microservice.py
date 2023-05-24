from flask import Flask

import sentry_sdk
sentry_sdk.init(
    dsn="https://5f9d5b81134849fb8fdcefc1b7922fd8@o447951.ingest.sentry.io/4505160413741056",
    debug=True,
    release="0.0.0",
)

app = Flask(__name__)

@app.route('/<something>')
def hello_world(something):
    return {
        "from_server": f"{something}'",
    }


if __name__ == '__main__':
    app.run(host="localhost", port=5001, debug=True)
    # sentry_sdk.capture_message("microservice.py started")    