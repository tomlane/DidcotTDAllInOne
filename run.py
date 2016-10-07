#!/usr/bin/env python
from NRListener import Listener
from MessageFilter import MessageFilter
from StateModel import StateModel
from DidcotGui import DidcotGui

from Berth import Berth

import stomp
import curses
import userconfig


mf = MessageFilter()
sm = StateModel()
mq = stomp.Connection(host_and_ports=[('datafeeds.networkrail.co.uk', 61618)],
                      keepalive=True,
                      vhost='datafeeds.networkrail.co.uk',
                      heartbeats=(5000, 20000)) #<------this value may need changing soon
lst = Listener(mq)
mq.set_listener('', lst)
mq.start()
mq.connect(username=userconfig.NETWORK_RAIL_AUTH[0],
           passcode=userconfig.NETWORK_RAIL_AUTH[1],
           wait=True)
#area to recieve didcot messages
mq.subscribe('/topic/TD_WWC_SIG_AREA', 'data', ack='client-individual')

curses.initscr()
curses.noecho()
curses.curs_set(0)
win = curses.newwin(40, 100, 0, 0)

gui = DidcotGui(win)


key = ''

gui.drawFixedMap()
    
while key != 27:   # While Esc key is not pressed
         
    event = win.getch()

    #get unfiltered message from queue
    unfiltered_msg = lst.msg
    #filter messages for didcot
    filtered_msg = mf.filter(unfiltered_msg)
    #pass messages and update state of railway
    sm.newData(filtered_msg)

    
    #get messages from state of the railway and send it to Didcotgui
    #then get didcotgui to update screen

    win.addstr(7,1, sm.getTest()) #<-- test dump


    gui.drawFixedMap() #<- this might come out


    key = key if event == -1 else event



    
curses.endwin()

