import re
from pathlib import Path
import os

search = '(pesky|bird)' # the searched phrase

# make it so the script rips ~10 second before the subtitle and 10 seconds after
# implement overlaping chunks recognition
# use regex instead of hardcoding

path = os.getcwd() + '/../subs/' # subtitles location
file_names = []

for file in os.listdir(path):
    file_names.append(file)
file_names.sort()

data = []

for f in file_names:
    file = open(path + f)
    for i, line in enumerate(file):
        if re.search(search, line):
            data.append({'fname':f, 'beg':prev[0:8], 'end':prev[17:25], 'desc':line}) # get file name, time stamps and desciption
        prev = line # a line just before text is a timestamp

file_rip = open('rip.sh', 'w')
file_list = open('list.txt', 'w')
for (i, d) in enumerate(data):
      name = d['fname'][:2] # get a name without an extension
      outname ="../out/{}-{:0>2}.mp4".format(name, i)
      file_list.write("file '{}'\n".format(outname))
      file_rip .write('ffmpeg -ss {} -i ../original/{}.mp4 -to 00:00:12 -c copy {}\n'.format(d['beg'], name, outname))
