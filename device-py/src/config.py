from re import sub

from board.fs import read, overwrite

def get(name):
    dict = {}

    for line in read('.config').split('\n'):
        pair = line.split('=')
        dict[pair[0]] = pair[1]

    return dict[name] if name in dict else None

def set(name, value):
    overwrite('.config', sub(f'{name}=[^\n]*', f'{name}={value}', read('.config')))
