#!/usr/bin/env python

import os
from time import sleep
import beanstalkc

# Config
check_interval = int(os.getenv('CHECK_INTERVAL', 10))
check_path = os.getenv('CHECK_PATH', "media")

beanstalk_host = os.getenv('BEANSTALK_HOST', 'localhost')
beanstalk_port = int(os.getenv('BEANSTALK_PORT', 11300))


def add_job(job):
    beanstalk = beanstalkc.Connection(host=beanstalk_host, port=beanstalk_port)
    beanstalk.put(str(job))
    beanstalk.close()


def main():
    print("Checking: %s every %s seconds." % (check_path, check_interval))
    before = dict ([(f, None) for f in os.listdir (check_path)])
    while True:
        print("Checking...")
        after = dict([(f, None) for f in os.listdir (check_path)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added:
            print("Added: %s" % added)
            for f in added:
                add_job(f)
        before = after
        sleep(check_interval)


if __name__ == "__main__":
    main()
