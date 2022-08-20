import multiprocessing 
import logging 
import telethon.ext.futures ##Patched file 
from stex.tools import add_fileupload 
from stex.tools import add_filedownload 
from . import config as cfg 

add_fileupload.semaphore = multiprocessing.Semaphore(n = cfg.MAX_UPLOAD_LIMIT )
add_filedownload.semaphore = multiprocessing.Semaphore(n = cfg.MAX_DOWNLOAD_LIMIT )

logger = logging.getLogger('wendy.concurrency')
logger.setLevel(logging.DEBUG)

def set_logs(path , mode = logging.DEBUG ):

    global logger 
    logger.setLevel(mode)
    
    logger.addHandler(logging.FileHandler(path))
    return True 

def set_semaphores(config):
    
    global EncDec, Upload, Download
    
    EncDec = multiprocessing.Semaphore(config.encdec)
    Upload = multiprocessing.Semaphore(config.upload)
    Download = multiprocessing.Semaphore(config.download)

def file_download(*args):
    
    return telethon.ext.futures.future(add_filedownload.semaphore.manage(*args))    
    
def file_upload(*args):
    
    return telethon.ext.futures.future(add_fileupload.semaphore.manage(*args))