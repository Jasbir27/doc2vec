import pickle
import zlib
import os

def load(fileName,folderName,compression=False):
    fullFileName=os.path.join(folderName,fileName)
    if os.path.isfile(fullFileName):
        dbfile = open(fullFileName, 'rb')
        if compression==True:
            compressed=pickle.load(dbfile)
            obj = pickle.loads(zlib.decompress(compressed))
            dbfile.close()
            return obj
        else:
            db = pickle.load(dbfile)
            dbfile.close()
            return db  
        
    else:
        print("Error: This is not a valid file!!! : ",fullFileName)
        return None
        
        
def save(obj,fileName,folderName,compression=False):
    fullFileName=os.path.join(folderName,fileName)
    if compression==True:
        compressed = zlib.compress(pickle.dumps(obj))
        dbfile = open(fullFileName, 'wb')
        db = pickle.dump(compressed,dbfile) 
        dbfile.close()
        return db
    else:
        dbfile = open(fullFileName, 'wb')
        db = pickle.dump(obj,dbfile) 
        dbfile.close()
        return db

 
#loadPickleFile(fileName,folderName)
# obj=loadPickleFile("pkl_all_articles_text_2L","../../LargeFiles")
# obj={"name":"jasbir singh"}

# #savePickeFile(obj,"testPicklecompressed",folderName,compression=True)
# savePickeFile(obj,"pkl_all_articles_text_2L_comp","../../LargeFiles",compression=True)
#d=loadPickleFile("pkl_all_articles_text_2L_comp",folderName,compression=True)

# print(d)