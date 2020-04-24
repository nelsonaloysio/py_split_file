#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Split a text file into smaller ones using Python's default CSV library,
repeating the file header throughout all output files written.

usage: split_file.py [-h] [-o OUTPUT] [--delimiter DELIMITER]
                     [--lines LINES] [no-header] input

positional arguments:
  input                 input file name

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output folder name
  --delimiter DELIMITER
                        column field delimiter
  --lines LINES         number of lines to split (default: 1000)
  --no-header           do not consider first line as header

'''

from argparse import ArgumentParser
from csv import reader, writer
from os import mkdir
from os.path import basename, exists, splitext

import json

def split_file(input_name, output_folder=None,
    delimiter=None, number_of_lines=1000, header=True):
    '''
    Perform input file splitting.
    '''
    name, ext = splitext(basename(input_name))

    if ext == '.json':
        header = False
        delimiter = '\n'

    elif not delimiter:
        delimiter = get_file_delimiter(input_name)

    if not output_folder:
        output_folder = 'SPLIT_' + name

    if exists(output_folder):
        print('Error: "%s" already exists.' % output_folder)
        raise SystemExit

    mkdir(output_folder)

    int_lines = 0
    int_files = 0

    finished = False

    print('Splitting...')

    with open(input_name, 'rt', encoding='utf8', errors='ignore') as input_file:
        file_reader = reader(input_file, delimiter=delimiter)
        file_header = next(file_reader) if header else None

        while True:
            int_lines = 0
            int_files += 1
            output_name = name + '_' + str(int_files) + ext

            print(output_name + '...')

            with open(output_folder + '/' + output_name, 'w', newline='', encoding='utf8', errors='ignore') as output_file:
                file_writer = writer(output_file)
                file_writer.writerow(file_header) if header else None

                while True:

                    try: # write next line until finished
                        line = next(file_reader)

                        if ext == '.json':
                            json.dump(json.loads(line[0]), output_file)
                            output_file.write('\n')
                        else:
                            file_writer.writerow(line)

                        int_lines += 1

                    except StopIteration:
                        finished = True

                    if finished or (int_lines == number_of_lines):
                        break

            if finished:
                break

    int_lines_total = file_reader.line_num

    print('Read', str(int_lines_total), 'total lines.\n'+\
          str(int_files), 'files after splitting.')

def get_file_delimiter(input_name):
    '''
    Returns character delimiter from file.
    '''
    with open(input_name, 'rt', encoding='utf8') as input_file:
        file_reader = reader(input_file)
        header = str(next(file_reader))

    for i in ['|', '\\t', ';', ',']:
        if i in header: # \\t != \t
            print('Delimiter set as "' + i + '".')
            return i.replace('\\t', '\t')

    return '\n'

if __name__ == "__main__":

    parser = ArgumentParser()

    parser.add_argument('input', action='store', help='input file name')
    parser.add_argument('-o', '--output', action='store', help='output folder name')
    parser.add_argument('--delimiter', action='store', help='column field delimiter')
    parser.add_argument('--lines', action='store', type=int, default=1000, help='number of lines to split (default: 1000)')
    parser.add_argument('--no-header', action='store_false', dest='header', help='do not consider first line as header')

    args = parser.parse_args()

    split_file(args.input,
               args.output,
               args.delimiter,
               args.lines,
               args.header)