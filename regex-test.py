import re
import os
from datetime import timedelta
import json


def strToTimedelta(string):
    # TODO later: change findall to get rid of those [0]s
    timeRegexFormat = r"(\d{2}):(\d{2}):(\d{2})\.(\d{3})"
    results = re.findall(timeRegexFormat, string)
    # print(results[0])
    hours, minutes, seconds, milliseconds = results[0]
    return timedelta(hours=int(hours),
                     minutes=int(minutes),
                     seconds=int(seconds),
                     milliseconds=int(milliseconds))


# i could use yielding to avoid passing in count
def getFfmpegString(episodeNumber, beg, end, count):
    return f"""# {episodeNumber}
        ffmpeg -i '{audioStream}' -ss {beg} -t {delta} -async 1 out/audio{paddedCount}.mp3
        ffmpeg -i '{videoStream}' -ss {beg} -t {delta} -async 1 out/video{paddedCount}.mp4
        ffmpeg -i out/video{paddedCount}.mp4 -i out/audio{paddedCount}.mp3 -c copy out/{paddedCount}.mp4

    """


def getFfmpegStringSlow(baseName, beg, end, count, extension):
    return f"""
        # {baseName}
        ffmpeg -i "../original/{baseName}.{extension}" -ss {beg} -t {end-beg} -async 1 "out/{paddedCount}{baseName}.mp4" -y
    """


def getFfmpegStringFast(baseName, beg, end, count, extension):
    return f"""
        # {baseName}
        ffmpeg -i "../original/{baseName}.{extension}" -ss {beg} -t {end-beg} -c copy "out/{paddedCount}{baseName}.mp4" -y
    """


with open("streams.json") as jsonFile:
    streams = json.load(jsonFile)
# print(streams)

# text = "unclear"
# text = "yeah"
# timeRegexFormat = r"(\d{2}):(\d{2}):(\d{2})\.(\d{3})"
# regex = r"<(\d{2}:\d{2}:\d{2}.\d{3})><c> (" + \
#     text + r")</c><(\d{2}:\d{2}:\d{2}.\d{3})>"

# testing new formula
text = 'yeah'
timeRegex = r"(\d{2}:\d{2}:\d{2}.\d{3})"
noTimes = "{2,}"
# regex = f"<{timeRegex}><c> ({text})</c><{timeRegex}><c> ({text})</c><{timeRegex}><c> ({text})</c><{timeRegex}>"
regex = f"<{timeRegex}><c> ({text})</c><{timeRegex}>(?:<c> ({text})</c><{timeRegex}>){noTimes}"

# print(regex)
# # regex = regex * 2
# print(regex)

subsDir = r"subs/"
count = 0
paddingLeft = timedelta(milliseconds=-80)
paddingRight = timedelta(milliseconds=125)
with open('rip2.sh', 'w') as ripFile:
    for filename in os.listdir(subsDir):
        subFile = subsDir + filename
        with open(subFile) as sample:
            results = re.findall(regex, sample.read())
            # getting rid of file extension and the episode number
            baseName = filename[3:-7]
            noExtensionName = filename[:-7]
            episodeNumber = filename[:3]
            videoStream = streams[baseName]['video']
            audioStream = streams[baseName]['audio']
            if results:
                pass
                print(baseName)
                print(results)
            for result in results:
                paddedCount = f'{count:06}'
                print(result)
                beg = strToTimedelta(result[0]) - paddingLeft
                end = strToTimedelta(result[-1]) + paddingRight
                delta = end - beg
                # ripFile.write(f'#{baseName}\n')
                # ripFile.write(
                # f'ffmpeg -i "../original/{filename[:-7]}" -ss {beg} -t {delta} -async 1 out/{paddedCount}.mp4\n')
                ripFile.write(
                    getFfmpegStringSlow(noExtensionName, beg, end, count,
                                        'mkv'))
                ripFile.write(
                    getFfmpegStringSlow(noExtensionName, beg, end, count,
                                        'webm'))
                ripFile.write(
                    getFfmpegStringSlow(noExtensionName, beg, end, count,
                                        'mp4'))
                count += 1
