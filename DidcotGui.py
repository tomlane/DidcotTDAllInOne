#collection of functions that draw the didcot area and also update the berths with headcodes based on the model


def drawFixedMap(win):
	win.keypad(1)
	win.border(0)
	win.nodelay(1)

	win.addstr(0, 2, 'Didcot TD')

  	win.addstr(33, 1, '-' * 118) #UP Main
  	win.addstr(35, 1, '-' * 118) #DN Main
  	win.addstr(31, 20, '-' * 30) #UP Relief Challow/Wantage
  	win.addstr(37, 20, '-' * 29) #Dn Relief Challow/Wantage

  	win.addstr(32, 19, '/') #um/ur challow
  	win.addstr(36, 19, '\\') #dr/dm challow

  	win.addstr(34, 48, "/ \\") #reversible crossovers wantage
  	win.addstr(36, 49, '/') #dm/dr wantage
  	win.addstr(32, 50, '\\') #ur/dm wantage
  	
  	win.addstr(37, 80, '-' * 15) #DN Milton loop
  	win.addstr(31, 80, '-' * 45) #UR Milton
  	win.addstr(32, 79 , '/') #UM/UR Steventon
  	win.addstr(36, 79, '\\') #Milton loop/ DM

  	win.addstr(36, 95, '/')


	win.timeout(200)   



class guiModel(object): #maybe???
	#a colllection of berths
	pass

