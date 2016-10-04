#State of the railway

#state model a dictionary where the key is the berth number and the value is the train headcode?

import json


class StateModel(object):


	def __init__(self):
		self.state = {} #map is empty on start up 


    #########Possible Methods###########
	def newData(self, filtered_msg):
		if len(filtered_msg) > 0: #only do if list has values in
			for item in filtered_msg:
				if item.msgtype == "STEP":

					if item.berth in self.state: #if berth key exists in dict delete key
						self.delTrain(item.berth)


					if item.destination not in self.state: #if new berth does not exist in dict add it
						self.addTrain(item.destination, item.train)


				elif item.msgtype == "CAN":
					if item.berth in self.state:
						self.delTrain(item.berth) #if can msg, delete train from berth


				elif item.msgtype == "INT":

					self.addTrain(item.berth, item.train)
		


	def addTrain(self, berth, train):
		self.state[berth] = train
		#print "key added-", train, berth

	def delTrain(self, berth):
		self.state.pop(berth, None)
		#print "key deleted", berth

	def getState(self):
		#sends the whole "image" of the railway
		#print self.state
		print "Berth - Train"
		for k, v in self.state.iteritems():
			
			print k, v

	def getTest(self):
		teststring = json.dumps(self.state)
		return teststring		
