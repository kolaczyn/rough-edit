import re
import os
from datetime import timedelta
import json

from rough_edit.utils import str_to_timedelta, escape_string, generate_regex
from rough_edit.file_writers import ffmpeg_command, mpv_command


if __name__ == '__main__':
    baseDir = '../'
    subs_dir = f"{baseDir}subs/"
    outDir = f"{baseDir}out/"

    phrase = "I don't know"
    regex = generate_regex(phrase)

    padding_left = timedelta(seconds=3)
    padding_right = timedelta(seconds=3)
    count = 0

    with open('rip.sh', 'w') as rip_file:
        rip_file.write(f'rm {outDir}/*\nmpv\\\n')
        for filename in os.listdir(subs_dir):
            subs_file = subs_dir + filename
            with open(subs_file) as sample:
                results = re.findall(regex, sample.read())
                episode_num = filename[:3]
                base_name = filename[3:-7]

                for result in results:
                    print(filename)
                    print(result)
                    beg = str_to_timedelta(result[0]) - padding_left
                    end = str_to_timedelta(result[-1]) + padding_right
                    # rip_file.write(ffmpeg_command(episode_num, beg, end, count, outDir, base_name))
                    rip_file.write(mpv_command(episode_num, beg, end))
                    count += 1
        rip_file.write('\techo Finished')
