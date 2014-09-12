#!/usr/bin/env python

import requests
import subprocess
import sys


def main(args):
    errors = ['failed', 'error']
    url = args[1]
    args[0] = 'httrack'  # override argument

    r = requests.get(url)
    text = r.text.lower()

    if r.status_code == 200:
        if not any(error in text for error in errors):
            subprocess.call(args)

if __name__ == "__main__":
    arguments = sys.argv
    main(arguments)
