#!/usr/bin/env python
# -*- coding: utf-8 -*-
import timeit
import argparse
import sys
import os
from os import path


def main():
    parser = argparse.ArgumentParser(description='Set arguments')
    parser.add_argument('target', help='target script_name')
    args = parser.parse_args()

    target = args.target
    repaet = -1
    origin_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')

    with open(target, 'r') as f:
        target_content = f.read()
        repeat = timeit.timeit(stmt=target_content, number=1000)

    sys.stdout = origin_stdout

    print(repeat)

if __name__ == '__main__':
    main()

