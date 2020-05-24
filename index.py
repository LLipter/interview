import os
import subprocess
import datetime
from operator import itemgetter

if __name__ == '__main__':
    
    data = {}
    for dirname in os.listdir("."):

        if not os.path.isdir(dirname):
            continue

        if dirname == '.git':
            continue

        filedata = []
        first_create_time = datetime.datetime.max
        for filename in os.listdir(dirname):
            link = os.path.join(dirname, filename)
            title = ''
            with open(link, 'r') as i_file:
                title = i_file.readline()[1:].strip()
                pipe = subprocess.Popen('git log {0}'.format(link.replace(' ', '\ ')), shell=True, stdout=subprocess.PIPE)
                pipe = pipe.stdout.readlines()
                create_date = datetime.datetime.strptime(pipe[-3][12:-7].decode(), '%b %d %H:%M:%S %Y')
                update_date = datetime.datetime.strptime(pipe[2][12:-7].decode(), '%b %d %H:%M:%S %Y')
                first_create_time = min(first_create_time, create_date)
            filedata.append((title, link, create_date, update_date))
        data[dirname] = (filedata, first_create_time)
    
    latest_files = []
    for i in [j[0] for j in data.values()]:
        latest_files.extend(i)
    latest_files.sort(key=itemgetter(2), reverse=True)

    with open("README.md", 'w') as o_file:
        o_file.write('# Latest Updates\n\n')
        for i in range(3):
            o_file.write(' - {2}  [{0}]({1}) \n'.format(latest_files[i][0], latest_files[i][1], latest_files[i][2]))
        o_file.write('\n')

        o_file.write('# Table of Contents\n\n')
        for dirname, (filedata, first_create_time) in sorted(data.items(), key=lambda item: item[1][1]):
            o_file.write('### {0}\n\n'.format(dirname))
            for title, link, create_date, update_date in sorted(filedata, key=itemgetter(2)):
                o_file.write(' - {2}  [{0}]({1}) \n'.format(title, link, create_date))
            o_file.write('\n')
