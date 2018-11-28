"""This script generates the README file from the list of analytics in the analytics directory"""

import glob
from os import path

def table_row(filename):
    txt = open(filename, "r").read()

    # Get the title from the first line
    title = txt.split('\n')[0].replace("# ", "")
    localfn = path.split(filename)[1]
    return ["[{}]({})".format(title, localfn)]

analytics = glob.glob(path.join(path.dirname(__file__), "..", "analytics", "CAR-*"))
rows = [["Analytic"], ["---"]] + [table_row(analytic) for analytic in analytics]
open(path.join(path.dirname(__file__), "..", "analytics", "README"), "w").write("|" + "\n|".join(["|".join(row) for row in rows]))

