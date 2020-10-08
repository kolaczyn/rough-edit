import re
from datetime import timedelta
import os


def escapeString(string):
    # escapes chars like ' and &
    # strings I have to replace to make the * work
    for sign in [' ', "'", '"', '(', ')', '&']:
        string = string.replace(sign, '\\'+sign)
    return string


def strToTimedelta(string):
    # TODO later: change findall to get rid of those [0]s
    timeRegexFormat = r"(\d{2}):(\d{2}):(\d{2})\.(\d{3})"
    results = re.findall(timeRegexFormat, string)
    hours, minutes, seconds, milliseconds = results[0]
    return timedelta(hours=int(hours),
                     minutes=int(minutes),
                     seconds=int(seconds),
                     milliseconds=int(milliseconds))


def generateRegex(prase):
    praseArray = prase.split(" ")
    timeRegex = r"(\d{2}:\d{2}:\d{2}.\d{3})"
    outRegex = ""

    for word in praseArray:
        outRegex += f"<{timeRegex}><c> ({word})</c>"
    outRegex += f"<{timeRegex}>"

    print(outRegex)
    return outRegex
    # regex = f"<{timeRegex}><c> ({text})</c><{timeRegex}><c> ({text})</c><{timeRegex}>"
