import multiprocessing 
import logging 

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
    
