#!/usr/bin/python

# add subtitles download support and conversion
# support different subtitles extensions
# support subs and vids renaming
# add debug file, I removed the old one because it wasnt working correctly

# check if you tell ffmpeg after the video is over - how does it handle it?
# if yes, add r_clamp(.). I would have to get the length of the videos

# handler error whene there are no fragments/ there's only one in function merge_overlap

import re
import os
import sys
from datetime import timedelta

# it's used to make sure that eg. 00:00:02 doesn't become 23:59:52
def left_clamps(t, delta):
    if t < delta:
        return timedelta()
    else:
        return t - delta

 # if two chunks overlap, they get merged
def merge_overlap(data):
    prev=data[-1] # probably there's a better way to start this loop
    for i, cur in enumerate(data):
        if prev['fname']==cur['fname'] and prev['end'] > cur['beg'] - sides: # that means we have to merge them
            cur['beg']=prev['beg']
            cur['desc']=prev['desc']+' | ' +cur['desc']
            data[i-1]={}
        prev = cur

# it collects data of clips which contain searched phrase
def generate_splice_data(file_names):
    data = []
    for i, f in enumerate(file_names):
        file = open(path + f)
        for i, line in enumerate(file):
            if i%4 == 2 and re.search(search, line): # we only need to check lines which contain text, hence the first condition
                data.append({
                'fname':f,                                                                                  #file name
                'beg':left_clamps(timedelta(minutes = int(prev[3  :5]), seconds=int(prev[6:  8])), sides),  #beginning timestamp
                'end':timedelta(minutes = int(prev[20:22]), seconds=int(prev[23:25])) + sides,              #ending timestamp
                'desc':line[:-1]})                                                                          #said lines
            if i%4 == 1:
                prev = line # a timestamp line
    return data


# it generates rip.sh - script which cut nessecsary part
# i dunno how to spell nessessery
def write_list_rip(data):
    file_list = open('list.txt', 'w')
    file_rip = open('rip.sh', 'w')
    file_rip.write('#!/bin/bash\n')
    for (i, d) in enumerate(data):
        if (d):
            name = d['fname'][:2] # get a name without an extension
            outname ="../out/{}-{:0>2}.mp4".format(name, i)

            file_list.write("file '{}'\n".format(outname))
            delta = d['end']-d['beg']

            if sys.argv[2] == 'slow':
                file_rip.write('ffmpeg -i ../original/{}.mp4 -ss 0{} -t 0{} -async 1 {}\n'.format(name, d['beg'], delta ,outname)) # slow but more accurate

            elif sys.argv[2] =='fast':
                true_beg = left_clamps(d['beg'], back)
                d1 = d['beg'] - true_beg # we have to do it his was just in case the clip is at the beginning
                file_rip.write('ffmpeg -ss 0{} -i ../original/{}.mp4 -ss 0{} -t 0{} -c copy {}\n'.format(true_beg, name, d1, delta, outname)) # fast but not accurate


def validate_arguments():
    if not len(sys.argv) == 3:
        print('Error: incorrect number of arguments.')
        sys.exit()
    if not sys.argv[2] in ['slow', 'fast']:
        print('Error: second argument can be only one of the following: slow, fast')
        sys.exit()

if __name__ == "__main__":
    validate_arguments()
    search = sys.argv[1] # the searched phrase
    sides = timedelta(seconds=10) # time we cut on both sides
    back  = timedelta(seconds=60) # how much do we want to go to get better keyframes. dunno how to explain this in two sentences
    path = os.getcwd() + '/../subs/' # subtitles location

    file_names = sorted(os.listdir(path))
    data = generate_splice_data(file_names)
    merge_overlap(data)
    write_list_rip(data)
