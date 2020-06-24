import re
import sys
from pathlib import Path
import os
import time
from datetime import datetime, timedelta

file_names = []

path = os.getcwd() + '/../subs/' # location of subtitles

for file_name in os.listdir(path):
    file_names.append(file_name)

file_names.sort() # not necessary, but it makes generated files look better

data =[];

for f in file_names:
    file = open(path+f)
    for i, line in enumerate(file):
        if re.search('(pesky|bird)', line):
            data.append([f, prev[0:8], prev[17:25], line])
        prev=line

for d in data:
    print(d)
#
#
# datestring1 = data[-1][1]
# datestring2 = data[-1][2]
#
# #!!!! t1 = time.strptime(datestring1, "%M:%S")
# #!!!! t2 = time.strptime('00:12', '%M:%S')
# #!!!! start = time.mktime(t1)-time.mktime(t2)
# #!!!! print
#
# out_file = open('script.sh', 'w')
# out_list = open('list.txt', 'w')
# for i,t in enumerate(data):
#     name = t[0][:2]
#     vid_fil = 'out/'+ name + '-' + str(i)+'.mp4'
#     out_list.write('file \'' + vid_fil + "'\n")
#     out_file.write('ffmpeg -ss ' + t[1] + ' -i ' + name + '.mp4 -to ' + '00:00:12' + ' -c copy out/' + name + '-' + str(i) + '.mp4\n'  )
#
# os.system('bash script.sh')
# #!!!!os.system('ffmpeg -f concat -safe 0 -i list.txt -c copy out.mp4')
