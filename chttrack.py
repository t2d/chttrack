#!/usr/bin/env python

import requests
import subprocess
import sys


def main(args, read_stdin=False):
    if read_stdin:
        # read errors from stdin
        errors = list()
        for line in sys.stdin.readlines():
            l = line.strip()
            if l != "":
                errors.append(l)
    else:
        # use standard errors
        errors = ["Couldn't execute query!", "Couldn't connect to server!"]

    # read arguments
    url = args[1]
    args[0] = 'httrack'  # override argument

    # fix url
    index = url.find('http')
    if index != 0:
        url = 'http://' + url

    r = requests.get(url)

    # check site for errors
    if r.status_code == 200:
        if not any(error in r.text for error in errors):
            subprocess.call(args)

if __name__ == "__main__":
    # check arguments
    if len(sys.argv) < 2:
        print "usage: chttrack.py url {httrack_arguments} {--stdin}"
        print "       --stdin    read errors to filter for from stdin"
    elif "--stdin" in sys.argv:
        sys.argv.remove("--stdin")
        main(sys.argv, True)
    else:
        main(sys.argv)
