class Board:
    def __init__(self) -> None:
        self.Gameboard = ['1','2','3','4','5','6','7','8','9',]
    def draw(self):
        print("\n",self.Gameboard[0:3])
        print(len(str(self.Gameboard[0:3]))*"-")
        print(self.Gameboard[3:6])
        print(len(str(self.Gameboard[0:3]))*"-")
        print(self.Gameboard[6:9],"\n")
    def place(self,place: int,piece: str):
        if self.Gameboard[place-1] in ['1','2','3','4','5','6','7','8','9',]:
            self.Gameboard[place-1] = piece
            return True
        else: return False
    def Haswon(self) -> str:
        def check(start,inc):
            for i in range(3):
                if i == 0:
                    first = self.Gameboard[start]
                if self.Gameboard[start + i * inc ] != first:
                    return (0)
            return((1 + (ord(first) << 1))) 
        hwon=0
        for i in range(3): hwon |= check(i,3)
        for i in range(3): hwon |= check(3*i,1)
        hwon |= check(0,4)
        hwon |= check(2,2)
        ret = str(bin(hwon))
        if int(ret[-1]) == 0: return (False,)
        else: return (True,chr((hwon -1) >> 1))       
m = ["X","O"]
b = Board()
for i in range(len(b.Gameboard)):
    while True:
        b.draw() 
        if b.place(int(input(f"Player {m[i%len(m)]}: ")),m[i%len(m)]): break   
    if b.Haswon()[0]: break
print("\n"*2)
try: print(f"winner: {b.Haswon()[1]}")
except: print("Tie")