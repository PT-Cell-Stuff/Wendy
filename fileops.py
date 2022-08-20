import os 

from . import concurrency 
import multiprocessing 

ENCRYPTION_STORE = None                     ##Injected Dictionary   :: key : object 
DB , DBCursor = None, None                  ##Injected Values       :: sqlite3.Connection , sqlite3.Cursor 
concurrency = None                          ##Injected Module

def file_upload(filepath , destpath , encryption_key  ):

    r = concurrency.add_fileupload.semaphore.manage(filepath , destpath , ENCRYPTION_STORE[encryption_key])
    t = await r.future().execute() 
    
    return t  
    
def file_download(filepath , destpath , encryption_key ):

    t = concurrency.add_filedownload.semaphore.manage(filepath , despath , ENCRYPTION_STORE[encryption_key])

def verify_proc():
    
    assert ENCRYPTION_STORE is not None 
    assert DB is not None 
    assert DBCursor is not None 
    assert concurrency is not None 

    