import time #Used to space out messages
import json #Used for save data
import os #Used for save data
from colorama import Fore, Back, Style, init #Gives me more text formatting
init(autoreset=True)  # Automatically resets style after every print


def BitSecMission1(): #Mission Name: Welcome to Bitsec
    print("After a surprisingly pleasant meeting at Smelly's, Adam, aka SysAdam on their online forums, offers you and the small crop of this year's newbies a chance to try to hack his test server.")
    print("\"This thing SUCKS, I don't have a single protection on the login screen except for a username and a password.")
    print("You could literally just brute-force it and it would still probably work. ")
    print("Still, it's a pretty good spot to teach you some of the basics.")
    print("Try brute-forcing it, then tell me what the flag inside is.")
    print("Oh-, by the way, a \'flag\' is a piece of data you copy to prove you broke into a system.\"")
    input("Ready? \n")
    print("You find yourself staring at your laptop after SysAdam helps you connect to his server. He tells you the username is just \"SysAdamUser\" \n(Honestly, it feels weird to just call him by his real name at this point)")
    QuizAnswer = input("You don't quite remember how a brute force attack works. Do you: \nA. Try random passwords until one works \nB. Try every password until one works \nC. Try every username AND password until one works\n")
    QuizAnswer = QuizAnswer.upper() #Makes the answers case-neutral
    if QuizAnswer == "A":
        print(Style.BRIGHT + "NO, random doesn't guarantee you'd get it in time. Try again.")
        time.sleep(2.0)
        input("Ready? \n")
        BitSecMission1()
    elif QuizAnswer == "B":
        print("Yes, that was it! You remember it better now. You successfully find the correct password eventually, and proudly show SysAdam your work.")
        print("\"Nice job man! We'll make a proper hacker out of you yet.\" ")
        time.sleep(1.5)
        print(Style.BRIGHT + "Your reputation with Bitsec has increased. Your skill with Brute Force has increased.")
    elif QuizAnswer == "C":
        print("NO. Technically, this would work eventually. But it would take orders of magnitude more time, and you already have the username. Just try every password.")
        print("Try again.")
        input("Ready? \n")
        BitSecMission1()
    else:
        print("You have to answer A, B, or C. Try again.")
        input("Ready? \n")
        BitSecMission1()


def SpiderDancemission1(): #Mission Name: Welcome to Spider Dance
    print("Welcome to Spider Dance, noobs. My name is Tuffet, and it's my job to figure out which ones of you are feds, talented, or useless.")
    print("To begin, you'll try to get into this unsecured server. It doesn't have any protections at all, meaning it should be pretty easy to do. ")
    print("Just brute force it and you can move onto an actually interesting test. ")
    print("The IP is 120.26.59.257:125, and the username you're using is just \"username\"")
    print("Tell me what the password is\n")
    print("     - Tuffet")
    input("Ready? \n")
    print("After a little frantic googling, you figure out how to connect to that IP address. After that, you're met with a login screen.")
    QuizAnswer = input("You don't quite remember how a brute force attack works. Do you: \nA. Try random passwords until one works \nB. Try every password until one works \nC. Try every username AND password until one works\n")
    QuizAnswer = QuizAnswer.upper() #Makes the answers case-neutral
    if QuizAnswer == "A":
        print("NO, random doesn't guarantee you ever get it right. Try again.")
        time.sleep(2.0)
        input("Ready? \n")
        SpiderDancemission1()
    elif QuizAnswer == "B":
        print("Yes, that was it! You remember it better now. You successfully find the correct password eventually, and proudly show Tuffet your work.")
        print("\"Good, you understand how a login screen works. It's a start. \" ")
        time.sleep(1.5)
        print(Style.BRIGHT + "Your reputation with Spider Dance has increased. Your skill with Brute Force has increased.")
    elif QuizAnswer == "C":
        print("NO. Technically, this would work eventually. But it would take orders of magnitude more time, and you already have the username. Just try every password.")
        print("Try again.")
        input("Ready? \n")
        SpiderDancemission1()
    else:
        print("You have to answer A, B, or C. Try again.")
        input("Ready? \n")
        SpiderDancemission1()

def SinKingShipMission1(): # Mission Name: Welcome to SinKingShip
    print("Welcome to the SinKingShip! \n")
    print("As you should know by now, we're a group of hacktivists focused on ecological preservation and media distribution. ")
    print("In order to protect the planet, sometimes you have to force the issue a little, and in order to do so you need personal strength. ")
    print("We have long since moved past the age of strength of arm, but a similar principle applies to strength of mind.")
    print("Prove you have some basic hacking skills, and we will gladly support you throughout further training, so long as you also aid in our cause.\n")
    print("     -RootRaider")
    print("After a little frantic googling, you figure out how to connect to that IP address. After that, you're met with a login screen.")
    QuizAnswer = input("You don't quite remember how a brute force attack works. Do you: \nA. Try random passwords until one works \nB. Try every password until one works \nC. Try every username AND password until one works\n")
    QuizAnswer = QuizAnswer.upper() #Makes the answers case-neutral
    if QuizAnswer == "A":
        print("NO, random doesn't guarantee you ever get it right. Try again.")
        time.sleep(2.0)
        input("Ready? \n")
        SinKingShipMission1()
    elif QuizAnswer == "B":
        print("Yes, that was it! You remember it better now. You successfully find the correct password eventually, and proudly show RootRaider your work.")
        print("\"Good, you understand how a login screen works. It proves you can be taught. \" ")
        time.sleep(1.5)
        print(Style.BRIGHT + "Your reputation with Spider Dance has increased. Your skill with Brute Force has increased.")
    elif QuizAnswer == "C":
        print("NO. Technically, this would work eventually. But it would take orders of magnitude more time, and you already have the username. Just try every password.")
        print("Try again.")
        input("Ready? \n")
        SinKingShipMission1()
    else:
        print("You have to answer A, B, or C. Try again.")
        input("Ready? \n")
        SpiderDancemission1()


def BitSecMission2(): #Mission Name: A New Friend
    print("Yo, Alan! I heard from one of my buddies at BitSec that you were looking for a way to learn a bit more and get some hands-on experience with hacking.")
    print("There's a client I'm doing bug bounties for that has a pretty fun vulnerability in their password management system.")
    print("You wanna take a look? \n")
    print("     -Buggy")
    QuizAnswer = input("You don't quite  understand what to do. You haven't been given a username to try, you're just looking for \"a vulnerability.\" Do you: \nA. Get a username, and try every password until one works \nB. Try every username AND password until one works \nC. Ask for help \nD. Get a password, and try every username until one works. \n")
    QuizAnswer = QuizAnswer.upper() #Makes the answers case-neutral
    if QuizAnswer =="A":
        print("You take a look through their website until you find a username, jSmith. You input it and run a program to try it with every possible password, but run into a problem after just three attempts. \nAccount lockout. It's not letting you try more passwords.")
        input("Try again? \n")
        BitSecMission2()
    elif QuizAnswer == "B":
        print("No. Not only do you get an account lockout, but even if you didn't, this would take too long.")
        input("Try again? \n")
        BitSecMission2()
    elif QuizAnswer == "C":
        print("\"Yeah sure man! This is an attack called reverse brute force. You see how it says on their website that they have to change their password every 90 days? \n The seasons. Basically, a lot of people get lazy, and decide to have the current season and year as their password. So in this case, Spring2026! \"")
        time.sleep(2.0)
        print(" \"So, you can start with a password you're pretty sure works, like Spring2026!, and match it agaisnt multiple passwords. It won't trigger account lockout, because that tracks incorrect login attempts PER ACCOUNT.\" ")
        time.sleep(1.5)
        input("Ready to try again?")
        BitSecMission2()
    elif QuizAnswer == "D":
        print("You successfully execute the reverse-brute force attack. Out of this 106 person company, you find three accounts using Spring2026. \nAfter a quick walkthrough of the reporting process, you've successfully completed your first bug bounty.")
        print(" \"You can keep the bounty money as well. These easy bounties are pretty much chump change to anybody with a few years of experience.\" ")
        print(Style.BRIGHT + "Your reputation with Bitsec has increased. Your skill with Brute Force is now MAXXED.")
    else:
        BitSecMission2("You have to answer with A, B, C, or D. Try again.")


def SpiderDancemission2(): #Mission Name: Handsome Ransom
    print("BlueGolem, I've got a simple task for you.")
    print("Aperture Beauty isn't secured properly, and are therefore a perfect target for ransomware. They left their employee records public, so here's a list of employees and their usernames.")
    print("Get me a set of employee credentials and I'll buy them from you for some $$$.\n")
    print("      -ShoePuppet")
    QuizAnswer = input("You don't quite  understand what to do. You haven't been given a username to try or anything. You just know something wasn't secured properly. Do you: \nA. Ask for help \nB. Get a password, and try every username until one works\nC. Get a username, and try every password until one works \nD. Try every username AND password until one works\n")
    QuizAnswer = QuizAnswer.upper() #Makes the answers case-neutral
    if QuizAnswer == "A":
        "\"I shouldn't have to teach you this, but whatever. There's an attack called reverse-brute force, where you use a password you think might work and try it against every username. \nI already gave you a list of employee records, so use a password you think might work, and try it with every single username.\""
        input("Try again")
        SpiderDancemission2()
    elif QuizAnswer == "B":
        print("Success! You eventually find an employee you can log into their website with. Whoever this jWhite is, you can't help but feel a little bad for her. \nStill, a job is a job, and you send the credentials to ShoePuppet.")
        print(Style.BRIGHT + "Your reputation with Spider Dance has increased. Your skill with brute force is now MAXXED.")
    elif QuizAnswer == "C":
        print("You take a look through their website until you find  random username, jWhite. You input it and run a program to try it with every possible password, but run into a problem after just three attempts. \nAccount lockout. It's not letting you try more passwords.")
        input("Try again? \n")
        SpiderDancemission2()
    elif QuizAnswer == "D":
        print("No. Not only do you get an account lockout, but even if you didn't, this would take too long.")
        input("Try again? \n")
        SpiderDancemission2()
    else:
        print("You need to input A, B, C or D.")
        input("Try again? \n")
        SpiderDancemission2()
SpiderDancemission2()



def SinKingShipMission2(): # Euler's Oil
    print("BlueGolem, we have a real mission for you. ")
    print("Euler Engineering is a mechanical company that has recently made some agreements with oil barons.")
    print("Go show them the error of their ways.")
    print("I don't care what you do, just slow them down and break some stuff.")
    print("Go to their website and see what you can do.\n")
    print("     -Sinking")

def BitSecMission3(): #Mission Name: Shiny Garbage (Bug Bounty)
    print("While digging for bug bounties, you found a company that had a recent data leak and wanted to be sure their user passwords were still safe.")
    print("You can see the usernames and passwords of other users, which is bad, but the passwords are encrypted, so theoretically they still should be safe.")
    print("You have a hunch it's not that simple though. If only you knew a way to break encryption.")

def SpiderDanceMission3(): #Mission Name: Operation Iridescent Spider
    print("bMail just had a really big data leak.")
    print("Lots of user account details are out, but the passwords are hashed.")
    print("Figure out a way to break that encryption and there's lots of money in it for you.")
    print("You can find the data here: pastecan.io/bMailLeak\n")
    print("     -Spyder")

def SinKingShipMission3(): #Mission Name: RainBow Training
    print("Hey, do you wanna see an attack I found?")
    print("It's called a " + Style.BRIGHT + "Rainbow Table.")
    print("It's pretty cool, you can use it to break encryption!")
    print("There's a lot of really complicated math, but basically you encode some strings of text the same way \nover and over again until they reach a point where the output of the encoding is the same as the input. ")
    print("You can use that to reverse-engineer the encoding and eventually reverse it for other people's encrypted data too!")
    print("I made this quick server to show you how it works, come take a look! :P")
    print("      -RainbowRebel")

def BitSecMission4(): #Mission Name: XSS Webtest
    print("Some Startups, an investment company, recently made a new website for startups to apply for seed money")
    print("They have a web form that looks interesting, maybe you can find some problems there?")

def SpiderDanceMission4(): #Mission Name: San XSS-cobar
    print("San Escobar Bank recently opened, go take a look and see if you can find anything there to make us some money.")
    print("ProFit, a mercenary who works with us sometimes, has some ideas about ways we can break into their system. Expect to be compensated well.\n")
    print("     -Spyder")

def SinKingShipMission4(): #Mission Name: Lethal Injection
    print("One of our more zealous operatives, RootRaider, got caught in San Escobar trying to break up their fossil fuel logistics.")
    print("He's currently imprisoned there.")
    print("They have a draconian legal system, so he received the death sentence and is currently awaiting his execution. ")
    print("Go save him. I bet you can figure something out using their visitor form, to at least buy some time.\n")
    print("     -SinKing \n")

def BitSecMission5(): #Mission Name: Operation Arachnicide
    print("This is Agent Kaid White. You know me as Fedditor.")
    print("Spyder, the leader of the hacking group known as Spider Dance, has finally overstepped for the first time in decades.")
    print("He left his browser unsecured. We've already logged his cookies, but they're not that useful.")
    print(" If we can find a way to make him do something incriminating with that browser, we can get something useful and finally put him behind bars.")

def SpiderDanceMission5(): #Mission Name: Spying On The Spies
    print("We finally have a way in.")
    print("The Feds have been sniffing around a bit too hard lately, but they made a mistake.")
    print("The agent we know as Fedditor didn't log out properly, and one of our moles managed to replace one of his browser bookmarks with a URL that looks similar but is now owned by us! ")
    print("I'm not sure where to go from here though.")
    print("BlueGolem, you wanna take a look?")
    print("You're the most senior member not currently on other jobs.")
    print("Figure out what you want to make happen. Just be careful, alright?")
    print("Fedditor is notoriously cautious, you can't just put a \"click here\" download link to a virus and call it a day. ")
    print("Whatever you do has to look identical to the real URL.")

def SinKingShipMission5(): #Mission Name: The Green Baron
    print("BlueGolem, we finally trust you enough to share one of our truly important jobs with you.")
    print("We managed to break into the browser of the oil bigwigJack B. Rackerfellow.")
    print("He had some… questionable bookmarks, but it isn't enough to do any real damage with.")
    print("We managed to replace one of those bookmarks with a url that we own.")
    print("Find a way to get him to use that bookmark, get find some blackmail. ")
    print("And, for what it's worth, I'm sorry for whatever you'll see there.\n")
    print("     -SinKing")