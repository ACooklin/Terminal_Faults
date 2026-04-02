import time #Used to space out messages
import sys #Used to quit the program (Currently only used for one bit)
import json #Used for save data
import os #Used for save data
from colorama import Fore, Back, Style, init #Gives me more text formatting
init(autoreset=True)  # Automatically resets style after every print
import Missions

# ======================
# MISSION SYSTEM
# ======================

MissionsData = {
    "BitSec": [
        {
            "name": "Welcome to BitSec",
            "func": Missions.BitSecMission1,
            "requires": 0,
            "repeatable": False
        },
        {
            "name": "A New Friend",
            "func": Missions.BitSecMission2,
            "requires": 1,
            "repeatable": False
        },
        {
            "name": "Shiny Garbage",
            "func": Missions.BitSecMission3,
            "requires": 2,
            "repeatable": False
        },
        {
            "name": "XSS Webtest",
            "func": Missions.BitSecMission4,
            "requires": 3,
            "repeatable": False
        },
        {
            "name": "Operation Arachnicide",
            "func": Missions.BitSecMission5,
            "requires": 4,
            "repeatable": False
        }
    ]
}

def GetProgressKey(branch):
    return branch + "Progress"  # Matches your GameData

def ShowMissionMenu(branch):
    missions = MissionsData[branch]
    progress = GameData[GetProgressKey(branch)]

    print(f"\n=== {branch} Missions ===")

    for i, mission in enumerate(missions):
        if i < progress:
            status = "[COMPLETED]"
        elif i == progress:
            status = "[AVAILABLE]"
        else:
            status = "[LOCKED]"

        print(f"{i+1}. {mission['name']} {status}")

    print(r"0. Back")

    choice = input("> ")
    return choice

def RunMission(branch, mission_index):
    missions = MissionsData[branch]
    progress = GameData[GetProgressKey(branch)]

    if mission_index < 0 or mission_index >= len(missions):
        print(r"Invalid mission.")
        return

    if mission_index > progress:
        print(r"That mission is locked.")
        return

    mission = missions[mission_index]

    print(f"\n--- {mission['name']} ---\n")

    mission["func"]()

    if mission_index == progress:
        GameData[GetProgressKey(branch)] += 1
        SaveGame()

def MissionHub(branch):
    while True:
        choice = ShowMissionMenu(branch)

        if choice == "0":
            return

        if not choice.isdigit():
            print(r"Invalid input.")
            continue

        mission_index = int(choice) - 1
        RunMission(branch, mission_index)

def GameLoop():
    while True:
        print(r"\nWhat do you want to do?")
        print(r"1. BitSec Missions")
        print(r"2. Spider Dance Missions (Coming Soon)")
        print(r"3. SinKingShip Missions (Coming Soon)")
        print(r"4. Save Game")
        print(r"5. Quit")

        choice = input("> ")

        if choice == "1":
            MissionHub("BitSec")

        elif choice == "2":
            print(r"Spider Dance not implemented yet.")

        elif choice == "3":
            print(r"SinKingShip not implemented yet.")

        elif choice == "4":
            SaveGame()

        elif choice == "5":
            print(r"Goodbye.")
            SaveGame()
            sys.exit()

        else:
            print(r"Invalid input.")


# Starting game data
GameData = {
    'Inventory': [],
    'Karma': 0,
    'PlayerLocation': "Macrohard",
    'brute_force': 0,
    'rainbow_table': 0,
    'xss_attack': 0,
    #Setting info
    'TextSpeed': 1.7,
    #Game Progress
    'GameProgress': 0,
    #Game Branch Progress
    'BitSecProgress': 0,
    'SpiderDanceProgress':0,
    'SinKingShipProgress': 0

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
        print(r"No save file found. Starting new game.")
        time.sleep(0.65)
        SaveGame()


LoadGame()
#Setting variable shortcuts
Inventory = GameData["Inventory"]
PlayerLocation = GameData["PlayerLocation"]
brute_force = GameData['brute_force']
rainbow_table = GameData['rainbow_table']
xss_attack = GameData['xss_attack']
#Setting info
TextSpeed = GameData['TextSpeed']
#Game Progress
GameProgress = GameData["GameProgress"]



#Title screen
print(r" ███████████                                     ███                       ████            ███████████                      ████   █████           ")
print(r"▒█▒▒▒███▒▒▒█                                    ▒▒▒                       ▒▒███           ▒▒███▒▒▒▒▒▒█                     ▒▒███  ▒▒███            ")
print(r"▒   ▒███  ▒   ██████  ████████  █████████████    ███  ████████    ██████   ▒███            ▒███   █ ▒   ██████   █████ ████ ▒███  ███████    █████ ")
print(r"    ▒███     ███▒▒███▒▒███▒▒███▒▒███▒▒███▒▒███ ▒▒███ ▒▒███▒▒███  ▒▒▒▒▒███  ▒███            ▒███████    ▒▒▒▒▒███ ▒▒███ ▒███  ▒███ ▒▒▒███▒    ███▒▒  ")
print(r"    ▒███    ▒███████  ▒███ ▒▒▒  ▒███ ▒███ ▒███  ▒███  ▒███ ▒███   ███████  ▒███            ▒███▒▒▒█     ███████  ▒███ ▒███  ▒███   ▒███    ▒▒█████ ")
print(r"    ▒███    ▒███▒▒▒   ▒███      ▒███ ▒███ ▒███  ▒███  ▒███ ▒███  ███▒▒███  ▒███            ▒███  ▒     ███▒▒███  ▒███ ▒███  ▒███   ▒███ ███ ▒▒▒▒███")
print(r"    █████   ▒▒██████  █████     █████▒███ █████ █████ ████ █████▒▒████████ █████ █████████ █████      ▒▒████████ ▒▒████████ █████  ▒▒█████  ██████ ")
print(r"   ▒▒▒▒▒     ▒▒▒▒▒▒  ▒▒▒▒▒     ▒▒▒▒▒ ▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒        ▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒ ▒▒▒▒▒    ▒▒▒▒▒  ▒▒▒▒▒▒  ")
                                                                                                                                                   
                                                                                                                                                   
                                                                                                                                                   
print(r"Welcome to Terminal Faults! This game is designed to teach you the basics of how to hack, how hackers think, and how to protect yourself. ")
time.sleep(2.0 * TextSpeed)
print(r"NOTE: This game contains ASCII Art not, not all of which was made by me. Credit has been assigned in accordance with the Digital Millenium Copyright Act.")
time.sleep(2.0 * TextSpeed)
def ReadyOrNot():
    Entergame=input("Are you ready to play? \n >y \n >n \n")
    if Entergame == "n":
        print(r"Then come back later. ")
        time.sleep(1.5)
        quit()
    elif Entergame != "y":
        print(r"It's a yes or no question, just type the letter y!")
        ReadyOrNot()
ReadyOrNot()

# Introduction
if GameProgress == 0:
    print(r"It is a wonderful, sunny day here at MacroHard™ and you are a terrible employee.")
    time.sleep(2.0 * TextSpeed)
    print(r"After months of claiming your plans to 'circle back,' people have finally noticed that you never actually did any work.")
    time.sleep(2.0 * TextSpeed)
    print(r"Your boss calls you into his office. He begins to talk with you about value add, benchmarks, and timelines.")
    time.sleep(2.0)
    print(r"He quickly notices your eyes seeming to glaze over.")
    time.sleep(1.5 * TextSpeed)
    print(r"After a moment, he comes to a conclusion, and types something into his laptop.")
    time.sleep(3.0 * TextSpeed)
    print(r"He spins his laptop around, and you see a blank Visual Studio Code tab.")
    time.sleep(1.5)
    print('"Write a program to reverse a linked list, right now." ')
    time.sleep(3.0)
    print(r"You don't know how to do that. You've never known how to write any code.")
    time.sleep(2.0)
    print(r"Well, you managed to collect a paycheck for a couple months. Better than you expected, at least.")
    time.sleep(3.5)
    print(r"You excuse yourself to head to the bathroom, walking out of the office a little too fast.")
    time.sleep(3.5)
    print(r"You walk past the bathroom door, headed towards your desk, and thus, your stuff.")
    time.sleep(2.0)
    print(r"You grab your meager belongings; a laptop, some loose meeting notes, and some office supplies.")
    time.sleep(2.0 * TextSpeed)
    GameData['GameProgress']+= 1
    print(r"Saving...")
    time.sleep(0.8)
    SaveGame()
    print(r"After a quick trip outside, it's up to you where to go.")
    time.sleep(1.5)

#The game begins
PlayerLocation = input("Do you want to go straight home, or wander around? \n >home \n >wander \n")
if PlayerLocation == "home":
    print(r"           )" )
    print(r"         ( _   _._")
    print(r"          |_|-'_~_`-._")
    print(r"       _.-'-_~_-~_-~-_`-._")
    print(r"   _.-'_~-_~-_-~-_~_~-_~-_`-._")
    print(r"  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(r"    |  []  []   []   []  [] |")
    print(r"jgs |           __    ___   |")
    print(r"  ._|  []  []  | .|  [___]  |_._._._._._._._._._._._._._._._._.")
    print(r"  |=|________()|__|()_______|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
    print(r"^^^^^^^^^^^^^^^ === ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(r"                 ===")
    print(r"                  ===")
    print(r"                   ===")
    print(r"                    ===")
    print(r"")
    print(r"Home sweet home.")
    print(r"The thought of what those bastards at MacroHard did to you is angering you more and more. How could they fire you just like that? ")
    time.sleep(1 * TextSpeed)
    print(r"After you worked for them for how many months? This cannot stand. ")
    time.sleep(1.0 * TextSpeed)
    print(r"They think you're incompetent, huh?")
    time.sleep(1 * TextSpeed)
    print(r"Well, how about you show them just how incompetent you are, then? ")
    time.sleep(1 * TextSpeed)
    print(r"When you hack them, they'll be sorry! ")
    time.sleep(1 * TextSpeed)
    PlayerInput = input("What do you want to do? \n> computer \n" )
    print(r"                                               ..,.oooE777999V(;")
    print(r"                                  ...oooP779090(;''       ''''  I")
    print(r"                    ...ooB777979V;;''       .....=v}}=}=}=}}v==  5")
    print(r"               97?(;''     .........<<vvvv<vvvvvvvvvvvvvvv}}}}v} L")
    print(r"               ,   ..;;`;;;;;<;<<<<<<<<<<<<<v<vvvvvvvvvv}vv}}}}}. 1")
    print(r"               b (:::``;;;;;;;;;;;<;<;<<<<<<<<<<<<v<v<vvvvvvvv}v}, E")
    print(r"               `J ::.:.:.``;;;;;;;;;;;<;;;<<<<<<<<<<<<v<v<vvvvvvvx L")
    print(r"                L  :. :.:.:.:.``;;;;;;;;;;;;;;<;<<<<<<<<<<v<<v<vv<( T")
    print(r"                `> .    . .:.:.:.:.`:;``;;;;;;;;<;;;<;<<<<<<<<<<<v< >")
    print(r"                 b ;           . : .:.:.:.`;;;;;;;;;;;<;;<;<<<<<<<<, I")
    print(r"                 `,`               . : :.:.:.:.`.`;;;;;;;;;;;;<;<;<<. 5")
    print(r"                  b ;                    . : .:.:.:.`;;;;;;;;;;;<;<;<: E")
    print(r"                  `,<                         . . .:.:.:.``;;;;;;;;;;. I")
    print(r"                   b :                             . . :.:.:.:.:.:.;;;. 5")
    print(r"                   `>;                                  . .:..:.:.:.`.:  |")
    print(r"                    b :                                      . . :.:.:.x T")
    print(r"                    `,;                                          . . .::  E")
    print(r"                     b :                                               _  !4")
    print(r"                     `r :   f_s                              __.__,--,;'))))).")
    print(r"                      b :                         ___...--'; `))))))))' '' `>!9eOc")
    print(r"                      `r :              __,--:-;;;)))))))))))'' '' ' ' _. -'-'.`!9Eg.")
    print(r"                       L : . __.--_--:,)))))))))))'' ' '  _. ._.-'-'-'-'\-'\---\/\ ``Qu.")
    print(r"                       `,: !x;:)))))))) ')'' ' _ _._-.'\'\_\_-'\''-\'_'\-'\'\ -_\'-\-. 95n.")
    print(r"                        D` ))))'''  _ .___.-_:/-/\/-_\ /-_, /-,\ \-/_\/\,-\_/-\/-/--' ..v<]9o.")
    print(r"                      __b :<> -_\._/\,- ,_ -\ _/\-\ _-\ -_/-\,\/,-/\_/-_\'\--' .vvvvvvv}v}}x}]NEo.")
    print(r"                .ooPO%LOCu  `< `/\_ -:\/_/-/,\/,/-,/_,-/\ :_\:_-:__-'' ...vvvvvvvvvvvvxx}vx}}}}==No")
    print(r"              .oPO'       `y. `< ~-\ _\/\_,- \ , - ,___..--' .......>>vvvvvvvvx<xvvxx}=x===}~^^   I")
    print(r"        om3jR&57'          `Ey, `\ `!,\ \-/_/\_---''.......vv>>vvvvvvvvvv)v<xvx=}=<~~^~`       :_yd")
    print(r"    _.rq8'                    `L, `<_ `--'.......vv<<<<v<<<<x<vv<vvvvxxxx=>~~~`         iuuuaE'")
    print(r"  .@tTL'                        `y,  `< .-vvv<<<<<<<<<xxvx>vvvvv=>~~~~`         _uuua'''")
    print(r".&P'                              `L,  `>>><<<<><>v<vvvvvx~`::`       ::_uuua'''")
    print(r"                                    `y,  `:F_P:<x>~>^` `        _uuug'")
    print(r"                                      `L,  ~~`          _uuua''")
    print(r"                                        `L,:    _uuua''")
    print(r"                                          `LaE'' ")
    time.sleep(1.5 * TextSpeed)
    print(r"Er… how do you hack exactly?")
    time.sleep(1.5 * TextSpeed)
    print(r"You've just realized, you have no idea where to start.")
    time.sleep(1 * TextSpeed)
    print(r"You quickly type in a “C”, and the computer autocompletes.")
    time.sleep(1.2 * TextSpeed)
    print(' “ChabGPT.com” stares at you, and you look at it, preparing to type something into the prompt screen to do the hacking for you. ')
    time.sleep(1.0 * TextSpeed)
    print(r"...")
    time.sleep(2.0 * TextSpeed)
    print(r"The same way as it's done all your work thus far.")
    time.sleep(2.0 * TextSpeed)
    print(r"Something stops you.")
    time.sleep(1 * TextSpeed)
    print(r"You're not sure what it is, but you're motivated now.")
    time.sleep(1.0 * TextSpeed)
    print(r"You want to do this one yourself. ")
    time.sleep(1.0 * TextSpeed)
    print(r"Invigorated by this realization, you instead Google \"How to Hack.\" ") 
    time.sleep(1.5 * TextSpeed)
    print(r"In the old days, you used to outsource your thinking to Readdit.")
    time.sleep(1.5 * TextSpeed)
    print(r"That seems good enough for now. Baby steps and all that.")

    print('You click the top result from Readdit, simply labeled “How do i Hack poeple.”')
    time.sleep(1.0 * TextSpeed)
    print(r"")
    print(r"")
    print(r"How do i Hack poeple")
    print(r"")
    print(r"Hello Every1, I Think I Was Recetnly Chaeted On By My Girlfrend, \nAnd I Want 2 Hack Her To Get Reveng, How Do i Do Taht? I Dont No Anything About Computers")
    time.sleep(1.0 * TextSpeed)
    input("You should go through the comments. \n >comments \n")
    print(r"\nu/PeaceAnd4giveness")
    print(r"You should have an honest conversation with your partner, and either break up with her or drop this train of thought. \nTrying to “hack her” won't make either of you feel any better.")
    print(r"(35k upvotes) \n")
    time.sleep(1.0 * TextSpeed)
    input("View next comment? \n")
    print(r"\nu/SaintSanta")
    print(r"It's almost December! This is the time for the spirit of Christmas, forgiveness, and togetherness to shine! \nDon't try to hack your girlfriend, just decide whether or not that's a relationship you want to be in. \nIf you can't trust her, hacking her won't make anything better anyway. \nPlus, it's illegal!")
    print(r"(26k upvotes)")
    time.sleep(3.0 * TextSpeed)
    print(r"     u/ReplyGuy")
    print(r"     It's March.")
    time.sleep(1.5) #Not affected by TextSpeed to ensure comedic timing
    print(r"     (55 downvotes) \n")
    time.sleep(0.5 * TextSpeed)
    input("Next post? \n")
    print(r"\nu/Doom&Gloomer")
    print(r"It's useless, may as well give up now. \nModern technology and security are too good, nobody really hacks anything anymore.")
    print(r"(16 downvotes)")
    time.sleep(2.0 * TextSpeed)
    print(r"\n \n \n")
    print(r"All useless, but as you scroll you start to see some actually useful information. \n \n")
    time.sleep(1.5 * TextSpeed)
    print(r"u/ScriptBabysitter")
    print(r"It's probably the absolute simplest option, but you can just put every single possible password until you eventually get it right. ")
    print(r"This is called a brute-force attack.")
    print(r"Just about anything made in the last 20+ years will lock you out after you get it wrong a few times, but you'd be surprised by how often it works. ")
    print(r"Nobody bothers to update their software.")
    print(r"200 upvotes")
    time.sleep(4 * TextSpeed)
    print(Style.BRIGHT + Back.YELLOW + "You have unlocked a new technique! Be wary though; brute force won't work everywhere. \n")
    time.sleep(1 * TextSpeed)
    input("\nView Next Post? \n")
    print(r"\nu/Educ8er")
    print(r"Obviously malicious hacking is illegal and all that, and I'm pretty sure the original post is one of u/fedditor ‘s honeypots anyway. \n However, for those of you interested in ethical hacking, I recommend you check out the W6Schools program on it! It's pretty simple, (at least at first) but it teaches you things the right way anyway. ")
    print(r"(30k upvotes)")
    print(Style.BRIGHT + Fore.BLUE + "(You have unlocked www.W6Schools.com! This website will teach you ethical hacking, if you're into that sort of thing. \nYou'll need a job after you get revenge, anyway.)")
    time.sleep(1 * TextSpeed)
    input("\nView Next Post? \n")
    print(r"\u/1e4bdd63d0841c351ba0d1f3812e26fa")
    print(r"www.9Ub339H38-HJ8hg9hiHG.nz")
    print(Style.BRIGHT + Fore.RED + "(You have unlocked a mysterious url. Maybe they might know more about how to hack your company.)" )
    

elif PlayerLocation == "wander": 
    print(r"///\\          \  /::\\ \_\ \\_:/:\:\:/_____ //:\ \                 /\  /\  /\ ")
    print(r"//:/\\          \//\::\\ \ \ \\/:\:\:/_____ //:::\ \   ls          /  \/  \/+/ ")
    print(r"/:/:/\\_________/:\/:::\`----' \\:\:/_____ //o:/\:\ \_____________/\  /\  / / ")
    print(r":/:/://________//\::/\::\_______\\:/_____ ///\_\ \:\/____________/  \/  \/+/\ ")
    print(r"/:/:///_/_/_/_/:\/::\ \:/__  __ /:/_____ ///\//\\/:/ _____  ____/\  /\  / /  \ ")
    print(r":/:///_/_/_/_//\::/\:\///_/ /_//:/______/_/ :~\/::/ /____/ /___/  \/  \/+/\  / ")
    print(r"/:///_/_/_/_/:\/::\ \:/__  __ /:/____/\  / \\:\/:/ _____  ____/\  /\  / /  \/ ")
    print(r":///_/_/_/_//\::/\:\///_/ /_//:/____/\:\____\\::/ /____/ /___/  \/  \/+/\  /\ ")
    print(r"///_/_/_/_/:\/::\ \:/__  __ /:/____/\:\/____/\\/____________/\  /\  / /  \/  \ ")
    print(r"//_/_/_/_//\::/\:\///_/ /_//::::::/\:\/____/  /----/----/--/  \/  \/+/\  /\  / ")
    print(r"/_/_/_/_/:\/::\ \:/__  __ /\:::::/\:\/____/ \/____/____/__/\  /\  / /  \/  \/_ ")
    print(r"_/_/_/_//\::/\:\///_/ /_//\:\::::\:\/____/ \_____________/  \/  \/+/\  /\  / ")
    print(r"/_/_/_/:\/::\ \:/__  __ /\:\:\::::\/____/   \ _ _ _ _ _ /\  /\  / /  \/  \/___ ")
    print(r"_/_/_//\::/\:\///_/ /_//\:\:\:\              \_________/  \/  \/+/\  /\  /   / ")
    print(r"/_/_/:\/::\ \:/__  __ /\:\:\:\:\______________\       /\  /\  / /  \/  \/___/_ ")
    print(r"_/_//\::/\:\///_/ /_//::\:\:\:\/______________/      /  \/  \/+/\  /\  /   / ")
    print(r"/_/:\/::\ \:/__  __ /::::\:\:\/______________/\     /\  /\  / /  \/  \/___/___ ")
    print(r"_//\::/\:\///_/ /_//:\::::\:\/______________/  \   /  \/  \/+/\  /\  /   /   / ")
    print(r"/:\/::\ \:/__  __ /:\:\::::\/______________/    \ /\  /\  / /  \/  \/___/___/ ")
    print(r"/\::/\:\///_/ /_//:\:\:\                         \  \/\\\/+/\  /\  /   /   /+/ ")
    print(r"\/::\ \:/__  __ /:\:\:\:\_________________________\ ///\\\/  \/  \/___/___/ /_ ")
    print(r"::/\:\///_/ /_//:\:\:\:\/_________________________////::\\\  /\  /   /   /+/ ")
    print(r"::\ \:/__  __ /:\:\:\:\/_________________________/:\/____\\\/  \/___/___/ /___ ")
    print(r"/\:\///_/ /_//:\:\:\:\/_________________________/:::\    /\/\  /   /   /+/   / ")
    print(r"\ \:/__  __ /:\:\:\:\/_________________________/:::::\  ///  \/___/___/ /___/_ ")
    print(r":\///_/ /_//:\:\:\:\/_________________________/:\:::::\///\  /   /  __________ ")
    print(r"\:/__  __ /:\:\:\:\/_________________________/:::\:::::\/  \/___/__/\ ")
    print(r"///_/ /_//:\:\:\:\/_________________________/:\:::\:::::\  /   /  /::\ ")
    print(r"/__  __ /\::\:\:\/_________________________/_____::\:::::\/___/__/:/\:\ ")
    print(r"/_/ /_//::\::\:\/_____________________/\/_/_/_/_/\  \           /::\ \:\ ")
    print(r"_  __ /:\::\:8\/_____________________/\/\   /\_\\/\  \ 8       /:/\:\ \:\ ")
    print(r"/ /_//\     \|______________________//\\/\::\/__\\/\  \|______/::\ \:\ \:\ ")
    print(r" __ /  \  \                        /:\/:\/\_______\/\        /:/\:\ \:\/::\ ")
    print(r"/_//    8      -8  --  --  --  -- //\::/\\/_/_/_/_/_/ --  --/::\ \:\ \::/\:\ ")
    print(r"_ /     |\  \   |________________/:\/::\///__/ /__//_______/:/\:\ \:\/::\ \:\ ")
    print(r"__________\     \               //\::/\:/___  ___ /       /::\ \:\ \::/\:\ \:\ ")
    print(r"::::::::::\\  \  \             /:\/::\///__/ /__//       /:/\:\ \:\/::\ \:\ \: ")
    time.sleep(0.8 * TextSpeed)
    print(r"You wander around the city for a while. ")
    time.sleep(0.3)
    input("Ready to start playing for real?")
    GameLoop()