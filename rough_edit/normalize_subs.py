import os
import re


def check_conditions(line):
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


for file_name in os.listdir('../../subs'):
    print(file_name)
    with open(f'../../subs/{file_name}', 'r') as infile:
        with open(f'../../out-subs/{file_name}', 'w') as outfile:
            for line in infile:
                if check_conditions(line):
                    outfile.write(line)
                    # .replace('\n', ''))
