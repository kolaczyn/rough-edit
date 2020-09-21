import re
import os
from datetime import timedelta
import json


def strToTimedelta(string, format):
    # TODO later: change findall to get rid of those [0]s
    results = re.findall(format, string)
    print(results[0])
    hours, minutes, seconds, milliseconds = results[0]
    return timedelta(hours=int(hours),
                     minutes=int(minutes),
                     seconds=int(seconds),
                     milliseconds=int(milliseconds))


with open("streams.json") as jsonFile:
    streams = json.load(jsonFile)
# print(streams)

# text = "unclear"
text = "whoops"
timeRegexFormat = r"(\d{2}):(\d{2}):(\d{2})\.(\d{3})"
regex = r"<(\d{2}:\d{2}:\d{2}.\d{3})><c> (" + \
    text + r")</c><(\d{2}:\d{2}:\d{2}.\d{3})>"

subsDir = r"subs/"
count = 0
padding = timedelta(milliseconds=500)
with open('rip.sh', 'w') as ripFile:
    for filename in os.listdir(subsDir):
        subFile = subsDir + filename
        with open(subFile) as sample:
            results = re.findall(regex, sample.read())
            # getting rid of file extension and the episode number
            baseName = filename[3:-7]
            episodeNumber = filename[:3]
            videoStream = streams[baseName]['video']
            audioStream = streams[baseName]['audio']
            if results:
                print(baseName)
            for result in results:
                paddedCount = f'{count:06}'
                print(result)
                beg = strToTimedelta(result[0], timeRegexFormat) - padding
                end = strToTimedelta(result[2], timeRegexFormat) + padding
                delta = end - beg
                ripFile.write(f'#{baseName}\n')
                # ripFile.write(
                # f'ffmpeg -i "../original/{filename[:-7]}" -ss {beg} -t {delta} -async 1 out/{paddedCount}.mp4\n')
                ripFile.write(
                    f"ffmpeg -i '{videoStream}' -ss {beg} -t {delta} -async 1 out/video{paddedCount}.mp4\n"
                )
                ripFile.write(
                    f"ffmpeg -i '{audioStream}' -ss {beg} -t {delta} -async 1 out/audio{paddedCount}.mp3\n"
                )
                ripFile.write(
                    f"ffmpeg -i out/video{paddedCount}.mp4 -i out/audio{paddedCount}.mp3 -c copy out/{paddedCount}.mp4\n"
                )
                count += 1
