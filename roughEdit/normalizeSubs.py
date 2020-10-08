import os
import re


def checkConditions(line):
    # tells if the line passes some regex comparasions
    conditions = [
        '^WEBVTT$',
        '^Kind: captions$',
        '^Language:.*$',
        '^.*align:start position:0%.*$',
        "^[a-zA-Z'\s\-\[\]]{3,}$"
    ]
    for condition in conditions:
        if re.match(condition, line):
            return False
    return True


for fileName in os.listdir('../../subs'):
    print(fileName)
    with open(f'../../subs/{fileName}', 'r') as infile:
        with open(f'../../out-subs/{fileName}', 'w') as outfile:
            for line in infile:
                if checkConditions(line):
                    outfile.write(line)
                    # .replace('\n', ''))
