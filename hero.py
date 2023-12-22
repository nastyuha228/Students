from tkinter import Tk, Canvas, ARC, W, CENTER
from human import Human

class Hero(Human):
    
    def __init__(self,canvas,x,y,n):
        super().__init__(canvas,x,y,n)
        self._health = 100
        
    def _TEXT(self) : 
        print(self.name)
        name = f"{self.name.split()[0]} {self.name.split()[1][0]}. {self.name.split()[2][0]}."
        self.canvas.create_text(self.x+50, self.y-300, 
        text=f'{name}',
        justify=CENTER, font="Verdana 14")
        self.canvas.create_line(self.x, self.y-350, self.x+100, self.y-350, width=10, fill="green")
    def _Weapon(self) :
        self.canvas.create_line(self.x, self.y-110, self.x+50, self.y-150, width=2)