from roughEdit.utils import escapeString


def mpvCommand(episodeNum, beg, end):
    return f'  --\\` ../original/{episodeNum}* --start={beg} --end={end} --\\~\\\n'.replace('`', '{').replace('~', '}')


def ffmpegCommand(episodeNum, beg, end, count, outDir, baseName):
    paddedCount = f'{count:06}'
    return f"""
# {baseName}
ffmpeg -i ../original/{episodeNum}* -ss {beg} -t {end-beg} -async 1 "{outDir}{paddedCount}{baseName}.mp4" -y
"""
