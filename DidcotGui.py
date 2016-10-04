#collection of functions that draw the didcot area and also update the berths with headcodes based on the model

madeby = "Made by Steve Rose 2016"

def drawFixedMap(win):
	win.keypad(1)
	win.border(0)
	win.nodelay(1)

	win.addstr(0, 2, 'Didcot TD')

  	win.addstr(33, 1, "-" * 118) #UP Main
  	win.addstr(35, 1, "-" * 118) #DN Main
  	win.addstr(31, 20, '-' * 30) #UP Relief Challow/Wantage
  	win.addstr(37, 20, '-' * 29) #Dn Relief Challow/Wantage

  	win.addstr(32, 19, '/') #um/ur challow
  	win.addstr(36, 19, '\\') #dr/dm challow

  	win.addstr(34, 48, "/ \\") #reversible crossovers wantage
  	win.addstr(36, 49, '/') #dm/dr wantage
  	win.addstr(32, 50, '\\') #ur/dm wantage
  	
  	win.addstr(37, 80, "-" * 15) #Milton loop

	win.timeout(200)   

def madeBy(win, event):
	win = win
	event = event
	if event == 32: #if space bar is pressed
		win.addstr(48, 50, madeby)
	else:
		win.addstr(48, 50, ' ' * len(madeby))