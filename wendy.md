Using Fusepy for Exposing the FileSystem:

```python
import logging

from collections import defaultdict
from errno import ENOENT
from stat import S_IFDIR, S_IFLNK, S_IFREG
from time import time

from fuse import FUSE, FuseOSError, Operations, LoggingMixIn 

#Maintain a python dictionary of all running filehandles and their corresponding paths 

class FileSytem(LoggingMixIn, Operations):

    def __init__(self, encrypted_credentials, password, **setup_kwargs ):
    
    	#Initialize Filesystem 
    	self.fd = 0 #Will be incremented every time a new file is created 

    def chmod(self, path, mode):
    	##Database Operation

    def chown(self, path, uid, gid):
        ##No user info on files, just returns None 
        return None 
        
    def create(self, path, mode):
        #Database Create with path  and mode 
        #Cache Create  with path and mode 
        #Return primary key as self.fd 
        return self.fd

    def getattr(self, path, fh=None):
		return default 
    
    def getxattr(self, path, name, position=0):
    	return default 
    	
    def listxattr(self, path):
          return [] 
          
    def mkdir(self, path, mode):
        #Pure database operation 
        
    def open(self, path, flags):
        
        #Database Operation to attach filehandle with cache file 
        return self.fd

    def read(self, path, size, offset, fh):
        return data in bytes 
        
        
    def readdir(self, path, fh):
        return ['.', '..'] + [x[1:] for x in self.files if x != '/']

    def readlink(self, path):
        #return self.data[path]
		return symlink_destination 

    def removexattr(self, path, name):
       	return ENOATTR #No attributes allowed in FS  
    
    def flush(self, path, fh):
        #return os.fsync(fh)
		#Return True only after the entire cache file is written 

    def fsync(self, path, datasync, fh):
        #Return True only after the entire cache file is written 
        
    def rename(self, old, new):
    	#Database Operation 

    def rmdir(self, path):
    
   		#Raise ENOTEMPTY if dir not empty 
        #Else, delete everything and return None 


    def setxattr(self, path, name, value, options, position=0):
        # Ignore options
    	return None 
   
    def statfs(self, path):
        return dict(f_bsize=512, f_blocks=4096, f_bavail=2048)
        #Otherwise FS may fail 

    def symlink(self, target, source):
        #Target existing file with symlink 
        
    def truncate(self, path, length, fh=None):
        #If size < fsize -> Truncate 
        #If size > fsize -> Fill with zero bytes 
     
        def release(self, path, fh):
        return os.close(fh)

	def release(self, path, fh):
        #Close filehandle 
        
    def destroy(self, path, fh):
    	##Like release, but operation read/write is technically pending 
        ##If being written --> good, just cancel and delete corresponding files 
        ##If being read --> return None and delete corresponding cache file and cancel running download if any 
        
    def unlink(self, path):
    	#Delete symlink 

    def utimens(self, path, times=None):
        
        #Set file modified and created time to times/now() 
        
    def write(self, path, data, offset, fh):
    	#Write binary data from offset for given filehandle 
		
    fuse = FUSE(
        FileSystem(config.root), config.mountpoint, foreground=True, 		allow_other=True, allow_thread = True)	
        #Will keep running in the foreground/background 
        #Multi-threaded but not multi-processed
        #So data integrity is preserved 
```


There's a dictionary running with file pk as primary keys and path of the file from root of the mount as the values. This helps to keep check of running files 

There's a config file with all sorts of configurations like `MAX_CONCURRENT_DOWNLOADS` and `TELETHON_CLIENT_ID`, `TELETHON_CLIENT_SECRET`, `ENCRYPTION_KEY` and `ENCRYPTION_PASSWORD` 



```python

class ReadStatus(Enum):
	DOWNLOAD_AND_CACHING
    DECRYPTING_CACHE_FILE
    CACHE_COMPLETE 

class WriteStatus(Enum):
	WRITING_TO_ENCRYPTED_CACHE
    CACHE_COMPLETE
    UPLOADING_FROM_CACHE

@dataclass     
class File:
	Operation : multiprocessing.Process
    path : str 
    cache_dec_path : str 
    cache_enc_path : str 
    current_op : status
    channel : int 
    pk : int 
    chunks : dict 
	
running_files = {pk : File(...) }
```

Semaphores: Every operation is capped out by a maximum Semaphore 

A redis database is used for cancelling operations 

```python
#Multiple callbacks can be created from here 
#Everytime a callback is done, it checks the value from Redis 
class Callback():

	def __init__(self, pk):
    	self.pk = pk 
       
    def telethon(current , total):
    	
        if Redis().get('cancels:pk'):
        	raise UserCancel() 
            
        #tqdm stuff 
        
def download(file : File):
	
    callback =  Callback() 
    
    with download_semaphore( timeout = -1 ) as s:
    	#multiprocessing.Process()
       	#telethon download with callback.telethon 
	
    with decrypt_semaphore(timeout = -1) as s:
    	###

def upload(file : File):
	#We don't need a callback here, destroy only needs to delete the cache file 
    
    with encrypt_semaphore(timeout = -1) as s:
    	###Write 
        
   	#Delete decrtypted file 
    
    with upload_semaphore(timeout = -1) as s:
    	###Write 
```