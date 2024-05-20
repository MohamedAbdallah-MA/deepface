import os

class path :

def get_parent_path(path,levels=1):
    for _ in range(levels):
        path = os.path.dirname(path)
    return path

