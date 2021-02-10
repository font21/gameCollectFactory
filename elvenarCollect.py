#!usr/bin/env python3

#### README
# This program is a factory for any game that needs a few clicks every few minutes within an area.
# It also accepts an area to randomly click in (called a hit box) so that it appears to be human.
# Next: build in a flat file that accepts JSON data to define the hitbox.

# Program Outline
# I.	Imported libraries
# II.	Functions
# III.	Set main variables
# IV.	Main program
# V.	Close Out





#### imported libraries
import os 
import time
import random
import sys
import sys, getopt
import subprocess
from datetime import datetime

#### DEFINE FUNCTIONs

# Define Hit Box and mouse movement.
# Accepts two Paramaters: Which Workshop and hover|click
def elvToolHitBox(elvShop, hc):
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
	
	# Mouse: Hover or click
	if hc == 0:
		mouseRunCommand = 'xdotool mousemove ' + str(elvToolHitBox0x) + ' ' + str(elvToolHitBox0y)'
	if hc == 1:
		mouseRunCommand = 'xdotool mousemove ' + str(elvToolHitBox0x) + ' ' + str(elvToolHitBox0y) + ' click 1 &'

	data = subprocess.Popen([mouseRunCommand], shell=True)
	output = data.communicate()
	time.sleep(randWait)


#Harvest Function: Clikck and drag from one point to another in order to harvest tools from Workshops
def elvHarvestHitBox(elvShop):
	randWait = random.randrange(2,9)
	if elvShop == 1:
		#elvShop1
		elvToolHitBox0x = random.randrange(219,269)
		elvToolHitBox0y = random.randrange(820,869)

	if elvShop == 2:
		#elvShop4
		elvToolHitBox0x = random.randrange(513,560)
		elvToolHitBox0y = random.randrange(686,726)

	# click mouse
	mouseRunCommand = 'xdotool mousemove ' + str(elvToolHitBox0x) + ' ' + str(elvToolHitBox0y) + ' click 1 &'
	data = subprocess.Popen([mouseRunCommand], shell=True)
	output = data.communicate()
	time.sleep(randWait)



def main(argv):
	helpText = 'elvenarCollect.py -i 6 -l 36'
	initialSleepTime = ''
	l = ''
	try:
		opts, args = getopt.getopt(argv,"hil",["initialWait=","looper="])
	except getopt.GetoptError:
		print helpText
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print helpText
			sys.exit()
		elif opt in ("-i", "--initialWait"):
			initialWait = arg
		elif opt in ("-o", "--looper"):
			looper = arg
	print 'Input file is "', inputfile
	print 'Output file is "', outputfile


#### Set main variables
l = 24
initialWait = 6

# Wait a bit of time to switch over to the proper window and tab.
time.sleep(initialWait)

# Main program
#### While loop to collect tools for one hour by looping a dozen times every five minutes
if __name__ == "__main__":
   main(sys.argv[1:])

while l > 0:
	#### Time Stamp
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print('Program start time: ', current_time)

	#### Produce
	# click on a random Workshop
	randWait = random.randrange(1,4)
	print('Choosing workshop ', randWait, ' to produce.')
	elvToolHitBox(randWait)

	# Click Select All Button in Pop up
	print('Producing.')
	elvToolHitBox(5, 1)

	# Click 5 minutes
	elvToolHitBox(6, 1)

	# Hangout for about five to six minutes to appear human
	randWait = random.randrange(303,333)
	print('Waiting for ', randWait, ' seconds.')
	time.sleep(randWait)

	#### Collect Tools
	j = 4
	while j > 0:
		randWait = random.randrange(2,4)
		elvToolHitBox(j, 1)
		j -= 1

	# Move mouse over a workshop and hover without clicking just to get info and timing information
	w = random.randrange(1,4)
	elvToolHitBox(w, 0)

	print('Collected Tools. Completed loop ', l, '.')
	l -= 1

# Close Out
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print('Program Completion time: ', current_time)
print('Exiting.')