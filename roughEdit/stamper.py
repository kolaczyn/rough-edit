from datetime import timedelta


def stringToTimedelta(time):
    time = time.split(':')
    return timedelta(hours=int(time[0]), minutes=int(time[1]), seconds=int(time[2]))


def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [alist[i*length // wanted_parts: (i+1)*length // wanted_parts] for i in range(wanted_parts)]


with open('rip2.sh') as file:
    data = file.read().split('\n')[:-1]
    data = split_list(data, 153)
    out = []

    for d in data:
        print(d)
        d[1] = stringToTimedelta(d[1])
        d[2] = stringToTimedelta(d[2])

    cur = timedelta(seconds=0)
    with open('rip3.sh', 'w') as outfile:
        for d in data:
            outfile.write(str(cur))
            outfile.write(' ')
            outfile.write(d[0])
            outfile.write(' at ')
            outfile.write(str(d[1]))
            outfile.write('\n')
            cur += d[2]
