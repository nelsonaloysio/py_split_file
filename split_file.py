#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Split a text file into smaller ones, optionally
repeating the file header throughout all files.

usage: split_file [-h] [-o OUTPUT] [-l LINES] [-e ENCODING] [-H] input

positional arguments:
  input                 input file name

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output folder name
  -l LINES, --lines LINES
                        number of lines to split (default: 1000)
  -e ENCODING, --encoding ENCODING
                        file encoding (default: utf-8)
  -H, --header          repeat first line as header in all files
'''

from argparse import ArgumentParser
from os import mkdir
from os.path import basename, exists, splitext

ENCODING = 'utf-8'

LINES = 1000

def split_file(input_name, output_folder=None,
    number_of_lines=1000, encoding=ENCODING, header=True):
    '''
    Perform input file splitting.
    '''
    name, ext = splitext(basename(input_name))

    if not output_folder:
        output_folder = 'SPLIT_' + name

    if exists(output_folder):
        print('Error: "%s" already exists.' % output_folder)
        raise SystemExit

    mkdir(output_folder)

    int_lines = 0
    int_files = 0
    int_total = 0

    finished = False

    print('Splitting file...')

    with open(input_name, 'rt', encoding=encoding) as input_file:

        while True:
            int_lines = 0
            output_name = name + '_' + str(int_files+1) + ext

            while True:
                line = input_file.readline()

                if line == '':
                    finished = True
                    break

                if int_files == 0 and int_lines == 0:
                    file_header = line

                with open(output_folder + '/' + output_name, 'a', newline='', encoding=encoding) as output_file:
                    if int_lines == 0 and header:
                        output_file.write(file_header)
                        if int_files == 0:
                            line = input_file.readline()
                            int_total += 1
                    output_file.write(line)

                int_lines += 1

                if (int_lines >= number_of_lines):
                    break

            if int_lines > 0:
                print(output_name + '...', end='\r')
                int_total += int_lines
                int_files += 1

            if finished:
                break

    print('Read', str(int_total), 'total lines.\n'+\
          str(int_files), 'files after splitting.')

if __name__ == "__main__":

    parser = ArgumentParser()

    parser.add_argument('input', action='store', help='input file name')
    parser.add_argument('-o', '--output', action='store', help='output folder name')
    parser.add_argument('-l', '--lines', action='store', type=int, default=LINES, help='number of lines to split (default: %s)' % LINES)
    parser.add_argument('-e', '--encoding', action='store', help='file encoding (default: %s)' % ENCODING)
    parser.add_argument('-H', '--header', action='store_true', help='repeat first line as header in all files')

    args = parser.parse_args()

    split_file(args.input,
               args.output,
               args.lines,
               args.encoding,
               args.header)