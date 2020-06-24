import re
import sys
import os
import time
from datetime import datetime, timedelta

file_names = []
directory = r'/home/pawel/Videos/grian-pesky/subs/'
for file_name in os.listdir(directory):
    file_names.append(file_name)

file_names.sort()

data =[]

for f in file_names:
    file = open(directory+f)
    for i, line in enumerate(file):
        if re.search('(pesky|bird)', line):
            data.append([f, prev[3:8], prev[20:25], line])
        prev=line

for (t) in (data):
    print(t)

print('-' * 10)

datestring1 = data[-1][1]
datestring2 = data[-1][2]

# t1 = time.strptime(datestring1, "%M:%S")
# t2 = time.strptime('00:12', '%M:%S')
# start = time.mktime(t1)-time.mktime(t2)
# print

out_file = open('script.sh', 'w')
out_list = open('list.txt', 'w')
for i,t in enumerate(data):
    name = t[0][:2]
    vid_fil = 'out/'+ name + '-' + str(i)+'.mp4'
    out_list.write('file \'/' + vid_fil + "'\n")
    out_file.write('ffmpeg -i ' + name + '.mp4 -ss 00:' + t[1] + ' -t 00:00:12 ' + ' -async 1 ' + vid_fil +'\n')
