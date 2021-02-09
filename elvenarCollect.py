#!usr/bin/env python3

#### README
# This program is a facory for any game that needs to click every few times within an area.
# It also accepts an area to randomly click in (called a hit box) so that it appears to be human.


#### importing libraries 
import subprocess 
import os 
import time
import random
from datetime import datetime

#### Print Timers
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print("Program start time =", current_time)

# endTime = current_time + 1
# print("Approximate program end time (+1) =", current_time)
# 
# endTime = current_time + 10
# print("Approximate program end time (+10) =", current_time)
# 
# endTime = current_time + 100
# print("Approximate program end time (+100) =", current_time)



# Wait a bit of time to switch over to the proper window and tab
time.sleep(6)

#### DEFINE FUNCTIONs
def elvToolHitBox(elvShop):
    randWait = random.randrange(2,9)
    if elvShop == 1:
        #elvShop1
        elvToolHitBox0x = random.randrange(219,269)
        elvToolHitBox0y = random.randrange(820,869)

    if elvShop == 2:
        #elvShop2
        elvToolHitBox0x = random.randrange(320,375)
        elvToolHitBox0y = random.randrange(797,840)
    if elvShop == 3:
        #elvShop3
        elvToolHitBox0x = random.randrange(433,475)
        elvToolHitBox0y = random.randrange(732,770)
    if elvShop == 4:
        #elvShop4
        elvToolHitBox0x = random.randrange(513,560)
        elvToolHitBox0y = random.randrange(686,726)
    if elvShop == 5:
        #elvSelectAll
        elvToolHitBox0x = random.randrange(844,860)
        elvToolHitBox0y = random.randrange(329,345)
    if elvShop == 6:
        #elvFiveMins
        elvToolHitBox0x = random.randrange(566,694)
        elvToolHitBox0y = random.randrange(393,512)

    # click mouse
    mouseRunCommand = 'xdotool mousemove ' + str(elvToolHitBox0x) + ' ' + str(elvToolHitBox0y) + ' click 1 &'
    data = subprocess.Popen([mouseRunCommand], shell=True)
    output = data.communicate()
    time.sleep(randWait)

#### While loop to collect tools for one hour by looping a dozen times every five minutes
l = 12
while l > 0:
    #### Time Stamp
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Program start time =", current_time)
    
    #### Produce
    # click on a random Workshop
    randWait = random.randrange(1,4)
    print("Choosing workshop ", randWait, " to produce.")
    elvToolHitBox(randWait)

    # Click Select All Button in Pop up
    print("Producing.")
    elvToolHitBox(5)

    # Click 5 minutes
    elvToolHitBox(6)

    # Hangout for about five to six minutes
    randWait = random.randrange(310,350)
    print("Waiting for ", randWait, " seconds.")
    time.sleep(randWait)

    #### Collect Tools
    j = 4
    while j > 0:
        randWait = random.randrange(2,4)
        elvToolHitBox(j)
        j -= 1
    print("Collected Tools. Completed loop ", l, ".")
    l -= 1
