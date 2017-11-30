# team MakeSmart
# lab13
# 

# used for getArticle(), may delete if we can't find a way to use getArticle()
import os

def madLibs():
    showInformation("Lets play some Mad Libs!")
    
    # Article is broken up into multiple lines because single quotes and double quotes within the article break things if its typed in as one string
    articleList = ['On the same day this week that the Spanish authorities stormed the offices of the Catalan regional government, detaining at least 14 people, a less-noticed raid took place.',
    'The puntCat foundation, which oversees the registry of websites with the ".cat" domain, tweeted Wednesday that its offices had also been raided and that one of its senior executives had been arrested.',
    'An arrest. Cats. The internet. Naturally, we were curious.',
    'Cats, of course, have a storied history on the internet. Cat videos were among the first clips to go viral on YouTube. BuzzFeed once told a reporter that cat posts generated 3.5 times more traffic than the average post.',
    'There flourished internet cats that wanted cheeseburgers, internet cats that were grumpy, internet cats that played keyboards, and an internet cat with an enviable life of the mind.',
    "In 2013, a cat food company, Friskies, promulgated a rumor that 15 percent of all internet traffic was cat-related. That this was even believable speaks to cats' status as rulers of the digital jungle.",
    'Almost all sites with the .cat suffix belong to the Catalan-speaking community thanks to the efforts of the puntCAT ("dot-cat" in Catalan),',
    "the foundation approved in 2005 to manage the domain's registry by the global Internet Corporation for Assigned Names and Numbers. That made it one of the first domains to explicitly refer to a language and culture, paving the way for others, when it first appeared in 2006.",
    "Catalan is spoken in Catalonia, the Spanish region that includes Barcelona and where political leaders have been pushing for years to secede from the rest of Spain. Madrid has declared that the secession effort violates the country's constitution, and have cracked down on attempts to hold a referendum on secession on Oct. 1.",
    'In a letter to ICANN, the foundation said that the Spanish authorities had asked it to "block all .cat domain names that may contain any kind of information about the forthcoming independence referendum."',
    '"We are being requested to censor content and suppress freedom of speech," the organization added.']
    # Article taken from https://www.nytimes.com/2017/09/22/style/cat-domain-catalonia.html
    
    # Rewrite the article into a single string
    article = ''
    for line in articleList:
        article += line + ' '
    
    # Get user input to replace words in the article
    replacementWords = dict()
    replacementWords['cat'] = getInput('Your first name').title()
    replacementWords['Cat'] = replacementWords['cat']
    replacementWords['CAT'] = replacementWords['cat'].upper()
    replacementWords['Barce'] = getInput('A fruit').title()
    replacementWords['Spanish'] = getInput('Genre of music').title()
    replacementWords['Spain'] = replacementWords['Spanish'] + "landia"
    replacementWords['keyboards'] = getInput('An instrument').lower()
    replacementWords['Friskies'] = getInput('Your favorite place to grab a bite to eat').title()
    replacementWords['cheeseburgers'] = getInput('favorite food (plural)').lower()
    replacementWords['Madrid'] = getInput('A politician').title()
    replacementWords['an enviable life of the mind'] = getInput('The coolest superpower').lower() + " superpowers"
    replacementWords['grumpy'] = getInput('A dangerous activity').lower()
    
    # Replace words in the article
    for key in replacementWords:
        article = article.replace(key, replacementWords[key])
        
    showInformation(article)
    
def getInput(prompt):
    """ Used to make sure that the user entered something in the prompt """
    
    word = ''
    while not word:
        word = requestString(prompt)
        if not word:
            showInformation("Input required")
    return word
          

"""  So I started building this function to read the text from an external file but can't for the life of me figure out how to correctly read in single quotes and double quotes.
  It would be a nice feature but I'm putting it on pause until the rest of the program requirements are complete. May end up deleting if we can't figure out how to fix """
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
