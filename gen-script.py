import re
import sys
from pathlib import Path
import os
import time
from datetime import datetime, timedelta
# jargon explanation: rip - 10-20 second part of a video
# # TODO:
# remove not used imports
# searched string is hardcoded. fix that
# make it so the script rips ~10 second before the subtitle and 10 seconds after
# implement overlaping chunks recognition
# use regex instead of hardcoding

path = os.getcwd() + '/../subs/' # subtitles location
file_names = []

for file in os.listdir(path):
    file_names.append(file)
file_names.sort() # not necessary, but it makes the generated script look better

data =[]

for f in file_names:
    file = open(path + f)
    for i, line in enumerate(file):
        if re.search('(pesky|bird)', line):
            data.append({'fname': f, 'beg': prev[0:8], 'end': prev[17:25], 'desc': line}) # get file name, time stamps and desciption
        prev = line

# datestring1 = data[-1][1]
# datestring2 = data[-1][2]
#
# #!!!! t1 = time.strptime(datestring1, "%M:%S")
# #!!!! t2 = time.strptime('00:12', '%M:%S')
# #!!!! start = time.mktime(t1)-time.mktime(t2)
# #!!!! print
#
# TODO I am using enumerato to make it so different rips from the same video
# have a different name and are in order. the order won't work if there is more
# than 9 rips from the same video
file_rip = open('rip.sh', 'w')
file_list = open('list.txt', 'w')
for (i, d) in enumerate(data):
      name = d['fname'][:2] # get a name without an extension, eg. 02.srt -> 02
      outname = '../out/' + name + '-' + str(i) + ".mp4" # name of a rip, eg ../out/02-4.mp4
      file_list.write("file '" + outname + "''\n") # TODO use {} or %s instead of +
      file_rip .write('ffmpeg -ss ' + d['beg'] + ' -i ../original/' + name + '.mp4 -to ' + '00:00:12' + ' -c copy ' +outname+'\n')
