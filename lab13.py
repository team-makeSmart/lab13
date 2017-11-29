# team MakeSmart
# lab13
# 

import os

def getArticle():
    article = "article.txt"
  
    # Get the programs working directory - see https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
    directory = os.path.dirname(os.path.abspath(__file__)) 
    
    path = directory + "\\" + article
    file = open(path, "rt")
    text = file.read()
    return text
    
    