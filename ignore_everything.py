#!/usr/bin/env python3
import os
from sh import git

if __name__ == '__main__':
    for root, dirs, files in os.walk('.'):
        if os.path.basename(root) == 'moveit_setup_assistant':
            continue
        for f in files:
            if f == 'package.xml':
                ignore_path = os.path.join(root, 'CATKIN_IGNORE')
                with open(ignore_path, 'wt') as out_file:
                    out_file.write('\n')
                git('add', '-f', ignore_path)
