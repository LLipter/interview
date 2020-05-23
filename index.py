import os
import subprocess
import datetime
from operator import itemgetter

if __name__ == '__main__':
    
    included_dir = []
    included_dir.append('java')
    included_dir.append('cpp')
    included_dir.append('db')

    data = {}

    for dirname in included_dir:
        filelist = os.listdir(dirname)
        filedata = []
        for filename in filelist:
            link = os.path.join(dirname, filename)
            title = ''
            with open(link, 'r') as i_file:
                title = i_file.readline()[1:].strip()
                pipe = subprocess.Popen('git log {0}'.format(link), shell=True, stdout=subprocess.PIPE)
                pipe = pipe.stdout.readlines()
                create_date = datetime.datetime.strptime(pipe[-3][12:-7].decode(), '%b %d %H:%M:%S %Y')
                update_date = datetime.datetime.strptime(pipe[2][12:-7].decode(), '%b %d %H:%M:%S %Y')
            filedata.append((title, link, create_date, update_date))
        data[dirname] = filedata

    with open("README.md", 'w') as o_file:
        o_file.write('# Table of Contents\n\n')
        for dirname in included_dir:
            o_file.write('### {0}\n\n'.format(dirname))
            for title, link, create_date, update_date in sorted(data[dirname], key=itemgetter(2)):
                o_file.write(' - {2}  [{0}]({1}) \n'.format(title, link, create_date.strftime("%Y-%m-%d")))
            o_file.write('\n')



