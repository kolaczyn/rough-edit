#!/usr/bin/python
import re
import os
from datetime import timedelta

search = '(pesky|bird)' # the searched phrase
sides = 6 # how much do we to both sides of a fragment
#now sides cant be bigger than 29, because of the way i hardcoded it somewhere

# to make sure that 00:00:02 doesn't become 23:59:42
def clamps(t):
    if (t<timedelta(seconds=sides)):
        return timedelta()
    else:
        return t

# if
# def merge_overlap(data): # if two chunks overlap, they get merged
#     for (i, d) in enumerate(data):
#         if(prev['fname']==d['fname']):
#             if
#         prev = d

# implement overlaping chunks recognition

path = os.getcwd() + '/../subs/' # subtitles location
file_names = []

for file in os.listdir(path):
    file_names.append(file)
file_names.sort()

data = []

for i, f in enumerate(file_names):
    file = open(path + f)
    for i, line in enumerate(file):
        if i%4 == 2 and re.search(search, line): # we only need to check lines which contain text, hence the first condition
            data.append({'fname':f, 'beg':prev[0:8], 'end':prev[17:25], 'desc':line}) # get file name, time stamps and desciption
        if i%4 == 1:
            prev = line # a timestamp line

file_list = open('list.txt', 'w')
file_rip = open('rip.sh', 'w')
file_rip.write('#!/bin/bash\n')
for (i, d) in enumerate(data):
      name = d['fname'][:2] # get a name without an extension
      outname ="../out/{}-{:0>2}.mp4".format(name, i)

      # refactor time thingy and get rid of hardcoding
      time_beg = '0' + str(clamps((timedelta(minutes=int(d['beg'][3:5]), seconds=int(d['beg'][6:8]))-timedelta(seconds=sides))))
      time_end = '0' + str(clamps((timedelta(minutes=int(d['end'][3:5]), seconds=int(d['end'][6:8]))+timedelta(seconds=sides))))
      file_list.write("file '{}'\n".format(outname))
      file_rip .write('ffmpeg -ss {} -i ../original/{}.mp4 -to 00:00:{} -c copy {}\n'.format(time_beg, name, sides*2,outname))
      # file_rip .write('ffmpeg -ss {} -i ../original/{}.mp4 -to 00:00:12 -c copy {}\n'.format(d['beg'], name, outname))



file_debug = open('debug.txt', 'w')
for d in data:
    file_debug.write('{}\t{}\t{}\t{}\n'.format(d['fname'][:2], d['beg'], d['end'], d['desc']))
