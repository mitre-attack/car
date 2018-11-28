"""This script generates redirects so the old car.mitre.org URLs go to the right place."""

import csv
from os import path, makedirs

basedir = path.join(path.dirname(__file__), "..", "docs")

with open('redirects.csv') as csvfile:
    redirects = list(csv.reader(csvfile))

for redirect in redirects:
    # Make the directory
    origpath = path.join(basedir, *redirect[0].split('/'))

    if 'http' in redirect[1]:
        targetpath = redirect[1]
    else:
        targetpath = "https://github.com/mitre-attack/car/blog/master{}".format(redirect[1])
    
    makedirs(origpath, exist_ok=True)

    redirect_txt = """<meta http-equiv="refresh" content="0; url={}"/>""".format(targetpath)

    open(path.join(origpath, "index.html"), "w").write(redirect_txt)