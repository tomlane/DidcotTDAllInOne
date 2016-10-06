class Berth(object): #maybe?

	def __init__(self, berth, ypos, xpos):
		self.berth = str(berth)
		self.ypos = int(ypos)
		self.xpos = int(xpos)
		
		self.desc = '????'

	def setDesc(self, desc):
		self.desc = str(desc)

	def clearDesc(self):
		self.desc = ''

	def hello(self): #<test shit
		return self.berth