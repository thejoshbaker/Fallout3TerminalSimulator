##
##  Imports
##

import os
import time
import configparser
import json
import re
import keyboard         # Used in 'F3TS.py'

from random import *
from colorama import *

##
##  File-Functions
##

class FileFunctions:
    def CLS():
        os.system('CLS')

    def TypeAnimation(str, speed): #Creates typing animation from real game
        for a in str:
            print(a, end="")
            time.sleep(speed)

            
##
##  F3TSGame-Class
##

class F3TSGame:
    
    def StartNew():

        ## Gathering Files

        Settings = configparser.ConfigParser()
        Settings.read('Settings.ini')
    
        Words   = json.load(open('F3TS_WordList.json', 'r'))

        AttAmnt = Settings.get('USER', 'numberofattempts')  #Attempt Ammount
        LetAmnt = Settings.get('USER', 'numberofletters')   #Letter  Ammount

        ## Setup

        print(Fore.GREEN, "") 

        FileFunctions.CLS()
        
        ## Game pt1

        print('ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL')
        print('ENTER PASSWORD NOW')

        print(AttAmnt, " ATTEMPT(S) LEFT: ")

        ## Game pt2
        
        i        = 0
        wordlist = []
        
        while i < 18:                                       ## This function selects 18 random words from the JSON databse and puts them in a list
            RanWord = randint(0, len(Words[LetAmnt])-1)
            SelWord = Words[LetAmnt][RanWord]
            if SelWord in wordlist:
                pass
            else:
                wordlist.append(SelWord)
                i = i + 1
                
        THEWORD = choice(wordlist)                          ## Chooses Word
        
        wordsused   = []
        LetAmnt     = int(LetAmnt)
        Lock        = True
        
        for h in Words["HEX"]:                              ## Prints mess of information
            print("\n", h, "  ", end="")
        
            RandChange = randint(9, 19 - LetAmnt)
            Right      = RandChange - LetAmnt - 4 
            MessAmnt   = randint(0, 20 - Right)
            RememberMA = MessAmnt
            
            while MessAmnt != 0:
                MessType    = randint(0, len(Words["RND"])-1)
                Mess        = Words["RND"][MessType]
                print(Mess, end="")
                MessAmnt = MessAmnt - 1
            
            Lock = True
            
            while Lock:
                if len(wordsused) != 18:
                    printword = choice(wordlist)
                    
                    if printword in wordsused:
                        pass
                    else:
                        wordsused.append(printword)
                        print(Fore.LIGHTGREEN_EX, printword, Fore.GREEN, end="")
                        
                        CharLeft = 20 - RememberMA - 4
                    
                        while CharLeft > 0:
                            MessType    = randint(0, len(Words["RND"])-1)
                            Mess        = Words["RND"][MessType]
                            print(Mess, end="")
                            CharLeft = CharLeft - 1
                            
                        Lock = False
                        
        print("\n")
            
        ## game pt3
        
        LetAmnt = int(LetAmnt)
        AttAmnt = int(AttAmnt)
        THEWORD = str(THEWORD)

        while True:
            
            user = input("Guess Word > ")
            print("", end="\n")
            
            Llist = [word.lower() for word in wordlist]
            Luser = user.lower()
            Lword = THEWORD.lower()
        
            if Luser in Llist:                              # Checks if word is apart of list                  
                pass
            else:    
                print(Fore.RED, "\nNot apart of list, try again\n", Fore.GREEN)
                
            AttAmnt = AttAmnt - 1    
            
            matches = 0
            for i in Luser:
                if re.search(i, Lword):
                    matches = matches + 1
            
            if (Luser == Lword):
                print(Luser)
                print("Exact match!")
                print("Please wait while system is accessed.")
                time.sleep(3)
                break
            
            print(Luser.upper())
            print("Entry denied  (", matches, "/", LetAmnt, ")")
            print(AttAmnt, " ATTEMPT(S) LEFT\n")
            
            if (AttAmnt == 0):
                FileFunctions.CLS()
                print('TERMINAL LOCKED')
                print('\nPLEASE CONTACT AN ADMINISTRATOR')
                time.sleep(5)
                break
            
                   
            

        
        
        
        
        
        
        
        
        
        
    def LoadTerminal():
        print(Fore.GREEN, "")   #Changes Text to Green
        
        Settings = configparser.ConfigParser()
        Settings.read('Settings.ini')
        
        Intro = Settings.get('USER', 'skipintro')

        Intro = int(Intro)

        if (Intro == 0):

            FileFunctions.CLS()

            FileFunctions.TypeAnimation('SECURITY RESET...\n\n', 0.01)
            FileFunctions.TypeAnimation('WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\n\n', 0.01)
            FileFunctions.TypeAnimation('>SET TERMINAL/INQUIRE\n\n', 0.05)
            FileFunctions.TypeAnimation('RIT-V300\n\n', 0.01)
            FileFunctions.TypeAnimation('>SET FILE/PROTECTION=OWNER:RWED ACCOUNTS.F\n', 0.05)
            FileFunctions.TypeAnimation('>SET HALT RESTART/MAINT\n\n', 0.05)

            FileFunctions.CLS()
            
        else:
            pass

##
##  Extensions-Class
##

class F3TSGameEX:
    
    def ChangeSetting(Set, NIn): 

        Settings = configparser.ConfigParser()
        Settings.read('Settings.ini')

        Settings.set('USER', Set, NIn)
        print(Fore.GREEN + "\nSetting Changed\n")
        
        with open('Settings.ini', 'w') as ConfigFile:
            Settings.write(ConfigFile)