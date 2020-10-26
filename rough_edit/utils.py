import re
from datetime import timedelta
import os


def escape_string(string):
    # escapes chars like ' and &
    # strings I have to replace to make the * work
    for sign in [' ', "'", '"', '(', ')', '&']:
        string = string.replace(sign, '\\'+sign)
    return string


def str_to_timedelta(string):
    # TODO later: change findall to get rid of those [0]s
    time_regex_format = r"(\d{2}):(\d{2}):(\d{2})\.(\d{3})"
    results = re.findall(time_regex_format, string)
    hours, minutes, seconds, milliseconds = results[0]
    return timedelta(hours=int(hours),
                     minutes=int(minutes),
                     seconds=int(seconds),
                     milliseconds=int(milliseconds))


def generate_regex(prase):
    phrase_array = prase.split(" ")
    time_regex = r"(\d{2}:\d{2}:\d{2}.\d{3})"
    out_regex = ""

    for word in phrase_array:
        out_regex += f"<{time_regex}><c> ({word})</c>"
    out_regex += f"<{time_regex}>"

    print(out_regex)
    return out_regex
    # regex = f"<{timeRegex}><c> ({text})</c><{timeRegex}><c> ({text})</c><{timeRegex}>"
