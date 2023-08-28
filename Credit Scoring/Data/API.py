# insert APIs to use here
#pip install rapidminer
import rapidminer

#connection to RapidMiner
def connector():
    connector = rapidminer.Studio("C:/Program Files/RapidMiner/RapidMiner Studio")
    return connector
   