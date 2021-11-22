# Generate diff

### Hexlet tests and linter status:
[![Actions Status](https://github.com/gabady13/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/gabady13/python-project-lvl2/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/e73048297c641deb3e5c/maintainability)](https://codeclimate.com/github/gabady13/python-project-lvl2/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/e73048297c641deb3e5c/test_coverage)](https://codeclimate.com/github/gabady13/python-project-lvl2/test_coverage)

[![Actions Status](https://github.com/gabady13/python-project-lvl2/workflows/Python%20CI/badge.svg)](https://github.com/gabady13/python-project-lvl2/actions)


Gendiff is a CLI utility for finding differences between configuration files.

## Features

- Suppported formats: YAML, JSON
- Report generation as plain text, structured text or JSON
- Can be used as CLI tool or external library

## Usage

### As external library

```python
from gendiff import generate_diff

diff = generate_diff(filepath1, filepath2)
```

### As CLI tool

```
> gendiff --help
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```


### step 4
[![asciicast](https://asciinema.org/a/3bX0cMTdWjLcncXAHVS2SVgEA.svg)](https://asciinema.org/a/3bX0cMTdWjLcncXAHVS2SVgEA)

### step 5
[![asciicast](https://asciinema.org/a/394589.svg)](https://asciinema.org/a/394589)

### step 6
[![asciicast](https://asciinema.org/a/HQzHmJntDMGza5XFOqWxFc2e5.svg)](https://asciinema.org/a/HQzHmJntDMGza5XFOqWxFc2e5)

### step 7
[![asciicast](https://asciinema.org/a/9r1w5pyubtarbxygibscGu1xw.svg)](https://asciinema.org/a/9r1w5pyubtarbxygibscGu1xw)

### step 8
[![asciicast](https://asciinema.org/a/SfYSdshYnSZ5K3y76qWkIx88s.svg)](https://asciinema.org/a/SfYSdshYnSZ5K3y76qWkIx88s)