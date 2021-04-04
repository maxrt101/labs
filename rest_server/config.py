'''
config.py - parse simple config files
Format: KEY=VALUE
Commenting is supported through prepending '#' at the line beginning
Important: spaces are NOT ignored, so if the row looks like 'key = value ',
           KEY will be 'key ' and VALUE - ' value '.

Functions:
  read
  write

'''

from typing import Dict


def read(filename: str) -> Dict[str, str]:
    config = {}
    with open(filename, 'r') as f:
        for line in f:
            if len(line) > 0 and line[0] != '#':
                tokens = line[:-1].split('=')
                config[tokens[0]] = tokens[1] if len(tokens) == 2 else None
    return config


def write(filaname: str, config: Dict[str, str]):
    with open(filename, 'w') as f:
        for key, value in config.items():
            f.write(f'{key}={value}')

