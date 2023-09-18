class Board:
    def __init__(self) -> None: self.Gameboard = ['1','2','3','4','5','6','7','8','9',]
    def draw(self): print("\n",self.Gameboard[0:3],"\n",len(str(self.Gameboard[0:3]))*"-","\n",self.Gameboard[3:6],"\n",len(str(self.Gameboard[0:3]))*"-","\n",self.Gameboard[6:9],"\n")
    def place(self,place: int,piece: str):
        if place in ("1","2","3","4","5","6","7","8","9") and self.Gameboard[int(place)-1] in ['1','2','3','4','5','6','7','8','9',] and (tra := False) == False : self.Gameboard[int(place)-1],tra = piece,True
        return tra
    def Haswon(self,hwon=0):
        def check(start,inc,defaul=0): return ((1 + (ord(self.Gameboard[0+start]) << 1))) * ( self.Gameboard[start::inc][:3].count(self.Gameboard[0+start]) == len(self.Gameboard[start::inc][:3]))
        for i in range(2): hwon |= check(i,3) | check(2-i*2,3-i*2) | check(3+i*3,1) | check(0+i*2,4-i*2)
        if (num := 0) == 0 and ((eg := (int(str(bin(hwon))[-1]))) == 0) or (num := chr((hwon -1) >> 1)): return (eg,num)
for i in range(((b := Board())==0) +len(b.Gameboard) + ((m := ["X","O"])==0)):
    while True: 
        if   b.draw() == "t" or b.place(input(f"\n\nPlayer {m[i%len(m)]}: "),m[i%len(m)]): break 
    if (won := b.Haswon())[0]: break
print(str(b.draw())*0 + f"\n\nwinner: {won[1]}"*won[0] + "\n\nTie" * (won[0] ^ 1))
