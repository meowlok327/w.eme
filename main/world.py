import random
import os
from time import sleep
import datetime
import math

###
#
# The program PythonInTheGarden implements an application that
# creates an empty simulated world with no meaning or purpose
#
# @author Meowlok
#
###

header = "PythonInTheGarden.py"
br = "-" * 120
existObj = []
log = [f"[{datetime.datetime.now().strftime("%H:%M:%S.%f")}][main/INFO]St","art logging."]
page = 0
maze = ""
overkill = 0
file = open("View.txt","r",encoding="unicode_escape")
View = file.read().split(",,")
for i in range(len(View)):
    View[i]=View[i].split("\n")
file.close()

def addLog(msg:str,mode:int = 0):
    global log
    pre = f"[{datetime.datetime.now().strftime("%H:%M:%S")}][main/{["INFO","WARN","ERR"][mode]}]"
    for i in range(math.ceil(len(pre+msg)/30)):
        temp = (pre+msg)[i*30:(i+1)*30]
        log += [f"{temp}"]
        temp = ""

def EXECUTION(tolog:bool = True):
    global log , existObj , overkill
    if len(existObj)==0:
        addLog("all dead")
        overkill += 1
    else:
        existObj = existObj[:-1]
        if tolog:
            addLog("EXECUTION")
    update()

def update():
    global header , br , existObj , log , View , page
    os.system("cls")
    Screen = f"{header}\n{br}\n"
    for i in range(25):
        if i==0:
                Screen += "Log".ljust(29) + " | " + f"Created Obejct({len(existObj)})\n"
        else:
            if i-1 <len(log):
                if len(log)<24:
                    Screen += f"{log [i-1]}".ljust(30)
                else:
                    Screen += f"{log [i-25]}".ljust(30)
            else:
                Screen += " " * 30
            Screen += "|"
            if i < 5:
                for j in range(3):
                    if (i-1)*3+j<11 and (i-1)*3+j<len(existObj):
                        Screen += f" {existObj[(i-1)*3+j]}".ljust(28)
                    elif (i-1)*3+j==11 and len(existObj)>12:
                        Screen += f" ... and {len(existObj)-11} more"
            elif i == 5:
                Screen += "-" * 89
            else:
                if i-6<len(View[page]):
                    Screen += View[page][i-6]
            Screen += "\n"

    print(Screen)

def main():
    global page , log , existObj
    update()
    addLog("Current from Socket 1 detected.",0)
    addLog("WorldLauncher running: args [-/t]",0)
    page += 1 #switch on the power line
    sleep(0.1)
    update()
    sleep(1.8)
    for i in range(16): #remember to put on PROTECTION
        sleep(0.09)
        page +=1
        update()
    addLog("Use protection",1)
    for i in range(4): #Lay down your pieces
        sleep(0.415)
        page +=1
        update()
    addLog("Ready to start simulation",0)
    update()
    sleep(0.384)
    page += 1 #and lets begin
    update()
    sleep(0.9)
    for i in range(5): #obj creation
        page += 1
        if page == 24:
            existObj.append("Me")
        elif page == 25:
            existObj.append("You")
        elif page == 27:
            for i in range(359):
                j = f"{random.randint(0,9999)}".zfill(4)
                existObj += [f"Human Being #{j}"]
                addLog(f"Human #{j} created.")
        update()
        sleep(0.26)
    for i in range(15): #fill in my data
        page += 1
        update()
        sleep(0.09)
    for i in range(5): #per int
        page += 1
        update()
        sleep(1.8/5)
    for i in range(17): #set up our new world
        page += 1
        update()
        sleep(1.6/17)
    addLog("World created, ready to start.")
    for i in range(9): #start simu
        page += 1
        update()
        sleep(2/9)
    addLog("Starting World, please wait")
    for i in range(28): #song
        page += 1
        if i==27:
            addLog("World started, enjoy.")
        update()
        sleep(15.5/29)
    page +=1
    update()
    sleep(1.5)
    page +=1
    addLog("Get dimension.")
    update()
    sleep(2)
    page +=1
    update()
    sleep(1.6)
    page +=1
    addLog("Get circumfrence of \"Earth\".")
    update()
    sleep(2.2)
    page +=1
    update()
    sleep(1.5)
    page +=1
    addLog("Sat on something, you feel rested.")
    update()
    sleep(2.2)
    page +=1
    update()
    sleep(1.6)
    page +=1
    addLog("Traceback (most recent call last): Calc(1/0) Runtime Error: Divided by 0",2)
    update()
    sleep(2)
    addLog("Current type changed to AC",1)
    for i in range(3): #to AC
        page += 1
        update()
        sleep(0.8)
    page += 1
    update()
    addLog("Current type changed to DC",1)
    sleep(0.8)
    addLog("Visual module disabled.",2)
    for i in range(5): #and then blind my vision
        page += 1
        update()
        sleep(2/5)
    page += 1
    update()
    sleep(1.7/4)
    page += 1
    update()
    sleep(1.7/4)
    addLog("Connection unstable, check the cable.")
    page -= 1
    update()
    sleep(1.7/4)
    page += 1
    update()
    sleep(1.7/4)
    page += 1
    update()
    sleep(2.2)
    page += 1
    addLog("Year set: D.C. 617")
    update()
    sleep(0.9)
    page += 1
    addLog("Year set: B.C. 3691")
    update()
    sleep(0.7)
    page += 1
    addLog("United: Me , You")
    update()
    sleep(2)
    for i in range(5):
        page += 1
        update()
        sleep(1.9/5)
    temp=["Cucumber","Egg","Slug","Lotion"]
    for i in range(4):
        page += 1
        addLog(f"Simulate {temp[i]}: Success.")
        update()
        sleep(3.5/4)
    for i in range(4):
        page += 1
        update()
        sleep(3.6/4)
    for i in range(27):
        page += 1
        update()
        if i%3==0:
            EXECUTION()
        sleep(3.4/27)
    page += 1
    update()
    sleep(2)
    page += 1
    update()
    sleep(0.5)
    page += 1
    update()
    sleep(0.5)
    page += 1
    update()
    sleep(0.9)
    page += 1 #eggplant
    update()
    sleep(1.6)
    addLog("Simulate: Eggplant ,Success.")
    page += 1
    update()
    sleep(2)
    page += 1 #tomato
    update()
    sleep(1.5)
    addLog("Simulate: tomato ,Success.")
    page += 1
    update()
    sleep(2.2)
    page += 1 #tabby cat
    update()
    sleep(1.6)
    addLog("Simulate: tabby cat ,cute.")
    page += 1
    update()
    sleep(2.05)
    page += 1 #only god
    update()
    sleep(1.75)
    page += 1
    update()
    sleep(1.9)
    page += 1 #gender
    addLog("Role Changed: [None] -> [F].")
    update()
    sleep(2.45)
    page += 1
    addLog("Role Changed: [F] -> [M].")
    update()
    sleep(0.8)
    for i in range(12): #AM->PM
        page += 1
        update()
        sleep(3.75/12)
    page += 1 #role
    addLog("Role Changed: [None] -> [S].")
    update()
    sleep(2.9)
    page += 1
    addLog("Role Changed: [S] -> [M].")
    update()
    sleep(0.8)
    page += 1 #enter
    update()
    sleep(2)
    addLog("Lost consciousness, trying to reboot",2)
    existObj.pop(1)
    addLog("\"You\" left.",1)
    for i in range(4):
        page += 1
        update()
        sleep(1.75/4)
    for i in range(4): #VIBRATIONS
        page += 1
        update()
        sleep(3.8/4)
    for i in range(4): #COMPLETION
        page += 1
        update()
        sleep(3.65/4)
    for i in range(12): #LEFT
        page += 1
        addLog("world.search(\"you\") >>Target Not Found.",2)
        update()
        sleep(0.5)
    page += 1 #ISOLATION
    addLog("SYSTEM unstable, please backup and restart.",2)
    update()
    sleep(0.5)
    page += 1
    update()
    sleep(0.9)
    for i in range(4): #pointless
        page += 1
        addLog(f"\"{["Limitation","Tangent","Mercy","Sense"][i]}\" removed from SYSTEM by itself.",1)
        update()
        sleep(3.7/4)
    for i in range(4): #QAQ
        page += 1
        update()
        sleep(3.7/4)
    for i in range(4): #challenge
        page += 1
        update()
        sleep(2.9/4)
    page += 1 #made some
    update()
    sleep(2.4)
    for i in range(7): #Illegal
        addLog("Traceback (most recent call last): world.getEntityByUUID(\"GOD\").challenge Runtime Error: \"GOD\" is not a challengeable object",2)
        page += 1
        update()
        sleep(1.8/7)
    for i in range(5): #song
        page += 1
        update()
        sleep(14.37/5)
    for i in range(12): #EXECUTION
        page += 1
        for j in range(19):
            EXECUTION(j==8)
        update()
        sleep(10/12)
    for i in range(6): #counting
        addLog(f"Switched language to {["de","es","fr","ko","sv","zh"][i]}.")
        page += 1
        for j in range(12):
            EXECUTION(j==11)
        update()
        sleep(2.7/6)
    addLog("Switched language to en.") #EXECUTION
    page += 1
    EXECUTION()
    update()
    sleep(0.7)
    for i in range(51): #If
        page += 1
        if i%5==0:
            EXECUTION()
        update()
        sleep(3/51)
    for i in range(51): #then
        page += 1
        if i%5==0:
            EXECUTION()
        update()
        sleep(3.2/51)
    for i in range(27): #will run
        page += 1
        EXECUTION()
        update()
        sleep(3.5/27)
    page += 1 #though
    addLog("\"ME\" is not a freeable object.",2)
    update()
    sleep(0.67)
    page += 1 #we are traped
    addLog("\"ME\" is not a freeable object.",2)
    update()
    sleep(0.9)
    page += 1 #we are traped
    addLog("\"ME\" is not a freeable object.",2)
    update()
    sleep(0.9)
    page += 1 #Ahh..
    addLog("\"ME\" is not a freeable object.",2)
    update()
    sleep(1.535)
    addLog("\"Method to LOVE\" learnt by SYSTEM.")
    for i in range(3): #studied
        page += 1
        update()
        sleep(2.6/3)
    for i in range(3):
        page += 1
        update()
        sleep(1/3)
    for i in range(3): #question
        page += 1
        update()
        sleep(2.6/3)
    for i in range(3):
        page += 1
        update()
        sleep(1/3)
    page += 1 #expression
    update()
    sleep(2.8/3)
    page += 1 #expression
    update()
    sleep(2.6/3*2)
    for i in range(3):
        page += 1
        update()
        sleep(1/3)
    addLog("Status of \"You\" : left.")
    addLog("Status of \"Me\" : trapped.")
    for i in range(4): #trapped
        page += 1
        update()
        sleep(2.6/4)
    for i in range(3):
        page += 1
        update()
        sleep(1/3)
    page += 1
    addLog(f"This Fanmade MV is brought to you by meow's liver, it's {datetime.datetime.now().strftime("%H:%M")} rn, I wanna sleep.")
    update()
    sleep(13.55)
    page += 1
    EXECUTION()
    update()
    sleep(0.45)
    for i in range(5):
        addLog(f"This world will end in {5-i}")
        update()
        sleep(1)
    

main()
input(f"World ended at {datetime.datetime.now().strftime("%H:%M:%S.%f")},{"" if overkill==0 else overkill} please return to the stream.")