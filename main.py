import time
import requests
import sentry_sdk


@sentry_sdk.monitor(monitor_slug='twp-cron-job') 
def some_cron_job():
    time.sleep(1)


def main():
    sentry_sdk.init(
        dsn="https://e0f002c997e841828595584ace084210@o447951.ingest.sentry.io/4505160406990848",
        debug=True,
        release="0.0.0",
    )

    sentry_sdk.capture_message("main.py started")

    some_cron_job()

    r = requests.get('http://localhost:5000/asdf')
    print()
    print("OUTPUT of main.py:")
    print(r.json())
    print()


if __name__ == "__main__":
    main()
