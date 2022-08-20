import os 
from .structures import File, Directory, Symlink 

def break_paths(path):
    
    path = os.path.normpath(path)
    path = path.replace(os.path.sep , '/')
    path = path.strip('/')    

    paths = [x for x in paths if x not in  ('' , '.')]
    return paths 
