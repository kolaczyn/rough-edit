from rough_edit.utils import escape_string


def mpv_command(episode_num, beg, end):
    return f'  --\\` ../original/{episode_num}* --start={beg} --end={end} --\\~\\\n'.replace('`', '{').replace('~', '}')


def ffmpeg_command(episode_num, beg, end, count, outDir, base_name):
    padded_count = f'{count:06}'
    return f"""
# {base_name}
ffmpeg -i ../original/{episode_num}* -ss {beg} -t {end-beg} -async 1 "{outDir}{padded_count}{base_name}.mp4" -y
"""
