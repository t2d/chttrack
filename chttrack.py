#!/usr/bin/env python

import requests
import subprocess
import sys


def main(args):
    errors = ["Couldn't execute query!", "Couldn't connect to server!"]
    url = args[1]
    args[0] = 'httrack'  # override argument

    # fix url
    index = url.find('http')
    if index != 0:
        url = 'http://' + url

    r = requests.get(url)

    if r.status_code == 200:
        if not any(error in r.text for error in errors):
            subprocess.call(args)

if __name__ == "__main__":
    arguments = sys.argv
    main(arguments)
