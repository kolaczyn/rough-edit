#!/usr/bin/python

import re
import os
from datetime import timedelta

#TODO give an option to use longer version
# the fast version should be for testing only a
# implement fast better quality version. will have to use
# make it so the application dowloads subtitles and videos and names them correctly
#check if you tell ffmpeg after the video is over - how does it handle it?

# left clamps. used to make sure that eg. 00:00:02 doesn't become 23:59:52
def l_clamps(t, delta):
    if t < delta:
        return timedelta()
    else:
        return t - delta

 # if two chunks overlap, they get merged
def merge_overlap(data):
    prev=data[-1] # it should work for now, but i should find a better solution
    #this also works, but for surely there's a better way to do this
    for i, cur in enumerate(data):
        if prev['fname']==cur['fname'] and prev['end'] > cur['beg'] - sides: # that means we have to merge them
            cur['beg']=prev['beg']
            cur['desc']=prev['desc']+' | ' +cur['desc']
            data[i-1]={}
        prev = cur


def generate_splice_data(file_names):
    data = []
    for i, f in enumerate(file_names):
        file = open(path + f)
        for i, line in enumerate(file):
            if i%4 == 2 and re.search(search, line): # we only need to check lines which contain text, hence the first condition
                data.append({
                'fname':f,                                                                                  #file name
                'beg':l_clamps(timedelta(minutes = int(prev[3  :5]), seconds=int(prev[6:  8])), sides),     #beginning timestamp
                'end':timedelta(minutes = int(prev[20:22]), seconds=int(prev[23:25])),                      #ending timestamp
                'desc':line[:-1]})                                                                          #lines said
            if i%4 == 1:
                prev = line # a timestamp line
    return data


def write_list_rip(data):
    file_list = open('list.txt', 'w')
    file_rip = open('rip.sh', 'w')
    file_rip.write('#!/bin/bash\n')
    for (i, d) in enumerate(data):
        if (d):
            name = d['fname'][:2] # get a name without an extension
            outname ="../out/{}-{:0>2}.mp4".format(name, i)

            file_list.write("file '{}'\n".format(outname))
            delta=d['end']-d['beg']+timedelta(seconds=6)
            file_rip .write('ffmpeg -ss {} -i ../original/{}.mp4 -to 0{} -c copy {}\n'.format(d['beg'], name, d['end']-d['beg'],outname)) # fast but not accurate
            # file_rip .write('ffmpeg -i ../original/{}.mp4 -ss 0{} -t 0{} -async 1 {}\n'.format(name, d['beg'], delta ,outname)) # slow but more accurate


def write_debug_file(data):
    file_debug = open('debug.txt', 'w')
    for d in data:
        if d:
            file_debug.write('{}\t{}\t{}\t{}\n'.format(d['fname'][:2], d['beg'], d['end'], d['desc']))

if __name__ == "__main__":
    search = '(pesky bird)' # the searched phrase
    sides = timedelta(seconds=10) # time we cut on both sides
    path = os.getcwd() + '/../subs/' # subtitles location

    file_names = sorted(os.listdir(path))
    data = generate_splice_data(file_names)
    merge_overlap(data)
    write_list_rip(data)
    write_debug_file(data)
