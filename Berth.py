class Berth(object):

	def __init__(self, berth, ypos, xpos):
		self.berth = str(berth)
		self.ypos = int(ypos)
		self.xpos = int(xpos)
		
		self.desc = 'XXXX'

	def setDesc(self, desc):
		self.desc = str(desc)

	def showBerth(self):
		self.desc = self.berth

	def hideBerth(self):
		self.desc = 'XXXX'

