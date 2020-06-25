#!/usr/bin/python
import re
import os
from datetime import timedelta

search = '(pesky bird)' # the searched phrase
sides = timedelta(seconds=8) # time we cut on both sides

# TODO:
#reimplement overlapping
#now sides cant be bigger than 29, because of the way i hardcoded it somewhere
#TODO give an option to use longer version
# the fast version should be for testing only a
# implement fast better quality version. will have to use

# left clamps. used to make sure that 00:00:02 doesn't become 23:59:42
def l_clamps(t, delta):
    if t < delta:
        return timedelta()
    else:
        return t - delta


# make it better. i don't use this function for now
def merge_overlap(data): # if two chunks overlap, they get merged
    prev=data[-1] # it should work for now, but i should find a better solution
    #this also works, but for surely there's a better way to do this
    for cur in data:
        if prev['fname']==cur['fname'] and prev['end'] > cur['beg'] - sides: # that means we have to merge them
            cur['desc']+='@'
            prev['end']=cur['end']
        prev = cur


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
            data.append({
            'fname':f,
            'beg':l_clamps(timedelta(minutes = int(prev[3  :5]), seconds=int(prev[6:  8])), sides),
            'end':l_clamps(timedelta(minutes = int(prev[20:22]), seconds=int(prev[23:25])), sides),
            'desc':line[:-1]}) # get file name, time stamps and desciption
        if i%4 == 1:
            prev = line # a timestamp line


#merge_overlap(data)


file_list = open('list.txt', 'w')
file_rip = open('rip.sh', 'w')
file_rip.write('#!/bin/bash\n')
for (i, d) in enumerate(data):
      if d['desc'][-1]=='@':
          continue
      name = d['fname'][:2] # get a name without an extension
      outname ="../out/{}-{:0>2}.mp4".format(name, i)

      file_list.write("file '{}'\n".format(outname))
      print(d['end']-d['beg'])
      delta=d['end']-d['beg']+timedelta(seconds=6)
      file_rip .write('ffmpeg -ss {} -i ../original/{}.mp4 -to 0{} -c copy {}\n'.format(d['beg'], name, d['end']-d['beg']+timedelta(seconds=6),outname)) # fast but not accurate
      # file_rip .write('ffmpeg -i ../original/{}.mp4 -ss 0{} -t 0{} -async 1 {}\n'.format(name, d['beg'], delta ,outname)) # fast but not accurate

file_debug = open('debug.txt', 'w')
for d in data:
    file_debug.write('{}\t{}\t{}\t{}\n'.format(d['fname'][:2], d['beg'], d['end'], d['desc']))
