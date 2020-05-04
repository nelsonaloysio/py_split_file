py_split_file
---

Split a text file into smaller ones, optionally
repeating the file header throughout all files.

```
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
```