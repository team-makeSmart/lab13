# team MakeSmart
# lab13
# 

import os

def getArticle():
    article = "article.txt"
  
    # Get the programs working directory - see https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
    directory = os.path.dirname(os.path.abspath(__file__)) 
    
    # Make full path name
    path = directory + "\\" + article
    
    
    # Make sure the file exists - see https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-using-python
    if os.path.exists(path):
        file = open(path, "rt")
        return file.read()
    # Manually select file if not found
    else:
        print "File not found\nPlease select " + article
        file = open(pickAFile(), "rt")
        return file.read()

    

    
    