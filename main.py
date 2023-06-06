import requests
import sys
import time

import sentry_sdk


SERVER_URL = "http://localhost:5000"
#SERVER_URL = "https://c9ecfbd01917.ngrok.app"


@sentry_sdk.monitor(monitor_slug='twp-cron-job') 
def some_cron_job():
    time.sleep(1)


def main(value):
    sentry_sdk.init(
        dsn="https://e0f002c997e841828595584ace084210@o447951.ingest.sentry.io/4505160406990848",
        debug=True,
        release="0.0.0",
    )

    sentry_sdk.capture_message("main.py started")

    some_cron_job()

    r = requests.get('%s/%s' % (SERVER_URL, value))

    print()
    print("OUTPUT of main.py:")
    print(r.json())
    print()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "some_default_value_asdf")
