#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:"""
import sys
import re


def check_format(input_string):
    """ check correct format"""
    pattern = (
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
        r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] '
        r'"GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
    )
    match = re.match(pattern, input_string)
    if match:
        return True
    else:
        return False


status_list = [200, 301, 400, 401, 403, 404, 405, 500]
count = 0
status_dic = {}
file_size = 0
line = sys.stdin.readline()
while line != '':
    try:
        if not check_format(line):
            continue
        if count == 10:
            count = 0
            print(f'File size: {file_size}')
            for scode in status_list:
                if scode in status_dic:
                    print(f'{scode}: {status_dic[scode]}')
        splited_line = line.split()
        status_code = int(splited_line[-2])
        if status_code in status_list:
            if status_code in status_dic:
                status_dic[status_code] += 1
            else:
                status_dic[status_code] = 1
        count += 1
        file_size += int(splited_line[-1])
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        print(f'File size: {file_size}')
        for scode in status_list:
            if scode in status_dic:
                print(f'{scode}: {status_dic[scode]}')
