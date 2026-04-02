import time #Used to space out messages
import json #Used for save data
import os #Used for save data
from colorama import Fore, Back, Style, init #Gives me more text formatting
init(autoreset=True)  # Automatically resets style after every print

def BitSecMission1(Attempted=False): #Mission Name: Welcome to Bitsec
    if Attempted == False:
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
        BitSecMission1(Attempted=True)
    elif QuizAnswer == "B":
        print("Yes, that was it! You remember it better now. You successfully find the correct password eventually, and proudly show SysAdam your work.")
        print("\"Nice job man! We'll make a proper hacker out of you yet.\" ")
        time.sleep(1.5)
        print(Style.BRIGHT + "Your reputation with Bitsec has increased. Your skill with Brute Force has increased.")
    elif QuizAnswer == "C":
        print("NO. Technically, this would work eventually. But it would take orders of magnitude more time, and you already have the username. Just try every password.")
        print("Try again.")
        input("Ready? \n")
        BitSecMission1(Attempted=True)
    else:
        print("You have to answer A, B, or C. Try again.")
        input("Ready? \n")
        BitSecMission1(Attempted=True)

def SpiderDancemission1(Attempted = False): #Mission Name: Welcome to Spider Dance
    if Attempted == False:
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
        SpiderDancemission1(Attempted=True)
    elif QuizAnswer == "B":
        print("Yes, that was it! You remember it better now. You successfully find the correct password eventually, and proudly show Tuffet your work.")
        print("\"Good, you understand how a login screen works. It's a start. \" ")
        time.sleep(1.5)
        print(Style.BRIGHT + "Your reputation with Spider Dance has increased. Your skill with Brute Force has increased.")
    elif QuizAnswer == "C":
        print("NO. Technically, this would work eventually. But it would take orders of magnitude more time, and you already have the username. Just try every password.")
        print("Try again.")
        input("Ready? \n")
        SpiderDancemission1(Attempted=True)
    else:
        print("You have to answer A, B, or C. Try again.")
        input("Ready? \n")
        SpiderDancemission1(Attempted=True)

def SinKingShipMission1(Attempted = False): # Mission Name: Welcome to SinKingShip
    if Attempted == False:
        print("Welcome to the SinKingShip! \n")
        print("As you should know by now, we're a group of hacktivists focused on ecological preservation and media distribution. ")
        print("In order to protect the planet, sometimes you have to force the issue a little, and in order to do so you need personal strength. ")
        print("We have long since moved past the age of strength of arm, but a similar principle applies to strength of mind.")
        print("Prove you have some basic hacking skills, and we will gladly support you throughout further training, so long as you also aid in our cause.\n")
        print("     -RootRaider\n")
        input("Ready?\n")
        print("After a little frantic googling, you figure out how to connect to that IP address. After that, you're met with a login screen.")
    QuizAnswer = input("You don't quite remember how a brute force attack works. Do you: \nA. Try random passwords until one works \nB. Try every password until one works \nC. Try every username AND password until one works\n")
    QuizAnswer = QuizAnswer.upper() #Makes the answers case-neutral
    if QuizAnswer == "A":
        print("NO, random doesn't guarantee you ever get it right. Try again.")
        input("Ready? \n")
        SinKingShipMission1(Attempted=True)
    elif QuizAnswer == "B":
        print("Yes, that was it! You remember it better now. You successfully find the correct password eventually, and proudly show RootRaider your work.")
        print("\"Good, you understand how a login screen works. It proves you can be taught. \" ")
        time.sleep(1.5)
        print(Style.BRIGHT + "Your reputation with Spider Dance has increased. Your skill with Brute Force has increased.")
    elif QuizAnswer == "C":
        print("NO. Technically, this would work eventually. But it would take orders of magnitude more time, and you already have the username. Just try every password.")
        print("Try again.")
        input("Ready? \n")
        SinKingShipMission1(Attempted=True)
    else:
        print("You have to answer A, B, or C. Try again.")
        input("Ready? \n")
        SpiderDancemission1(Attempted=True)

def BitSecMission2(Attempted = False, HelpAsked = False): #Mission Name: A New Friend
    if Attempted == False:
        print("Yo, Alan! I heard from one of my buddies at BitSec that you were looking for a way to learn a bit more and get some hands-on experience with hacking.")
        print("There's a client I'm doing bug bounties for that has a pretty fun vulnerability in their password management system.")
        print("You wanna take a look? \n")
        print("     -Buggy")
    QuizAnswer = input("You don't quite  understand what to do. You haven't been given a username to try, you're just looking for \"a vulnerability.\" Do you: \nA. Get a username, and try every password until one works \nB. Try every username AND password until one works \nC. Ask for help \nD. Get a password, and try every username until one works. \n")
    QuizAnswer = QuizAnswer.upper() #Makes the answers case-neutral
    if QuizAnswer =="A":
        print("You take a look through their website until you find a username, jSmith. You input it and run a program to try it with every possible password, but run into a problem after just three attempts. \nAccount lockout. It's not letting you try more passwords.")
        input("Try again? \n")
        BitSecMission2(Attempted=True)
    elif QuizAnswer == "B":
        print("No. Not only do you get an account lockout, but even if you didn't, this would take too long.")
        input("Try again? \n")
        BitSecMission2(Attempted=True)
    elif QuizAnswer == "C":
        print("\"Yeah sure man! This is an attack called reverse brute force. You see how it says on their website that they have to change their password every 90 days? \n The seasons. Basically, a lot of people get lazy, and decide to have the current season and year as their password. So in this case, Spring2026! \"")
        time.sleep(2.0)
        print(" \"So, you can start with a password you're pretty sure works, like Spring2026!, and match it agaisnt multiple passwords. It won't trigger account lockout, because that tracks incorrect login attempts PER ACCOUNT.\" ")
        time.sleep(1.5)
        input("Ready to try again?/n")
        BitSecMission2(Attempted=True, HelpAsked=True)
    elif QuizAnswer == "D" and HelpAsked == True:
        print("You successfully execute the reverse-brute force attack. Out of this 106 person company, you find three accounts using Spring2026. \nAfter a quick walkthrough of the reporting process, you've successfully completed your first bug bounty.")
        print(" \"You can keep the bounty money as well. These easy bounties are pretty much chump change to anybody with a few years of experience.\" ")
        print(Style.BRIGHT + "Your reputation with Bitsec has increased. Your skill with Brute Force is now MAXXED.")
    elif QuizAnswer == "D" and HelpAsked == False:
        print("How would that work? You should ask for help first.")
        input("Ready?\n")
        BitSecMission2(Attempted=True)
    else:
        BitSecMission2("You have to answer with A, B, C, or D. Try again.")

def SpiderDancemission2(Attempted = False): #Mission Name: Handsome Ransom
    if Attempted == False:  
        print("BlueGolem, I've got a simple task for you.")
        print("Aperture Beauty isn't secured properly, and are therefore a perfect target for ransomware. They left their employee records public, so here's a list of employees and their usernames.")
        print("Get me a set of employee credentials and I'll buy them from you for some $$$.\n")
        print("      -ShoePuppet")
    QuizAnswer = input("You don't quite  understand what to do. You haven't been given a username to try or anything. You just know something wasn't secured properly. Do you: \nA. Ask for help \nB. Get a password, and try every username until one works\nC. Get a username, and try every password until one works \nD. Try every username AND password until one works\n")
    QuizAnswer = QuizAnswer.upper() #Makes the answers case-neutral
    if QuizAnswer == "A":
        print("\"I shouldn't have to teach you this, but whatever. There's an attack called reverse-brute force, where you use a password you think might work and try it against every username. \nI already gave you a list of employee records, so use a password you think might work, and try it with every single username.\"")
        input("Try again? \n")
        SpiderDancemission2(Attempted=True)
    elif QuizAnswer == "B":
        print("Success! You eventually find an employee you can log into their website with. Whoever this jWhite is, you can't help but feel a little bad for her. \nStill, a job is a job, and you send the credentials to ShoePuppet.")
        print(Style.BRIGHT + "Your reputation with Spider Dance has increased. Your skill with brute force is now MAXXED.")
    elif QuizAnswer == "C":
        print("You take a look through their website until you find  random username, jWhite. You input it and run a program to try it with every possible password, but run into a problem after just three attempts. \nAccount lockout. It's not letting you try more passwords.")
        input("Try again? \n")
        SpiderDancemission2(Attempted=True)
    elif QuizAnswer == "D":
        print("No. Not only do you get an account lockout, but even if you didn't, this would take too long.")
        input("Try again? \n")
        SpiderDancemission2(Attempted=True)
    else:
        print("You need to input A, B, C or D.")
        input("Try again? \n")
        SpiderDancemission2(Attempted=True)

def SinKingShipMission2(Attempted = False): # Euler's Oil
    if Attempted == False:
        print("BlueGolem, we have a real mission for you. ")
        print("Euler Engineering is a mechanical company that has recently made some agreements with oil barons.")
        print("Go show them the error of their ways.")
        print("I don't care what you do, just slow them down and break some stuff.")
        print("Go to their website and see what you can do.\n")
        print("     -Sinking")
    QuizAnswer = input("\nYou don't quite  understand what to do. You haven't been given a username to try or anything. You just know something wasn't secured properly. Do you: \nA. Ask for help \nB. Get a password, and try every username until one works\nC. Get a username, and try every password until one works \nD. Try every username AND password until one works\n")
    QuizAnswer = QuizAnswer.upper()
    if QuizAnswer == "A":
        print("\"There's an attack called reverse-brute force, where you use a password suspect could work and check it with every username. \nUse a password you think might work, and try it with every single username.\"")
        input("Try again? \n")
        SinKingShipMission2(Attempted=True)
    elif QuizAnswer == "B":
        print("Success! Their policy says that employees have to change their passwords every 90 days. You try the season and the year. (Spring2026!) \nYou eventually find an employee you can log into their website with. Whoever this kSteele is, you can't help but feel a little bad for her. \nStill, a job is a job, and you send the credentials to SinKing saying this is the most you can do.")
        print(Style.BRIGHT + "Your reputation with SinKingShip has increased. Your skill with brute force is now MAXXED.")
    elif QuizAnswer == "C":
        print("You take a look through their website until you find  random username, kSteele. You input it and run a program to try it with every possible password, but run into a problem after just three attempts. \nAccount lockout. It's not letting you try more passwords.")
        input("Try again? \n")
        SinKingShipMission2(Attempted=True)
    elif QuizAnswer == "D":
        print("No. Not only do you get an account lockout, but even if you didn't, this would take too long.")
        input("Try again? \n")
        SinKingShipMission2(Attempted=True)
    else:
        print("You need to input A, B, C or D.")
        input("Try again? \n")
        SinKingShipMission2(Attempted=True)

def BitSecMission3(Attempted = False): #Mission Name: Shiny Garbage (Bug Bounty), requires Rainbow Tables 1
    if Attempted == False:
        print("While digging for bug bounties, you found a company that had a recent data leak and wanted to be sure their employee passwords were still safe.")
        print("You can see the usernames and passwords of other employees, which is bad, but the passwords are encrypted, so theoretically they still should be safe.")
        print("You have a hunch it's not that simple though. If only you knew a way to break encryption.")
        input("\nReady?\n")
        print("You use the RainbowTable app you installed to check if their hashing is insecure. ")
        time.sleep(1.0)
        print("...") 
        time.sleep(0.5)
        print("...") 
        time.sleep(0.5)
        print("...") 
        time.sleep(0.5)
        print("Success! It looks like this garbage disposal company is using an outdated hashing algorithm and didn't salt their passwords to protect against this attack.")
        print("After reporting the bug and collecting your bounty, you show off the attack at your next BitSec meeting.") 
        print("There is some polite applause from the audience, like they're applauding a middle school science project.")
        time.sleep(1.5)
        print("...It still feels good though.")
        print(Style.BRIGHT + "You aren't talented enough at math to have a better understanding of Rainbow Tables, so your skill is still MAXXED. Your reputation with BitSec has increased!")

def SpiderDanceMission3(Attempted = False): #Mission Name: Operation Iridescent Spider, requires Rainbow Tables 1
    if Attempted == False:
        print("bMail just had a really big data leak.")
        print("Lots of user account details are out, but the passwords are hashed.")
        print("Figure out a way to break that encryption and there's lots of money in it for you.")
        print("You can find the data here: pastecan.io/bMailLeak\n")
        print("     -Spyder")
        input("\nReady?\n")
        print("You successfully use the RainbowTable app you installed to check if their hashing is insecure.\nIt is!")
        print(Style.BRIGHT + "You aren't talented enough at math to have a better understanding of Rainbow Tables, so your skill is still MAXXED. Your reputation with Spider Dance has increased!")

def SinKingShipMission3(Attempted = False):
    if Attempted == False:
        print("Hey, do you wanna see an attack I found?")
        print("It's called a " + Style.BRIGHT + "Rainbow Table.")
        print("It's pretty cool, you can use it to break encryption!")
        print("There's a lot of really complicated math, but basically you encode some strings of text the same way \nover and over again until they reach a point where the output of the encoding is the same as the input. ")
        print("You can use that to reverse-engineer the encoding and eventually reverse it for other people's encrypted data too!")
        print("I made this quick server to show you how it works, come take a look! :P")
        print("      -RainbowRebel\n")
        input("Ready?\n")
        print("To understand how to break cryptography, you first have to understand how to make it.")
        time.sleep(1.5)
        print("The simplest form of cryptography is the Ceasar Cipher. You put each letter on a wheel, then you rotate it by a given amount of letters.")
        time.sleep(2.5)
        print("So, with a key of 1, \"abc\" becomes \"bcd\". ")
        time.sleep(2.0)
        print("With an actual sentence, like: \n\"The quick brown fox jumps over the lazy dog\", it turns into the incomprehensible: \n\"Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph\"")
        time.sleep(2.5)
        print("Modern cryptography is sort of similar, it just uses more complicated math. We have better algorithms than just rotating everything by one.")
        time.sleep(2.0)
        print("So basically, you do a bunch of math to your starting data to make it incomprehensible, and ideally impossible to re-comprehensible-ify it without knowing the key.")
        time.sleep(2.0)
        print("A Rainbow Table is an attack that tries to decode the information so we have what the original is.")
    QuizAnswer = input("Get it? (Yes/No)")
    QuizAnswer = QuizAnswer.upper()
    if QuizAnswer == "YES" or QuizAnswer == "Y" or QuizAnswer =="YEAH":
        print("Cool, good talk.")
        print(Style.BRIGHT + "Your skill with Rainbow Tables has increased! Your reputation with SinKingShip has increased!")
    else:
        print("That's ok, most people don't really get it either. Just use this app to decode stuff.")
        time.sleep(2.5)
        SinKingShipMission3(Attempted=True)

def BitSecMission4(Attempted = False): #Mission Name: XSS Webtest
    if Attempted == False:
        print("Some Startups, an investment company, recently made a new website for startups to apply for seed money")
        print("They have a web form that looks interesting, maybe you can find some problems there?")
        input("\nReady?\n")
    print("You're looking for weaknesses, but you haven't found anything just yet. They have correct account lockouts, no recent data leaks, \n it seems like their servers are secured correctly, what can you do?")
    QuizAnswer = input("Do you \nA: Give up \nB: Ask for help \nC: Mess with their web form\n")
    QuizAnswer = QuizAnswer.upper()
    if QuizAnswer == "A":
        print("Never back down, never give up! There's no such thing as a perfect system.")
        input("Ready?\n")
        BitSecMission4(Attempted=True)
    if QuizAnswer == "B":
        print("You call up your friend Buggy, and he explains an idea he has. \"I trust you're familiar with XSS attacks? \nI bet you could use one here. If you use this web form they have for startups to apply for money, maybe it isn't sanitized correctly and you could find something there.\"")
        input("Looks like you need to attack their web form. Ready? \n")
        BitSecMission4(Attempted=True)
    if QuizAnswer == "C":
        print("After a little SQL injection, you've found part of what you need. You know the investment database name, so you can just drop a table to prove your attack works.")
        print("\"Robert') DROP TABLE Applicants;--\" makes a submission, and although there's no output on your end, \na command to give you a list of applicants now gives you a blank list.")
        time.sleep(3.0)
        print("...Come to think of it, you could have just given this company their list of applicants as proof that their system was insecure.")
        time.sleep(2.0)
        print(Style.BRIGHT + "Your skill with MITM attacks has increased! " + Style.RESET_ALL +  "Some of Some Startups' startups have to resubmit their applications.")

def SpiderDanceMission4(usernamelist = False, Attempted = False): #Mission Name: San XSS-cobar
    if Attempted == False:
        print("San Escobar Bank recently opened, go take a look and see if you can find anything there to make us some money.")
        print("ProFit, a mercenary who works with us sometimes, has some ideas about ways we can break into their system. Expect to be compensated well.\n")
        print("     -Spyder")
        print("You're not sure what to do to attack this bank. They don't have a mobile app, you obviously can't travel to San Escobar to try to attack them in person. \nThe only option you really have is their website.")
        input("Ready?\n")
    QuizAnswer = input("Do you: \nA: Try to brute force their login system \nB: Talk to ProFit \nC: Attack the servers directly \nD: Attack through their login page\n")
    QuizAnswer = QuizAnswer.upper()
    if QuizAnswer == "A" and usernamelist == False:
        print("No dice. You got an account lockout, and you don't have a list of usernames to attempt reverse brute-force.")
        input("Ready to try again? \n")
        SpiderDanceMission4(Attempted=True)
    elif QuizAnswer == "A" and usernamelist == True:
        print("Success! With the list of usernames you've obtained, you manage to execute a reverse brute force attack, obtaining access credentials of multiple bank members.")
        print(Style.BRIGHT + "Your skill with XSS attacks has increased! Your reputation with Spider Dance has increased!")
    elif QuizAnswer == "B":
        print("\"Hello, BlueGolem. My name is ProFit, and Spyder has informed me that you would be assisting me with this operation. \nMy current best idea is to perform an XSS attack on their web page, causing it to send the credentials of all successful login attempts to a website owned by Spider Dance.\"")
        print("The two of you attempt the XSS attack, but with only some success. You manage to get a list of usernames, but the passwords are encrypted and salted before they get to you.")
        print(Style.BRIGHT + "If only there was something you could do with a list of usernames.")
        input("Ready?\n")
        SpiderDanceMission4(usernamelist=True, Attempted=True)
    elif QuizAnswer == "C":
        print("Looks like nothing for you here. You don't have the IP for any of their servers, you don't even know what to attack.")
        input("Ready to try again? \n")
        SpiderDanceMission4(Attempted=True)
    elif QuizAnswer == "D":
        print("You take a closer look at their web form, and although it seems simple enough, it's actually fairly well protected. \nYou could probably take down their form, but that wouldn't make you any money. \nMaybe ProFit has some ideas?")
        input("Ready?\n")
        SpiderDanceMission4(Attempted=True)
    else:
        print("Type A, B, C, or D.")
        input("Ready?")
        SpiderDanceMission4(Attempted=True)

def SinKingShipMission4(Attempted=False): #Mission Name: Lethal Injection
    print("One of our more zealous operatives, RootRaider, got caught in San Escobar trying to break up their fossil fuel logistics.")
    print("He's currently imprisoned there.")
    print("They have a draconian legal system, so he received the death sentence and is currently awaiting his execution. ")
    print("Go save him. I bet you can figure something out using their visitor form, to at least buy some time.\n")
    print("     -SinKing \n")
    print("You open the visitor form, and see a bunch of information. You can't upload files, which would have made things easy, but you can upload text.")
    QuizAnswer = input("You don't know how to attack them. You can \nA: Ask SinKing for help \nB: Look for more info \nC: Little Bobby Tables \n")
    QuizAnswer = QuizAnswer.upper()
    if QuizAnswer == "A":
        print("\"If I had any good ideas as to how to get him out, I wouldn't have had to ask you. I'm sorry, I truly wish I could do more.\"")
        input("Well, that was useless. Ready to try again?\n")
        SinKingShipMission4(Attempted=True)
    elif QuizAnswer == "B":
        print("Digging a little deeper into their website, you still aren't finding much. You dig through their cases for a while, and although you find plenty of examples of injustice, you aren't finding any weaknesses to act on.")
        input("Ready to try again?\n")
        SinKingShipMission4(Attempted=True)
    elif QuizAnswer == "C":
        print("If you can't attack anything else, you'll attack the web form.")
        time.sleep(1.0)
        print("You submit a request to visit. Not you, of course, but \"Robert') DROP TABLE Prisoners;--\" who destroys their database. \nHow are they going to execute these prisoners when they don't even know who to execute?")
        print("This solution won't last forever, but it should still buy some time.")
        time.sleep(1.0)
        print(Style.BRIGHT + "Your reputation with SinKingShip has increased! Your skill with XSS attacks has increased!")

def BitSecMission5(Attempted = False): #Mission Name: Operation Arachnicide
    if Attempted == False:
        print("This is Agent Kaid White. You know me as Fedditor.")
        print("Spyder, the leader of the hacking group known as Spider Dance, has finally overstepped for the first time in over a decade.")
        print("He left his browser unsecured. We've already logged his cookies, but they're nothing useful.")
        print("If we can find a way to make him do something incriminating with that browser, we can put him behind bars.")
        input("Ready?\n")
    print("You have an idea for how to catch a Spyder. If you're trying to eavesdrop, a MITM attack seems great.")
    QuizAnswer = input("What should you mirror though? \nA: bMail \nB: PasteCan \nC: TeleOunce \nD: Calendar\n")
    QuizAnswer = QuizAnswer.upper()
    if QuizAnswer == "A":
        print("You set up a mirror on a similar website. bMail becoms bMaiI, which looks like an identical URL on most browsers.")
        print("It takes a few days of waiting, but eventually you get a hit. The Spyder is on the web.")
        time.sleep(3.0)
        print("Everything is set up correctly, and you watch him check his email. It's mostly just marketing emails. \nEventually, he disconnects his side of the connection, but you decide not to let that input through.")
        time.sleep(2.5)
        print("Instead, when he closes it, you remain logged in and able to go through his emails.")
        time.sleep(2.0)
        print("...Unfortunately, you don't end up finding much of value. You can see his real name, but Kumo Örümcek was already a known quantity. ")
        print("You'll have to try something else.")
        input("Ready to try again?\n")
        BitSecMission5(Attempted=True)
    elif QuizAnswer == "B":
        print("You mirror his PasteCan, and although it's full of data leaks and pirated files, there's nothing truly incriminating.")
        print("Although the distribution of this content would be illegal, the mere act of having it is not. Thus, this is useless.")
        input("Ready to try again?\n")
        BitSecMission5(Attempted=True)
    elif QuizAnswer == "C":
        print("You scarcely have to wait an hour to find something spicy. Since Spyder doesn't save his passwords, the keylogger you have on your mirror recorded his username and password as he logged into his TeleOunce account.")
        print("The username and password are both just seemingly random strings of letters.")
        time.sleep(1.0)
        print("Interestingly, based on the timing of the keystrokes, he seems to have typed both of those in manually.")
        time.sleep(1.5)
        print("After he logs in, there's a few minutes of him just looking at memes. Some of them are actually pretty funny.")
        print("Still, after a while he goes into a server with a similarly weird-looking name, and it's there that you can see some real crime happening.")
        time.sleep(1.0)
        print("Bingo. You see the usernames of other semi-known members of Spider Dance, like Cackler and ShoePuppet.")
        print("Ladies and gentlemen, we got em. You see them discussing new jobs, and the combination of the screen recorder and the keylogger are enough to get more than enough incriminating evidence to put Spyder away.")
        time.sleep(2.0)
        print("You pass the data over to Fedditor, along with a little present of your own design.")
        time.sleep(1.0)
        print("You manage to maintain the login even after Spyder closes the application on his end. \nThus, Fedditor has a way in with every single other member of Spider Dance and can impersonate Spyder to try to get more of them.")
        print(Style.BRIGHT + "Your reputation with BitSec is now MAXXED. Your skill with MITM attacks is now MAXXED.")
    elif QuizAnswer == "D":
        print("Nothing of use here. You see some medical appointments or TV shows, but that's about the extent of it. \nYou almost feel bad for him, this guy has no social life.")
        input("Ready to try again?")
        BitSecMission5(Attempted=True)
    else:
        print("You need to answer A, B, C, or D.")
        BitSecMission5(Attempted=True)

def SpiderDanceMission5(Attempted = False): #Mission Name: Spyder Bites
    if Attempted == False:
        print("We finally have a way in.")
        print("The Feds have been sniffing around a bit too hard lately, but they made a mistake.")
        print("The agent we know as Fedditor didn't log out properly, and one of our moles managed to replace one of his browser bookmarks with a URL that looks similar but is now owned by us! ")
        print("I'm not sure where to go from here though.")
        print("BlueGolem, you wanna take a look?")
        print("You're the most senior member not currently on other jobs.")
        print("Figure out what you want to make happen. Just be careful, alright?")
        print("Fedditor is notoriously cautious, you can't just put a \"click here\" download link to a virus and call it a day. ")
        print("Whatever you do has to look identical to the real URL.")
        print("\n   -Spyder \n")
        input("Ready?\n")
    print("If you're trying to eavesdrop, a MITM attack seems perfect.")
    QuizAnswer = input("What should you mirror though? \nA: bMail \nB: InternalCommunications \nC: Calendar\n")
    QuizAnswer = QuizAnswer.upper()
    if QuizAnswer == "A":
        print("Every morning at 8:58  sharp Fedditor, who you now know as Kaid White, logs into his work bMail account. \nHis wife/daughter Joanne White (You're not sure, you just know he calls her honey) sends him personal emails every now and then.")
        time.sleep(1.0)
        print("However, the vast majority of emails he receives are from other feds. \nMost of those also contain enough corporate and technical jargon to atomize a Victorian child.")
        time.sleep(1.0)
        print("Of the small amount that's left, there are some useful ones.")
        time.sleep(1.0)
        print("You find some emails about future federal projects, some attack plans, and even some information on other 3rd-party hackers that Spider Dancers have worked with in the past.")
        input("View?\n")
        print("You find dossiers on Markenary, RxGoon, ProFit, and even Brainz4Rent. Most of them are just behavioral patterns, but Brainz's dossier has his name and address. \nIt looks like they're planning on arressting him soon.")
        print("You save all the emails, sharing the work emails with Spyder. You don't share the personal emails though. \nEven if you're a criminal, some things should still be sacred.")
        print(Style.BRIGHT + "Your reputation with Spider Dance is MAXXED. Your skill with MITM attacks is MAXXED.")
    if QuizAnswer == "B":
        print("Taking a look through their internal comms app, you don't find too much of value. The stuff in there is automatically deleted after being read. \nYou set up a logger for later, but as of now, this isn't anything.")
        input("Ready to try again?\n")
        SpiderDanceMission5(Attempted=True)
    if QuizAnswer == "C":
        print("Digging into his calendar the next time you open it, you don't find much of value. \nA few meetings, doctor's appointments, and birthdays, but nothing really worth breaking into the government for.")
        print("Nevertheless, you dutifully record it and send it to Spyder. Still, it's not enough.")
        input("Ready to try again?\n")
        SpiderDanceMission5(Attempted=True)

def SinKingShipMission5(Attempted=False): #Mission Name: The Green Baron
    if Attempted == False:
        print("BlueGolem, we finally trust you enough to share one of our truly important jobs with you.")
        print("We managed to break into the browser of the oil bigwig Jack B. Rackerfellow.")
        print("He had some… questionable bookmarks, but it isn't enough to do any real damage with.")
        print("We managed to replace one of those bookmarks with a url that we own.")
        print("Find a way to get him to use that bookmark, get find some blackmail. ")
        print("And, for what it's worth, I'm sorry for whatever you'll see there.\n")
        print("     -SinKing\n")
        input("Ready?\n")
        print("Taking a closer look at the list of booksmarks, you can see the issues. \nTruly, it's among the most morally reprehensible acts you've ever seen.")
        time.sleep(2.5)
        print("Jack B. Rackerfellow is...")
        time.sleep(1.0)
        print("...")
        time.sleep(1.0)
        print("...")
        time.sleep(1.0)
        print("...a \"Sorcery the Collecting\" player.")
        time.sleep(1.0)
        print("Not only that, but there's more! His decks are the most expensive, pay-to-win ones! \nWhat an evil man.")
        time.sleep(2.0)
        print("Still, this isn't exactly blackmail material. You need something better.")
        time.sleep(2.0)
    QuizAnswer = input("Do you: \nA: Replace one of his decks with a control deck to see if he still plays it \nB: Just put a \"Click Here!\" ransomware virus on your mirror \nC: Leak that he's a Sorcery player\n ")
    QuizAnswer = QuizAnswer.upper()
    if QuizAnswer == "A":
        print("Not only does the knave play it, it becomes his most used deck! ...Unfortunately, this still isn't enough blackmail.")
        input("Ready to try again?\n")
        SinKingShipMission5(Attempted=True)
    elif QuizAnswer == "B":
        print("He falls for it! What an idiot. You show SinKing your work, and though you both shudder at the oligarch's taste in card games, he agrees the ransomware is enough.")
        print("\"You know what, fair enough. No need to overcomplicate it.\"")
        print("Sinking eventually sends Mr. Rackerfeller a message offering to decrypt the computer in exchange for some policy changes. \nIt ain't honest work, but it's much. /(^.^/) ")
    elif QuizAnswer == "C":
        input("That might be a hit to his reputation, but it also loses your only bargaining chip. \nYou can't blackmail him when you give away your only blackmail. Try again? \n")
        SinKingShipMission5(Attempted=True)
    else:
        input("You gotta input A, B, or C. Try again? \n")
        SinKingShipMission5(Attempted=True)