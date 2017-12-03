# Lab 13
# Team MakeSmart
# Pavlos Papadonikolakis, Maco Doussias, Jake McGhee
#12-02-17

#Type madLibs() into console for PART1 of this lab
#Type main() into console for PART2 of this lab additions 


# -------------------------- Lab 13 - Part I  --------------------------

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
    while not word or word.isspace():
        word = requestString(prompt)
        if not word or word.isspace():
            showInformation("Invalid input")
    return word
          
# -------------------------- Lab 13 - Part II  --------------------------

# CAVE ESCAPE Game Description:
# An explorer has fallen down a hole in the ground and into a cave. In order to navigate through the cave,
# they have to use specific commands that lead to specific directions inside the cave. If the user is lost
# or confused, there is a map or a help description available.
# MAP OF CAVE
#  [startRoom]    -  [darkRoom]  -  [islandRoom]
#      |                 |
#  [skeletonRoom] -  [batRoom]
#
# Win Condition for Game:  Get the rope from the island room and use it to climb out of the cave
# Lose Condition for Game:  Do more than twenty room changes
# Secret room.  Use the matches, if you find them, to light up the dark room, reveals a new secret room

import time

def map():  # Serves as the additional feature required per classroom instruction
    """ Prints map of the cave """
    """ Map can only be read in rooms with sufficient lighting """
    #display the map, one room per second
    i = 0
    mapArray = ['[startRoom]',' - ', '[darkRoom]',  ' - ',  '[islandRoom]\n',
                '     |    ','\t    |\n','[skeletonRoom]',' - ','[batRoom]\n']
    #Below while loop will print the map slowly for effect       
    while i < 10:
      sys.stdout.write("\r%s" % mapArray[i])
      sys.stdout.flush()
      time.sleep(1)
      i += 1 
    showInformation('There are five rooms plus.... one secret room')            
    print ''    


def getHelp():
    """ Prints help instructions to the user, if the user enters the 'HELP' command """
    showInformation(welcomeMessage())


def welcomeMessage():
    """ displays a wellcome message that displays the rules of the game """
    return '*** WELLCOME TO THE CAVE ESCAPE GAME! ***\n' \
           '-- In each room you will be told which directions you can go\n-- You\'ll be' \
           'able to go UP, DOWN, LEFT or RIGHT by typing that direction\n' \
           '-- Type HELP to redisplay this introduction --\n' \
           '-- Type MAP for a cave map\n' \
           '-- Type EXIT to quit at any time\n'

def runRoom(description, roomSpecificCommands):
    """ Prints the details of each room and gets a command from the user, ensure it is an acceptable command for the program and returns command
        If the command is not a valid entry, displays error message and requests user to enter a valid command
        :param roomSpecificCommands (list) the specific commands for the given room
        :return command (string) the command typed by the user
    """

    acceptableCommands = ['EXIT', 'HELP', 'MAP'] + roomSpecificCommands
    allValidCommands = "COMMANDS: "

    for i in range(0, len(acceptableCommands)):  # This for loops puts all the acceptable commands into a single string
        allValidCommands += acceptableCommands[i] + ' '

    while True:
        command = requestString(description + '\n\n' +
            allValidCommands + '\nEnter Command:').upper()

        if command not in acceptableCommands:
            showInformation('ERROR! Not a valid entry!\nAcceptable Commands for this room are\n' + allValidCommands)
        else:
            return command


def startRoom(acceptableCommands):
    """ the first room
         :return userCommand (string) the command typed by the user
    """
    description = 'START ROOM!\nThis area is big and expansive.\n' \
                  'You can see daylight coming from where you fell.\nIf you have rope you can climb out!'
    userCommand = runRoom(description, acceptableCommands)#['RIGHT', 'DOWN']
    return userCommand


def darkRoom(acceptableCommands):
    """ one of the rooms
        :return userCommand (string) the command typed by the user
    """
    description = 'DARK ROOM!\nThe room is dark and you cannot see much\n' \
                  'It smells damp and you can hear critters in the nearby water.\n' \
                  'This room needs more light!'
    userCommand = runRoom(description, acceptableCommands)#['RIGHT', 'DOWN', 'LEFT']
    return userCommand

def secretRoom(acceptableCommands):
    """ one of the rooms
        :return userCommand (string) the command typed by the user
    """
    description = 'SECRET ROOM!\nWow this room is not on map.  There is a commodore 64 computer in this room!\n' \
                  'If you play the game War Games(WOPR) on this you might accidentally break into NORAD!\n' \
                  'Best to leave this secret room alone!'
    userCommand = runRoom(description, acceptableCommands)
    return userCommand  

def skeletonRoom(acceptableCommands):
    """ one of the rooms
        :return userCommand (string) the command typed by the user
    """
    description = 'SKELETON ROOM!\nStalagmites fill this cavern.\n' \
                  'You see skeletons of past victims that fell down the well.\nPoor souls!'
    userCommand = runRoom(description, acceptableCommands)#['UP', 'RIGHT']
    return userCommand


def batRoom(acceptableCommands):
    """ one of the rooms
        :return userCommand (string) the command typed by the user
    """
    description = 'BATROOM!\n The walls of the cavern are filled with thousands of hanging bats\n ' \
                  'It smells of bat guano... Yuck.\n'\
                  'Another explorer left their pack here with a bunch of matches!'
    userCommand = runRoom(description, acceptableCommands)#['LEFT', 'UP']
    return userCommand


def islandRoom(acceptableCommands):
    """ one of the rooms
        :return userCommand (string) the command typed by the user
    """
    description = 'ISLAND ROOM!\nThe room is surrounded by a large lake that looks pristine\n' \
                  'The water is blue and it refracts light on the cavern walls.\nThere is a lot of rope laying around!'
    userCommand = runRoom(description, acceptableCommands)#['LEFT']
    return userCommand
    
def getName():
    name = ''
    while not name or name.isspace():
        name = requestString("What is your name?")
        if not name or name.isspace():
            showInformation("Invalid input!")
    return name
  

def main():
    """main function, starts the game """

    showInformation('Lets Get Started!')
    name = getName()
    showInformation(welcomeMessage())
 
    
    
    x = 0  # represents an x cartestian coordinate
    y = 0  # represents a y cartestian coordinate
    
    #additional items and actions 
    rope = 'ROPE'
    matches = 'MATCHES'
    items = []
    darkRoomLit = false #changes to true if matches used in dark room
    secretRoomAccess = false #user can only gain access to secret room by lighting a match in the dark room
    roomChanges = 0 #If room changes exceeds maxRoomChanges, you lose the game
    maxRoomChanges = 20 #Lose condition if you exceed maxRoomChanges  
    currentRoom = ''
    # Get input from user by calling the room functions.  Input will be specific to each room
    while true:

        if x == 0 and y == 0:
          if rope not in items:
            userCommand = startRoom(['RIGHT', 'DOWN'])
          else:
            userCommand = startRoom(['RIGHT', 'DOWN', 'CLIMBOUT'])     
                   
        elif x == 0 and y == -1:
          userCommand = skeletonRoom(['UP', 'RIGHT'])
            
        elif x == 1 and y == 0:
         if secretRoomAccess == true:
           userCommand = darkRoom(['RIGHT', 'DOWN', 'LEFT', 'UP'])
         elif matches in items:
           userCommand = darkRoom(['RIGHT', 'DOWN', 'LEFT', 'STRIKEMATCH'])
         else:
           userCommand = darkRoom(['RIGHT', 'DOWN', 'LEFT'])
           
        elif x == 1 and y == 1:
          currentRoom = 'Secret Room'
          userCommand = secretRoom(['DOWN'])  
               
        elif x == 2 and y == 0:
          if rope not in items:    
            userCommand = islandRoom(['LEFT','GETROPE'])
          else:
            userCommand = islandRoom(['LEFT'])  
            
        elif x == 1 and y == -1:
          if matches in items:  
            userCommand = batRoom(['LEFT', 'UP'])
          else:
            userCommand = batRoom(['LEFT', 'UP', 'GETMATCHES'])

        # Process off of what user input or userCommand is
        if userCommand == 'HELP':
            getHelp()
        elif userCommand == 'EXIT':
            showInformation(name + ',\nEven though you are a quiter, thank you for playing!')
            return  # effectively exit the program
            
        elif userCommand == 'MAP':
            if x == 1 and y == 0:
                showInformation('You cannot read your map in the Dark Room... Too dark!')
            else:
                map()
             
        elif userCommand == 'GETMATCHES':
          showInformation('You have picked up several matches!')
          items.append(matches)
          
        elif userCommand == 'STRIKEMATCH':
          showInformation('After stirking the match, you see a secret room hidden in the shadows!'\
                                  'You can now enter the secret room!')
          secretRoomAccess = true #Now user can access secret room  
          
        elif userCommand == 'GETROPE':
          showInformation('You have picked up rope!\nYou can use rope to climb!')
          items.append(rope)
          
        elif userCommand == 'CLIMBOUT':
          showInformation('YOU WIN! You use the rope to climb out\n' + name + ' you have survived the game!')
          return #end of game, user has won   
                      
        elif userCommand == 'UP':
            y += 1
            roomChanges += 1 
        elif userCommand == 'DOWN':
            y -= 1
            roomChanges += 1
        elif userCommand == 'RIGHT':
            x += 1
            roomChanges += 1
        elif userCommand == 'LEFT':
            x -= 1
            roomChanges += 1
    
        #GAME OVER condition        
        if roomChanges > maxRoomChanges:
          showInformation('GAME OVER ' + name.upper() + '\nYOU HAVE DIED FROM OXYGEN DEPREVATION\nTOO MANY ROOM CHANGES SO YOU HAVE LOST THE GAME!')
          return #end of game         
