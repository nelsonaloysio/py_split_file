py_split_file
---

Split a text file into smaller ones using Python's default CSV library,
repeating the file header throughout all output files written.

```
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
```
