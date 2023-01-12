##
##  Imports
##

from F3TS_Functions import *

##
##  Vars / Setup
##

Set = ""

FileFunctions.CLS()

keyboard.press('f11')           #Maximizes Fullscreen

##
##  MainMenu
##

while True:
    print(Fore.GREEN + "FALLOUT 3 TERMINAL SIMULATOR\n")
    print("[1] Start Game")
    print("[2] Settings")
    print("[3] About")
    print("[4] Quit\n")

    Ans = input("Answer > ")

    if Ans == '1':
        F3TSGame.LoadTerminal()
        F3TSGame.StartNew()
        FileFunctions.CLS()
    
    while Ans == '2':
        FileFunctions.CLS()
        print(Fore.GREEN + "SETTINGS AVAILABLE\n")
        print(Fore.RED + "WARNING: THIS IS VERY FLIMSY, IF YOU INPUT SOMETHING WRONG THE\nGAME MAY BREAK, BE CAREFUL. IF ANYTHING BREAKS THAN CLOSE GAME\nAND REPLACE 'Settings.ini' contents with the SettingsFix.ini\n" + Fore.GREEN)
        print("[QTN] Close Settings         ")
        print("[NOA] Number of Attempts     (Must be Number)")
        print("[NOL] Number of Letters      (Must be Number from 4-6)")
        print("[SKI] Skip Intro             (0 = false : 1 = true)\n")

        SIn = input("Setting > ")
        
        if SIn == 'QTN':
            FileFunctions.CLS()
            break
        
        NIn = input("New Value > ")
            
        if SIn == 'NOA':
            Set = "NumberOfAttempts"
        elif SIn == 'NOL':
            Set = "NumberOfLetters"
        elif SIn == 'SKI':
            Set = "skipintro"
        
        SIn = str(SIn)
        NIn = str(NIn)
        
        F3TSGameEX.ChangeSetting(Set, NIn)

    if Ans == '3':
        print("This a game made using python and the console window. This game is meant to recreate Fallout3's terminal game, for more instructions view the\ngithub repository at https://github.com/thejoshbaker/Fallout3TerminalSimulator")

    if Ans == '4':
        exit()
        
    else:
        FileFunctions.CLS()
        print(Fore.RED, "INVALID INPUT\n", Fore.GREEN)



##
##  Game
##

