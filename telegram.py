from typing import List, Union, Path, NamedTuple
from telethon.sync import TelegramClient 

CHANNELS = dict()

##TODO: Complete this code to initialize channels from their names 
def channels_init(channels: List[str]):
    pass

def upload_file_chunk(channel_name : str , caption : str , filepath : Path , start : int = 0 , end : int = 2000*1024*1024):
    global client , CHANNELS
    
    with open(filepath , 'rb') as handle:
        handle.seek(start)
        message = client.send_file(CHANNELS[channel_name], handle , force_document = True, file_size = end-start )
    
    return message 
    
def download_file_chunk(message ,  filepath : Path , start : int = 0 ):
    global client 
    
    with open(filepath , 'rb+') as handle:
        handle.seek(start)
        info = client.download_media(message, handle)
    
    return info 
    
def client_init(config : NamedTuple):
    
    ##Make sure the session file has been decrypted to use 
    global client 
    client = TelegramClient(config.sessionfile , config.api_id , config.api_hash )
    