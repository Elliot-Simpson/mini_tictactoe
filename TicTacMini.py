class Board:
    def __init__(self): self.Gameboard,self.plist = ['1','2','3','4','5','6','&','8','9',],["X","O"]
    draw,place,pcount = lambda self : print("\n",self.Gameboard[0:3],"\n",len(str(self.Gameboard[0:3]))*"-","\n",self.Gameboard[3:6],"\n",len(str(self.Gameboard[0:3]))*"-","\n",self.Gameboard[6:9],"\n"), lambda self,where,piece : where in ("1","2","3","4","5","6","7","8","9") and self.Gameboard[int(where)-1] in ['1','2','3','4','5','6','7','8','9',] and self.Gameboard.pop(int(where)-1) != None  and self.Gameboard.insert(int(where)-1,piece) == None, lambda self: self.Gameboard.count("X") + self.Gameboard.count("O")
    def Haswon(self,hwon=0):
        def check(start,inc): return ((1 + (ord(self.Gameboard[0+start]) << 1))) * ( self.Gameboard[start::inc][:3].count(self.Gameboard[0+start]) == len(self.Gameboard[start::inc][:3]))
        for i in range(2): hwon |= check(i,3) | check(2-i*2,3-i*2) | check(3+i*3,1) | check(0+i*2,4-i*2)
        if (num := 0) == 0 and ((eg := (int(str(bin(hwon))[-1]))) == 0) or (num := chr((hwon -1) >> 1)): return (eg,num)
b = Board()
while b.draw() == None and (won := b.Haswon())[0] == 0 and b.pcount() != 9: print(b.place(input(f"\n\nPlayer { b.plist[b.pcount()%len(b.plist)] }: "),b.plist[b.pcount()%len(b.plist)]))
print(str(b.draw())*0 + f"\n\nwinner: {(won:=b.Haswon())[1]}"*won[0] + "\n\nTie" * (won[0] ^ 1))
