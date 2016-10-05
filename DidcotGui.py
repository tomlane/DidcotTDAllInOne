class DidcotGui(object): #maybe???
    def __init__(self, win):
      self.win = win

    def drawFixedMap(self):
      self.win.keypad(1)
      self.win.border(0)
      self.win.nodelay(1)

      self.win.addstr(0, 2, 'Didcot TD')

      self.win.addstr(33, 1, '-' * 118) #UP Main
      self.win.addstr(35, 1, '-' * 118) #DN Main
      self.win.addstr(31, 20, '-' * 30) #UP Relief Challow/Wantage
      self.win.addstr(37, 20, '-' * 29) #Dn Relief Challow/Wantage

      self.win.addstr(32, 19, '/') #um/ur challow
      self.win.addstr(36, 19, '\\') #dr/dm challow

      self.win.addstr(34, 48, "/ \\") #reversible crossovers wantage
      self.win.addstr(36, 49, '/') #dm/dr wantage
      self.win.addstr(32, 50, '\\') #ur/dm wantage
        
      self.win.addstr(37, 80, '-' * 15) #DN Milton loop
      self.win.addstr(31, 80, '-' * 45) #UR Milton
      self.win.addstr(32, 79 , '/') #UM/UR Steventon
      self.win.addstr(36, 79, '\\') #Milton loop/ DM

      self.win.addstr(36, 95, '/')


      self.win.timeout(200) 
