from Berth import Berth

class DidcotGui(object):


    def __init__(self, win):
      self.b1014 = Berth('1014', 30, 1)
      self.b1010 = Berth('1010', 30, 7)
      self.b1000 = Berth('1000', 30, 21)
      self.b1005 = Berth('1005', 30, 15)
      self.b0992 = Berth('0992', 30, 31)
      self.b0986 = Berth('0986', 30, 40)
      self.b0983 = Berth('0983', 30, 47)
      self.b0980 = Berth('0980', 30, 52)
      self.b0976 = Berth('0976', 30, 59)
      self.b0966 = Berth('0966', 30, 68)
      self.b0965 = Berth('0965', 30, 75)
      self.b0952 = Berth('0952', 30, 82)
      self.b0949 = Berth('0949', 30, 89)
      self.b0947 = Berth('0947', 32, 89)
      self.b0950 = Berth('0950', 32, 82)
      self.b0963 = Berth('0963', 32, 75)
      self.b0964 = Berth('0964', 32, 68)
      self.b0973 = Berth('0973', 32, 63)
      self.b0977 = Berth('0977', 32, 56)
      self.b0981 = Berth('0981', 32, 47)
      self.b0984 = Berth('0984', 32, 40)
      self.b0989 = Berth('0989', 32, 33)
      self.b0993 = Berth('0993', 32, 28)
      self.b0999 = Berth('0999', 32, 22)
      self.b1003 = Berth('1003', 32, 15)
      self.b1007 = Berth('1007', 32, 7)
      self.b0951 = Berth('0951', 28, 89)
      self.b0954 = Berth('0954', 28, 82)
      self.b0961 = Berth('0961', 34, 75)
      self.b0987 = Berth('0987', 34, 33)
      self.b0991 = Berth('0991', 34, 28)
      self.b0997 = Berth('0997', 34, 22)
      self.b1001 = Berth('1001', 34, 15)
      self.b1002 = Berth('1002', 28, 21)
      self.b0994 = Berth('0994', 28, 31)
      self.b0988 = Berth('0988', 28, 40)
      self.b1011 = Berth('1011', 32, 1)

      self.berthList = [self.b1014, self.b1010, self.b1000, self.b0992, 
      self.b0986, self.b0980, self.b0976, self.b0966, self.b1005, self.b0983, self.b0965,
       self.b0952, self.b0949, self.b0947, self.b0950, self.b0963, self.b0964, self.b0973,
        self.b0977, self.b0981, self.b0984, self.b0989, self.b0993, self.b0999, self.b1003, 
        self.b1007, self.b0951, self.b0954, self.b0961, self.b0987, self.b0991, self.b0997,
        self.b1001, self.b1002, self.b0994, self.b0988, self.b1011]
      
      self.win = win #curses window object



    def drawBerths(self, berths):

      berths = berths

      for key in berths.keys(): #for each key in the dict berths thats passed in
        for BTH in self.berthList: #and for each berth object in the model
          if key == BTH.berth: #but if the key in the dict matches the model berth
            BTH.setDesc(berths[key]) #set the new value


      # sberths = str(berths) #test
      # self.win.addstr(5,5, sberths) #display raw dict for testing

      for item in self.berthList:
        #display all new berths
        self.win.addstr(item.ypos, item.xpos, item.desc)

    def drawFixedMap(self):

      self.win.keypad(1)
      self.win.border(0)
      self.win.nodelay(1)

      self.win.addstr(0, 2, 'Didcot TD')

      self.win.timeout(200) 
