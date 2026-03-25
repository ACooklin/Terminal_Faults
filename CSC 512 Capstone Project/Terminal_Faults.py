import time #Used to space out messages
import sys #Used to quit the program (Currently only used for one bit)
import json #Used for save data
import os #Used for save data
from colorama import Fore, Back, Style, init #Gives me more text formatting
init(autoreset=True)  # Automatically resets style after every print


# Starting game data
GameData = {
    'Money': 100,
    'Inventory': [],
    'Karma': 0,
    'PlayerLocation': "Macrohard",
    'brute_force': 0,
    'rainbow_table': 0,
    'xss_attack': 0,
    #Setting info
    'TextSpeed': 1.7,
    #Game Progress
    'GameProgress': 0

}

def SaveGame(filename='SaveGame.json'):
    # Open the file in write mode ('w')
    with open(filename, 'w') as f:
        # Use json.dump to write the dictionary to the file
        json.dump(GameData, f, indent=4)
    print(f"Game saved to {filename}")

def LoadGame(filename='SaveGame.json'):
    global GameData
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            GameData = json.load(f)
        print(f"Game loaded from {filename}")
    else:
        print("No save file found. Starting new game.")
        time.sleep(0.65)
        SaveGame()

LoadGame()
#Setting variable shortcuts
Money = GameData['Money']
Inventory = GameData["Inventory"]
Karma = GameData['Inventory']
PlayerLocation = GameData["PlayerLocation"]
brute_force = GameData['brute_force']
rainbow_table = GameData['rainbow_table']
xss_attack = GameData['xss_attack']
#Setting info
TextSpeed = GameData['TextSpeed']
#Game Progress
GameProgress = GameData["GameProgress"]



#Title screen
print(" ███████████                                     ███                       ████            ███████████                      ████   █████           ")
print("▒█▒▒▒███▒▒▒█                                    ▒▒▒                       ▒▒███           ▒▒███▒▒▒▒▒▒█                     ▒▒███  ▒▒███            ")
print("▒   ▒███  ▒   ██████  ████████  █████████████    ███  ████████    ██████   ▒███            ▒███   █ ▒   ██████   █████ ████ ▒███  ███████    █████ ")
print("    ▒███     ███▒▒███▒▒███▒▒███▒▒███▒▒███▒▒███ ▒▒███ ▒▒███▒▒███  ▒▒▒▒▒███  ▒███            ▒███████    ▒▒▒▒▒███ ▒▒███ ▒███  ▒███ ▒▒▒███▒    ███▒▒  ")
print("    ▒███    ▒███████  ▒███ ▒▒▒  ▒███ ▒███ ▒███  ▒███  ▒███ ▒███   ███████  ▒███            ▒███▒▒▒█     ███████  ▒███ ▒███  ▒███   ▒███    ▒▒█████ ")
print("    ▒███    ▒███▒▒▒   ▒███      ▒███ ▒███ ▒███  ▒███  ▒███ ▒███  ███▒▒███  ▒███            ▒███  ▒     ███▒▒███  ▒███ ▒███  ▒███   ▒███ ███ ▒▒▒▒███")
print("    █████   ▒▒██████  █████     █████▒███ █████ █████ ████ █████▒▒████████ █████ █████████ █████      ▒▒████████ ▒▒████████ █████  ▒▒█████  ██████ ")
print("   ▒▒▒▒▒     ▒▒▒▒▒▒  ▒▒▒▒▒     ▒▒▒▒▒ ▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒        ▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒ ▒▒▒▒▒    ▒▒▒▒▒  ▒▒▒▒▒▒  ")
                                                                                                                                                   
                                                                                                                                                   
                                                                                                                                                   
print("Welcome to Terminal Faults! This game is designed to teach you the basics of how to hack, how hackers think, and how to protect yourself. ")
time.sleep(2.0 * TextSpeed)
print("NOTE: This game contains ASCII Art not, not all of which was made by me. Credit has been assigned in accordance with the Digital Millenium Copyright Act.")
time.sleep(2.0 * TextSpeed)
def ReadyOrNot():
    Entergame=input("Are you ready to play? \n >y \n >n \n")
    if Entergame == "n":
        print("Then come back later. ")
        time.sleep(1.5)
        quit()
    elif Entergame != "y":
        print("It's a yes or no question, just type the letter y!")
        ReadyOrNot()
ReadyOrNot()

# Introduction
if GameProgress == 0:
    print("It is a wonderful, sunny day here at MacroHard™ and you are a terrible employee.")
    time.sleep(2.0 * TextSpeed)
    print("After months of claiming your plans to 'circle back,' people have finally noticed that you never actually did any work.")
    time.sleep(2.0 * TextSpeed)
    print("Your boss calls you into his office. He begins to talk with you about value add, benchmarks, and timelines.")
    time.sleep(2.0)
    print("He quickly notices your eyes seeming to glaze over.")
    time.sleep(1.5 * TextSpeed)
    print("After a moment, he comes to a conclusion, and types something into his laptop.")
    time.sleep(3.0 * TextSpeed)
    print("He spins his laptop around, and you see a blank Visual Studio Code tab.")
    time.sleep(1.5)
    print('"Write a program to reverse a linked list, right now." ')
    time.sleep(3.0)
    print("You don't know how to do that. You've never known how to write any code.")
    time.sleep(2.0)
    print("Well, you managed to collect a paycheck for a couple months. Better than you expected, at least.")
    time.sleep(3.5)
    print("You excuse yourself to head to the bathroom, walking out of the office a little too fast.")
    time.sleep(3.5)
    print("You walk past the bathroom door, headed towards your desk, and thus, your stuff.")
    time.sleep(2.0)
    print("You grab your meager belongings; a laptop, some loose meeting notes, and some office supplies.")
    time.sleep(2.0 * TextSpeed)
    GameData['GameProgress']+= 1
    print("Saving...")
    time.sleep(0.8)
    SaveGame()
    print("After a quick trip outside, it's up to you where to go.")
    time.sleep(1.5)

#The game begins
PlayerLocation = input("Do you want to go straight home, or wander around? \n >home \n >wander \n")
if PlayerLocation == "home":
    print("           )" )
    print("         ( _   _._")
    print("          |_|-'_~_`-._")
    print("       _.-'-_~_-~_-~-_`-._")
    print("   _.-'_~-_~-_-~-_~_~-_~-_`-._")
    print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("    |  []  []   []   []  [] |")
    print("jgs |           __    ___   |")
    print("  ._|  []  []  | .|  [___]  |_._._._._._._._._._._._._._._._._.")
    print("  |=|________()|__|()_______|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
    print("^^^^^^^^^^^^^^^ === ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("                 ===")
    print("                  ===")
    print("                   ===")
    print("                    ===")
    print("")
    print("Home sweet home.")
    print("The thought of what those bastards at MacroHard did to you is angering you more and more. How could they fire you just like that? ")
    time.sleep(1 * TextSpeed)
    print("After you worked for them for how many months? This cannot stand. ")
    time.sleep(1.0 * TextSpeed)
    print("They think you’re incompetent, huh?")
    time.sleep(1 * TextSpeed)
    print("Well, how about you show them just how incompetent you are, then? ")
    time.sleep(1 * TextSpeed)
    print("When you hack them, they’ll be sorry! ")
    time.sleep(1 * TextSpeed)
    PlayerInput = input("What do you want to do? \n> computer \n" )
    print("                                               ..,.oooE777999V(;")
    print("                                  ...oooP779090(;''       ''''  I")
    print("                    ...ooB777979V;;''       .....=v}}=}=}=}}v==  5")
    print("               97?(;''     .........<<vvvv<vvvvvvvvvvvvvvv}}}}v} L")
    print("               ,   ..;;`;;;;;<;<<<<<<<<<<<<<v<vvvvvvvvvv}vv}}}}}. 1")
    print("               b (:::``;;;;;;;;;;;<;<;<<<<<<<<<<<<v<v<vvvvvvvv}v}, E")
    print("               `J ::.:.:.``;;;;;;;;;;;<;;;<<<<<<<<<<<<v<v<vvvvvvvx L")
    print("                L  :. :.:.:.:.``;;;;;;;;;;;;;;<;<<<<<<<<<<v<<v<vv<( T")
    print("                `> .    . .:.:.:.:.`:;``;;;;;;;;<;;;<;<<<<<<<<<<<v< >")
    print("                 b ;           . : .:.:.:.`;;;;;;;;;;;<;;<;<<<<<<<<, I")
    print("                 `,`               . : :.:.:.:.`.`;;;;;;;;;;;;<;<;<<. 5")
    print("                  b ;                    . : .:.:.:.`;;;;;;;;;;;<;<;<: E")
    print("                  `,<                         . . .:.:.:.``;;;;;;;;;;. I")
    print("                   b :                             . . :.:.:.:.:.:.;;;. 5")
    print("                   `>;                                  . .:..:.:.:.`.:  |")
    print("                    b :                                      . . :.:.:.x T")
    print("                    `,;                                          . . .::  E")
    print("                     b :                                               _  !4")
    print("                     `r :   f_s                              __.__,--,;'))))).")
    print("                      b :                         ___...--'; `))))))))' '' `>!9eOc")
    print("                      `r :              __,--:-;;;)))))))))))'' '' ' ' _. -'-'.`!9Eg.")
    print("                       L : . __.--_--:,)))))))))))'' ' '  _. ._.-'-'-'-'\-'\---\/\ ``Qu.")
    print("                       `,: !x;:)))))))) ')'' ' _ _._-.'\'\_\_-'\''-\'_'\-'\'\ -_\'-\-. 95n.")
    print("                        D` ))))'''  _ .___.-_:/-/\/-_\ /-_, /-,\ \-/_\/\,-\_/-\/-/--' ..v<]9o.")
    print("                      __b :<> -_\._/\,- ,_ -\ _/\-\ _-\ -_/-\,\/,-/\_/-_\'\--' .vvvvvvv}v}}x}]NEo.")
    print("                .ooPO%LOCu  `< `/\_ -:\/_/-/,\/,/-,/_,-/\ :_\:_-:__-'' ...vvvvvvvvvvvvxx}vx}}}}==No")
    print("              .oPO'       `y. `< ~-\ _\/\_,- \ , - ,___..--' .......>>vvvvvvvvx<xvvxx}=x===}~^^   I")
    print("        om3jR&57'          `Ey, `\ `!,\ \-/_/\_---''.......vv>>vvvvvvvvvv)v<xvx=}=<~~^~`       :_yd")
    print("    _.rq8'                    `L, `<_ `--'.......vv<<<<v<<<<x<vv<vvvvxxxx=>~~~`         iuuuaE'")
    print("  .@tTL'                        `y,  `< .-vvv<<<<<<<<<xxvx>vvvvv=>~~~~`         _uuua'''")
    print(".&P'                              `L,  `>>><<<<><>v<vvvvvx~`::`       ::_uuua'''")
    print("                                    `y,  `:F_P:<x>~>^` `        _uuug'")
    print("                                      `L,  ~~`          _uuua''")
    print("                                        `L,:    _uuua''")
    print("                                          `LaE'' ")
    time.sleep(1.5 * TextSpeed)
    print("Er… how do you hack exactly?")
    time.sleep(1.5 * TextSpeed)
    print("You’ve just realized, you have no idea where to start.")
    time.sleep(1 * TextSpeed)
    print("You quickly type in a “C”, and the computer autocompletes.")
    time.sleep(1.2 * TextSpeed)
    print(' “ChabGPT.com” stares at you, and you look at it, preparing to type something into the prompt screen to do the hacking for you. ')
    time.sleep(1.0 * TextSpeed)
    print("...")
    time.sleep(2.0 * TextSpeed)
    print("The same way as it's done all your work thus far.")
    time.sleep(2.0 * TextSpeed)
    print("Something stops you.")
    time.sleep(1 * TextSpeed)
    print("You're not sure what it is, but you're motivated now.")
    time.sleep(1.0 * TextSpeed)
    print("You want to do this one yourself. ")
    time.sleep(1.0 * TextSpeed)
    print("Invigorated by this realization, you instead Google \"How to Hack.\" ") 
    time.sleep(1.5 * TextSpeed)
    print("In the old days, you used to outsource your thinking to Readdit.")
    time.sleep(1.5 * TextSpeed)
    print("That seems good enough for now. Baby steps and all that.")

    print('You click the top result from Readdit, simply labeled “How do i Hack poeple.”')
    time.sleep(1.0 * TextSpeed)
    print("")
    print("")
    print("How do i Hack poeple")
    print("")
    print("Hello Every1, I Think I Was Recetnly Chaeted On By My Girlfrend, \nAnd I Want 2 Hack Her To Get Reveng, How Do i Do Taht? I Dont No Anything About Computers")
    time.sleep(1.0 * TextSpeed)
    input("You should go through the comments. \n >comments \n")
    print("\nu/PeaceAnd4giveness")
    print("You should have an honest conversation with your partner, and either break up with her or drop this train of thought. \nTrying to “hack her” won’t make either of you feel any better.")
    print("(35k upvotes) \n")
    time.sleep(1.0 * TextSpeed)
    input("View next comment? \n")
    print("\nu/SaintSanta")
    print("It’s almost December! This is the time for the spirit of Christmas, forgiveness, and togetherness to shine! \nDon’t try to hack your girlfriend, just decide whether or not that’s a relationship you want to be in. \nIf you can’t trust her, hacking her won’t make anything better anyway. \nPlus, it’s illegal!")
    print("(26k upvotes)")
    time.sleep(3.0 * TextSpeed)
    print("     u/ReplyGuy")
    print("     It’s March.")
    time.sleep(1.5) #Not affected by TextSpeed to ensure comedic timing
    print("     (55 downvotes) \n")
    time.sleep(0.5 * TextSpeed)
    input("Next post? \n")
    print("\nu/Doom&Gloomer")
    print("It’s useless, may as well give up now. \nModern technology and security are too good, nobody really hacks anything anymore.")
    print("(16 downvotes)")
    time.sleep(2.0 * TextSpeed)
    print("\n \n \n")
    print("All useless, but as you scroll you start to see some actually useful information. \n \n")
    time.sleep(1.5 * TextSpeed)
    print("u/ScriptBabysitter")
    print("It’s probably the absolute simplest option, but you can just put every single possible password until you eventually get it right. ")
    print("This is called a brute-force attack.")
    print("Just about anything made in the last 20+ years will lock you out after you get it wrong a few times, but you’d be surprised by how often it works. ")
    print("Nobody bothers to update their software.")
    print("200 upvotes")
    time.sleep(4 * TextSpeed)
    print(Style.BRIGHT + Back.YELLOW + "You have unlocked a new technique! Be wary though; brute force won't work everywhere. \n")
    time.sleep(1 * TextSpeed)
    input("\nView Next Post? \n")
    print("\nu/Educ8er")
    print("Obviously malicious hacking is illegal and all that, and I’m pretty sure the original post is one of u/fedditor ‘s honeypots anyway. \n However, for those of you interested in ethical hacking, I recommend you check out the W6Schools program on it! It’s pretty simple, (at least at first) but it teaches you things the right way anyway. ")
    print("(30k upvotes)")
    print(Style.BRIGHT + Fore.BLUE + "(You have unlocked www.W6Schools.com! This website will teach you ethical hacking, if you’re into that sort of thing. \nYou’ll need a job after you get revenge, anyway.)")
    time.sleep(1 * TextSpeed)
    input("\nView Next Post? \n")
    print("\u/1e4bdd63d0841c351ba0d1f3812e26fa")
    print("www.9Ub339H38-HJ8hg9hiHG.nz")
    print(Style.BRIGHT + Fore.RED + "(You have unlocked a mysterious url. Maybe they might know more about how to hack your company.)" )

elif PlayerLocation == "wander": 
    print("///\\          \  /::\\ \_\ \\_:/:\:\:/_____ //:\ \                 /\  /\  /\ ")
    print("//:/\\          \//\::\\ \ \ \\/:\:\:/_____ //:::\ \   ls          /  \/  \/+/ ")
    print("/:/:/\\_________/:\/:::\`----' \\:\:/_____ //o:/\:\ \_____________/\  /\  / / ")
    print(":/:/://________//\::/\::\_______\\:/_____ ///\_\ \:\/____________/  \/  \/+/\ ")
    print("/:/:///_/_/_/_/:\/::\ \:/__  __ /:/_____ ///\//\\/:/ _____  ____/\  /\  / /  \ ")
    print(":/:///_/_/_/_//\::/\:\///_/ /_//:/______/_/ :~\/::/ /____/ /___/  \/  \/+/\  / ")
    print("/:///_/_/_/_/:\/::\ \:/__  __ /:/____/\  / \\:\/:/ _____  ____/\  /\  / /  \/ ")
    print(":///_/_/_/_//\::/\:\///_/ /_//:/____/\:\____\\::/ /____/ /___/  \/  \/+/\  /\ ")
    print("///_/_/_/_/:\/::\ \:/__  __ /:/____/\:\/____/\\/____________/\  /\  / /  \/  \ ")
    print("//_/_/_/_//\::/\:\///_/ /_//::::::/\:\/____/  /----/----/--/  \/  \/+/\  /\  / ")
    print("/_/_/_/_/:\/::\ \:/__  __ /\:::::/\:\/____/ \/____/____/__/\  /\  / /  \/  \/_ ")
    print("_/_/_/_//\::/\:\///_/ /_//\:\::::\:\/____/ \_____________/  \/  \/+/\  /\  / ")
    print("/_/_/_/:\/::\ \:/__  __ /\:\:\::::\/____/   \ _ _ _ _ _ /\  /\  / /  \/  \/___ ")
    print("_/_/_//\::/\:\///_/ /_//\:\:\:\              \_________/  \/  \/+/\  /\  /   / ")
    print("/_/_/:\/::\ \:/__  __ /\:\:\:\:\______________\       /\  /\  / /  \/  \/___/_ ")
    print("_/_//\::/\:\///_/ /_//::\:\:\:\/______________/      /  \/  \/+/\  /\  /   / ")
    print("/_/:\/::\ \:/__  __ /::::\:\:\/______________/\     /\  /\  / /  \/  \/___/___ ")
    print("_//\::/\:\///_/ /_//:\::::\:\/______________/  \   /  \/  \/+/\  /\  /   /   / ")
    print("/:\/::\ \:/__  __ /:\:\::::\/______________/    \ /\  /\  / /  \/  \/___/___/ ")
    print("/\::/\:\///_/ /_//:\:\:\                         \  \/\\\/+/\  /\  /   /   /+/ ")
    print("\/::\ \:/__  __ /:\:\:\:\_________________________\ ///\\\/  \/  \/___/___/ /_ ")
    print("::/\:\///_/ /_//:\:\:\:\/_________________________////::\\\  /\  /   /   /+/ ")
    print("::\ \:/__  __ /:\:\:\:\/_________________________/:\/____\\\/  \/___/___/ /___ ")
    print("/\:\///_/ /_//:\:\:\:\/_________________________/:::\    /\/\  /   /   /+/   / ")
    print("\ \:/__  __ /:\:\:\:\/_________________________/:::::\  ///  \/___/___/ /___/_ ")
    print(":\///_/ /_//:\:\:\:\/_________________________/:\:::::\///\  /   /  __________ ")
    print("\:/__  __ /:\:\:\:\/_________________________/:::\:::::\/  \/___/__/\ ")
    print("///_/ /_//:\:\:\:\/_________________________/:\:::\:::::\  /   /  /::\ ")
    print("/__  __ /\::\:\:\/_________________________/_____::\:::::\/___/__/:/\:\ ")
    print("/_/ /_//::\::\:\/_____________________/\/_/_/_/_/\  \           /::\ \:\ ")
    print("_  __ /:\::\:8\/_____________________/\/\   /\_\\/\  \ 8       /:/\:\ \:\ ")
    print("/ /_//\     \|______________________//\\/\::\/__\\/\  \|______/::\ \:\ \:\ ")
    print(" __ /  \  \                        /:\/:\/\_______\/\        /:/\:\ \:\/::\ ")
    print("/_//    8      -8  --  --  --  -- //\::/\\/_/_/_/_/_/ --  --/::\ \:\ \::/\:\ ")
    print("_ /     |\  \   |________________/:\/::\///__/ /__//_______/:/\:\ \:\/::\ \:\ ")
    print("__________\     \               //\::/\:/___  ___ /       /::\ \:\ \::/\:\ \:\ ")
    print("::::::::::\\  \  \             /:\/::\///__/ /__//       /:/\:\ \:\/::\ \:\ \: ")
    time.sleep(0.8 * TextSpeed)
    print("You wander around the city for a while. ")
    time.sleep(0.3)