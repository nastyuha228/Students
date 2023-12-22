from tkinter import *

from human import Human

class Student(Human):
    
    def __init__(self,  canvas, x, y, name, g, v):
        super().__init__( canvas, x, y, name)
        self.__g = g
        self.__v = v
        
        
    def _TEXT(self) : 
        print(self.name)
        name = f"{self.name.split()[0]} {self.name.split()[1][0]}. {self.name.split()[2][0]}."
        self.canvas.create_text(self.x+50, self.y-300, 
        text=f'{name}, {self.__g}, №{self.__v}',
        justify=CENTER, font="Verdana 14")
       
       
      