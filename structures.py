from typing import List, Union, Path


class File():
    
    def __init__(self , pk: int  , dir_pk : int , filepath : Path):
        
        self.filepath = filepath
        self.pk = pk 
        self.dir_pk = dir_pk 
        
class Directory():
    
    def __init__(self , pk : int , parent_pk: int , dirpath : Path ):
        
        self.dirpath = dirpath
        self.pk = pk
        self.parent_pk = parent_pk

class Symlink():
    
    def __init__(self, src : Union[File , Directory] , dest : Union[File , Directory]):
        
        self.src = src 
        self.dest = dest