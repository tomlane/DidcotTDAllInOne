class Berth(object):

	def __init__(self, berth, ypos, xpos):
		self.berth = str(berth)
		self.ypos = int(ypos)
		self.xpos = int(xpos)
		
		self.desc = '----'

	def setDesc(self, desc):
		self.desc = str(desc)


#This has some weird behaviour for showing berths after a genuine train has passed through it
	def showBerth(self):
		self.desc = self.berth

	def hideBerth(self):
		self.desc = '----'

