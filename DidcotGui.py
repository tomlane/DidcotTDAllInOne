#collection of functions that draw the didcot area and also update the berths with headcodes based on the model

madeby = "Made by Steve Rose 2016"

def drawFixedMap(win):
	win.keypad(1)
	win.border(0)
	win.nodelay(1)

	win.addstr(0, 2, 'Didcot TD')

  	win.addstr(20, 1, "-" * 77)
  	win.addstr(22, 1, "-" * 77)
  	win.addstr(18, 20, '-' * 20)
  	win.addstr(24, 20, '-' * 20)

  	win.addstr(23, 19, '-')
  	win.addstr(19, 19, '-')

  	
	win.timeout(200)   

def madeBy(win, event):
	win = win
	event = event
	if event == 32: #if space bar is pressed
		win.addstr(48, 50, madeby)
	else:
		win.addstr(48, 50, ' ' * len(madeby))