class Board:
    def __init__(self) -> None: self.Gameboard = ['1','2','3','4','5','6','7','8','9',]
    def draw(self): print("\n",self.Gameboard[0:3],"\n",len(str(self.Gameboard[0:3]))*"-","\n",self.Gameboard[3:6],"\n",len(str(self.Gameboard[0:3]))*"-","\n",self.Gameboard[6:9],"\n")
    def place(self,place: int,piece: str):
        if place in ("1","2","3","4","5","6","7","8","9") and self.Gameboard[int(place)-1] in ['1','2','3','4','5','6','7','8','9',] and (tra := False) == False : self.Gameboard[int(place)-1],tra = piece,True
        return tra
    def Haswon(self,hwon=0):
        def check(start,inc,defaul=0): return ((1 + (ord(self.Gameboard[0+start]) << 1))) * ( self.Gameboard[start::inc][:3].count(self.Gameboard[0+start]) == len(self.Gameboard[start::inc][:3]))
        for i in range(3): hwon |= check(i,3) | check(3*i,1)
        hwon |= check(0,4) | check(2,2)
        if int(str(bin(hwon))[-1]) == 0: return (False,)
        else: return (True,chr((hwon -1) >> 1))       
for i in range(((b := Board())==0) +len(b.Gameboard) + ((m := ["X","O"])==0)):
    while True: 
        if b.draw() == "t" or b.place(input(f"\n\nPlayer {m[i%len(m)]}: "),m[i%len(m)]): break 
    if b.Haswon()[0]: break
try: h = b.draw() == print(f"\n\nwinner: {b.Haswon()[1]}")
except: h = b.draw() == print("\n\nTie")
