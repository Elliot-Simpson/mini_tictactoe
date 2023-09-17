class Board:
    def __init__(self) -> None: self.Gameboard = ['1','2','3','4','5','6','7','8','9',]
    def draw(self): print("\n",self.Gameboard[0:3],"\n",len(str(self.Gameboard[0:3]))*"-","\n",self.Gameboard[3:6],"\n",len(str(self.Gameboard[0:3]))*"-","\n",self.Gameboard[6:9],"\n")
    def place(self,place: int,piece: str):
        if place in ("1","2","3","4","5","6","7","8","9") and self.Gameboard[int(place)-1] in ['1','2','3','4','5','6','7','8','9',]:
            self.Gameboard[int(place)-1] = piece
            return True
        else: return False
    def Haswon(self,hwon=0) -> str:
        def check(start,inc):
            if self.Gameboard[start::inc][:3].count(self.Gameboard[0+start]) != len(self.Gameboard[start::inc][:3]): return 0 
            return((1 + (ord(self.Gameboard[0+start]) << 1))) 
        for i in range(3): hwon |= check(i,3) | check(3*i,1)
        hwon |= check(0,4) | check(2,2)
        if int(str(bin(hwon))[-1]) == 0: return (False,)
        else: return (True,chr((hwon -1) >> 1))       
m,b = ["X","O"],Board()
for i in range(len(b.Gameboard)):
    while True: 
        if b.draw() == "t" or b.place(input(f"\n\nPlayer {m[i%len(m)]}: "),m[i%len(m)]): break 
    if b.Haswon()[0]: break
try: h = b.draw() == print(f"\n\nwinner: {b.Haswon()[1]}")
except: h = b.draw() == print("\n\nTie")
