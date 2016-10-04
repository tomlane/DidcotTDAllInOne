class StepMsg(object):
	def __init__(self, train, start, destination):
		self.msgtype = "STEP"
		self.train = train
		self.berth = start
		self.destination = destination


class IntMsg(object):
	def __init__(self, train, berth):
		self.msgtype = "INT"
		self.train = train
		self.berth = berth


class CanMsg(object):
	def __init__(self, train, berth):
		self.msgtype = "CAN"
		self.train = train
		self.berth = berth



#re work this to inherit from a class msg which is a bit more generic
