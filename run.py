#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import subprocess
from os import path
import json
import sys


pyenv_path = "/root/.pyenv/versions"

def main():
    parser = argparse.ArgumentParser(description='Set arguments')
    parser.add_argument('target', help='target script_name')
    parser.add_argument('--dir')
    parser.add_argument('--ver', metavar='ver')

    args = parser.parse_args()
    vers = args.ver.split(',')
    dirname = args.dir
    target = args.target
    retval = {
                'status': 'success',
                'data': dict(),
            }

    for ver in vers:
        python_path = path.join(pyenv_path, ver, 'bin', 'python')
        command = python_path + ' ./worker.py '  + path.join(dirname, target)

        proc = subprocess.Popen(
                [command],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True)
        (out, err) = proc.communicate()
        if err != None:
            retval['status'] = 'fail'
            retval['reason'] = err.decode('utf-8')
            break
        out = out.decode('utf-8').strip()
        retval['data'][ver] = {
                    'time': float(out)
                }

    print(json.dumps(retval))

if __name__ == '__main__':
    main()
