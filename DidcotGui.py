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
      self.b0949 = Berth('0949', 30, 92)
      self.b0947 = Berth('0947', 32, 92)
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
      self.b0951 = Berth('0951', 28, 92)
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
      self.b0901 = Berth('0901', 23, 89)
      self.b0903 = Berth('0903', 19, 89)
      self.b0906 = Berth('0906', 17, 75)
      self.b0907 = Berth('0907', 19, 77)
      self.b0904 = Berth('0904', 21, 75)
      self.b0905 = Berth('0905', 23, 77)
      self.b0911 = Berth('0911', 23, 63)
      self.b0913 = Berth('0913', 19, 63)
      self.b0912 = Berth('0912', 21, 50)
      self.b0914 = Berth('0914', 19, 50)
      self.b0916 = Berth('0916', 17, 50)
      self.b0918 = Berth('0918', 15, 50)
      self.b0920 = Berth('0920', 13, 50)
      self.b0931 = Berth('0931', 23, 30)
      self.b0941 = Berth('0941', 23, 10)
      self.b0936 = Berth('0936', 23, 5)
      self.b0938 = Berth('0938', 21, 5)
      self.b0940 = Berth('0940', 19, 5)
      self.b0942 = Berth('0942', 17, 5)
      self.b0921 = Berth('0921', 19, 45)
      self.b0923 = Berth('0923', 17, 45)
      self.b0925 = Berth('0925', 15, 45)
      self.b0924 = Berth('0924', 19, 33)
      self.b0926 = Berth('0926', 17, 33)
      self.b0933 = Berth('0933', 19, 27)
      self.b0935 = Berth('0935', 17, 27)
      self.b6420 = Berth('6240', 19, 15)
      self.b0922 = Berth('0922', 3, 47)
      self.b2209 = Berth('2209', 5, 22)
      self.b2207 = Berth('2207', 6, 22)
      self.b2208 = Berth('2208', 7, 22)
      self.b2205 = Berth('2205', 9, 22)
      self.b2201 = Berth('2201', 13, 21)
      self.b0937 = Berth('0937', 15, 25)
      self.b0928 = Berth('0928', 7, 31)
      self.b2203 = Berth('2203', 9, 31)
      self.b6416 = Berth('6416', 11, 32)   
      self.b6413 = Berth('6413', 10, 45)
      self.b6411 = Berth('6411', 11, 45)
      self.b2210 = Berth('2210', 3, 13)
      self.b2211 = Berth('2211', 5, 13)
      self.b2212 = Berth('2212', 7, 5)
      self.b2214 = Berth('2214', 3, 4)

      self.berthList = [self.b1014, self.b1010, self.b1000, self.b0992, 
      self.b0986, self.b0980, self.b0976, self.b0966, self.b1005, self.b0983, self.b0965,
       self.b0952, self.b0949, self.b0947, self.b0950, self.b0963, self.b0964, self.b0973,
        self.b0977, self.b0981, self.b0984, self.b0989, self.b0993, self.b0999, self.b1003, 
        self.b1007, self.b0951, self.b0954, self.b0961, self.b0987, self.b0991, self.b0997,
        self.b1001, self.b1002, self.b0994, self.b0988, self.b1011, self.b0901, self.b0903, 
        self.b0906, self.b0907, self.b0904, self.b0905, self.b0911, self.b0931 , self.b0941,
        self.b0913, self.b0912, self.b0914, self.b0916, self.b0918, self.b0920, self.b0936, 
        self.b0938, self.b0940, self.b0942, self.b0921, self.b0923, self.b0925, self.b0924, 
        self.b0926, self.b0933, self.b0935, self.b6420, self.b0922, self.b2209,
        self.b2207, self.b2208, self.b2205, self.b2201, self.b0937, self.b0928, self.b2203,
        self.b6416, self.b6413, self.b6411, self.b2210, self.b2211, self.b2212, self.b2214]
      
      self.win = win #curses window object



    def drawBerths(self, berths):


      for key in berths.keys(): #for each key in the dict berths thats passed in
        for BTH in self.berthList: #and for each berth object in the model
          if key == BTH.berth: #but if the key in the dict matches the model berth
            BTH.setDesc(berths[key]) #set the new value


      for item in self.berthList:
        #display all new berths
        self.win.addstr(item.ypos, item.xpos, item.desc)

    def drawFixedMap(self):

      tile = '-'
      point1 = '/'
      point2 = '\\'
      vertical = '|'

      self.win.keypad(1)
      self.win.border(0)
      self.win.nodelay(1)

      self.win.addstr(0, 2, 'Didcot TD')

      #lines

      self.win.addstr(30, 1, tile * 98) #Up Main
      self.win.addstr(21, 1, tile * 98) #Up Main
      self.win.addstr(32, 1, tile * 98) #Dn Main
      self.win.addstr(23, 1, tile * 98) #Dn Main
      self.win.addstr(19, 1, tile * 98) #Dn Relief
      self.win.addstr(17, 17, tile * 82) #Up Relief
      self.win.addstr(34, 15, tile * 30) #Dn Relief Wantage
      self.win.addstr(28, 15, tile * 30) #Up Relief Wantage
      self.win.addstr(34, 74, tile * 13) #Dn Milton Loop
      self.win.addstr(28, 74, tile * 25) #Up Milton Loop
      self.win.addstr(3, 1, tile * 61) #Up Oxford / Avoider
      self.win.addstr(5, 1, tile * 57) #Dn Oxford / Avoider
      self.win.addstr(7, 20, tile * 21) #Up Chester
      self.win.addstr(9, 20, tile * 18) #Dn Chester
      self.win.addstr(15, 42, tile * 14) #P5
      self.win.addstr(13, 49, tile * 6) #Didcot Yard East Entrance
      

      #points

      self.win.addstr(29, 14, point1) #UM/UR Challow
      self.win.addstr(29, 45, point2) #UR/UM Wantage
      self.win.addstr(33, 14, point2) #DR/DM Challow
      self.win.addstr(33, 45, point1) #DM/DR Wantage
      self.win.addstr(31, 44, point1) #Reversible Wantage
      self.win.addstr(31, 45, point2) #Reversible Wantage
      self.win.addstr(29, 73, point1) #UM/UR Milton
      self.win.addstr(33, 73, point2) #DG/DM Milton
      self.win.addstr(33, 87, point1) #DM/DG Milton
      self.win.addstr(31, 88, point1) #DM/UM Milton
      self.win.addstr(29, 89, point1) #UM/UR Milton2
      self.win.addstr(20, 12, point1) #UM/UR Foxhall
      self.win.addstr(20, 20, point1) #UM/UR Foxhall
      self.win.addstr(22, 15, point1) #DM/UM Foxhall
      self.win.addstr(22, 25, point2) #DM/UM Foxhall
      self.win.addstr(18, 19, point1) #UR/UG Foxhall
      self.win.addstr(18, 22, point1) #UR/UG Foxhall
      self.win.addstr(18, 86, point1) #DR/UP Moreton Cutting
      self.win.addstr(20, 85, point1) #UM/DR Moreton Cutting
      self.win.addstr(22, 84, point1) #UM/DM Moreton Cutting
      self.win.addstr(22, 70, point2) #UM/DM Didcot East
      self.win.addstr(18, 70, point2) #UR/DR Didcot East
      self.win.addstr(20, 68, point2) #DR/UM Didcot East
      self.win.addstr(20, 72, point2) #DR/UM Didcot East
      self.win.addstr(18, 60, point2) #DR/UR Didcot East
      self.win.addstr(16, 58, point2) #DO/DR Didcot East
      self.win.addstr(16, 62, point2) #UO/UR Didcot East
      self.win.addstr(16, 56, point2) #P5/UR
      self.win.addstr(18, 38, point1) #UR/P4 Station
      self.win.addstr(14, 55, point2) #Didcot Yard East Entrance
      self.win.addstr(18, 42, point2) #P3/Down Chester
      self.win.addstr(16, 38, point2) #P4/Down Chester
      self.win.addstr(16, 42, point2) #P4/Up Chester
      self.win.addstr(15, 29, point1) #down west curve

      #vertical

      self.win.addstr(4, 62, vertical) #up avoider
      self.win.addstr(5, 62, vertical) #up avoider
      self.win.addstr(15, 38, vertical) #up chester
      self.win.addstr(15, 41, vertical) #down chester
      self.win.addstr(8, 41, vertical) #down chester
      self.win.addstr(9, 41, vertical) #down chester

      for i in range(10,15):
        self.win.addstr(i, 29, vertical)


      for i in range(6,16):
        self.win.addstr(i, 58, vertical) #down avoider
        self.win.addstr(i, 62, vertical) #up avoider

      for i in range(10,15):
        self.win.addstr(i, 38, vertical) #down chester
        self.win.addstr(i, 41, vertical) #up chester
      

      self.win.timeout(200) 
