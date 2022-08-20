import os 
from argparse import Namespace


PROG_PATH = os.path.dirname(os.path.abspath(__file__))
STORAGEPATH = os.path.join(PROG_PATH , 'storage-info.sqlite')

##Limits 
LIMITS = Namespace( 
                   downloads = 3 , 
                   uploads = 3 , 
                   encdec = 10 , 
                   cachesize = 10*1024*1024*1024,        ##10 GB
                   
                   )