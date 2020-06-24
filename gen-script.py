import re
import sys
from pathlib import Path
import os
import time
from datetime import datetime, timedelta

# # TODO:
# remove not used imports
# searched string is hardcoded. fix that
# make it so the script rips ~10 second before the subtitle and 10 seconds after
# implement overlaping chunks recognition

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
# out_file = open('rip.sh', 'w')
# out_list = open('list.txt', 'w')
# for (i, t) in enumerate(data):
#     name = t[0][:2]
#     vid_fil = 'out/'+ name + '-' + str(i)+'.mp4'
#     out_list.write('file \'' + vid_fil + "'\n")
#     out_file.write('ffmpeg -ss ' + t[1] + ' -i ' + name + '.mp4 -to ' + '00:00:12' + ' -c copy out/' + name + '-' + str(i) + '.mp4\n'  )
#
# os.system('bash script.sh')
# #!!!!os.system('ffmpeg -f concat -safe 0 -i list.txt -c copy out.mp4')
