#!/usr/bin/env python
#Message filter for Didcot, takes a Dictionary and filters TD Step/Can/Interpose messages

from Msgs import StepMsg, IntMsg, CanMsg

class MessageFilter(object):

	def __init__(self):

		self.msg = []


	def filter(self, unfiltered_msg):

		self.msg = unfiltered_msg

		filtered = []

		for item in self.msg:

			if "CA_MSG" in item:

				if item['CA_MSG']['area_id'] == "D5": #filter for Didcot IECC

					train = item['CA_MSG']['descr']
					start = item['CA_MSG']['from']
					destination = item['CA_MSG']['to']

					#print "Step", train, start, destination

					o = StepMsg(train, start, destination) #new msg object

					filtered.append(o) # add to filtered list

			elif "CB_MSG" in item:

				if item['CB_MSG']['area_id'] == "D5":

					train = item['CB_MSG']['descr']
					berth = item ['CB_MSG']['from']

					#print "Cancel", train, berth

					o = CanMsg(train, berth)
					filtered.append(o)

			elif "CC_MSG" in item:

				if item['CC_MSG']['area_id'] == "D5":

					train = item['CC_MSG']['descr']
					berth = item['CC_MSG']['to']

					#print "Interpose", train, berth

					o = IntMsg(train, berth)
					filtered.append(o)

		return filtered #returns a filtered list of msg objects

