import re
import os
from datetime import timedelta
import json

from roughEdit.utils import strToTimedelta, escapeString, generateRegex
from roughEdit.fileWriters import ffmpegCommand, mpvCommand


if __name__ == '__main__':
    baseDir = '../'
    subsDir = f"{baseDir}subs/"
    outDir = f"{baseDir}out/"

    phrase = "I don't know"
    regex = generateRegex(phrase)

    paddingLeft = timedelta(seconds=3)
    paddingRight = timedelta(seconds=3)
    count = 0

    with open('rip.sh', 'w') as ripFile:
        ripFile.write(f'rm {outDir}/*\nmpv\\\n')
        for filename in os.listdir(subsDir):
            subsFile = subsDir + filename
            with open(subsFile) as sample:
                results = re.findall(regex, sample.read())
                episodeNum = filename[:3]
                baseName = filename[3:-7]

                for result in results:
                    print(filename)
                    print(result)
                    beg = strToTimedelta(result[0]) - paddingLeft
                    end = strToTimedelta(result[-1]) + paddingRight
                    ripFile.write(ffmpegCommand(episodeNum, beg, end, count, outDir, baseName))
                    # ripFile.write(mpvCommand(episodeNumber, beg, end))
                    count += 1
        ripFile.write('\techo Finished')
