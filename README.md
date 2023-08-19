### Hexlet tests and linter status:
[![Actions Status](https://github.com/minoko86/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/minoko86/python-project-50/actions)
[![Actions Status](https://github.com/minoko86/python-project-50/actions/workflows/code_climate_check.yml/badge.svg)](https://github.com/minoko86/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/4e2029c2c6047573d995/maintainability)](https://codeclimate.com/github/minoko86/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/4e2029c2c6047573d995/test_coverage)](https://codeclimate.com/github/minoko86/python-project-50/test_coverage)

### Description
**Gendiff (Difference generator)** - Performs comparison of documents in *.json, *.yml, *.yaml formats containing a dictionary of dictionaries. Finds differences in keys and their values and displays them in the specified format.
You can either use the python package or call it from the command line.

### Installation
```
git clone https://github.com/minoko86/python-project-50
cd python-project-50
make install
make build
make package-install
```

### Uninstallation
```
make package-remove
```

### Dependencies
* Python ^3.10
* poetry
* make

### Usage
```
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output (default: stylish).
                        Formats: {stylish, plain, json}.
```



### Examples


Use of help argument:

[![asciicast](https://asciinema.org/a/nWQATrNwIGmSzEVqVJMGgQUcQ.svg)](https://asciinema.org/a/nWQATrNwIGmSzEVqVJMGgQUcQ)

Comparison of 2 .json files:

[![asciicast](https://asciinema.org/a/ETboE5y9Zl7A2CnDd7WAFgTzH.svg)](https://asciinema.org/a/ETboE5y9Zl7A2CnDd7WAFgTzH)
 
Comparison of 2 .yml files:

[![asciicast](https://asciinema.org/a/6Is27QFhVCNbrctXFfadDfSv6.svg)](https://asciinema.org/a/6Is27QFhVCNbrctXFfadDfSv6)

Comparison of 2 complex .yml files:

[![asciicast](https://asciinema.org/a/8aG56hz4nnb0wzrYvGIlvkSiQ.svg)](https://asciinema.org/a/8aG56hz4nnb0wzrYvGIlvkSiQ)

Comparison of 2 complex .json files:

[![asciicast](https://asciinema.org/a/aNUgSAtY3Lzahz9M78pxz6S7V.svg)](https://asciinema.org/a/aNUgSAtY3Lzahz9M78pxz6S7V)

Comparison in "plain" format (2 complex .json files):

[![asciicast](https://asciinema.org/a/K2ZTVBUnkCc1E8jVhAHeOHN2x.svg)](https://asciinema.org/a/K2ZTVBUnkCc1E8jVhAHeOHN2x)

Comparison in "json" format (2 complex .yml files):

[![asciicast](https://asciinema.org/a/YeG1x8wXzcbG1bHqrngduBkPn.svg)](https://asciinema.org/a/YeG1x8wXzcbG1bHqrngduBkPn)