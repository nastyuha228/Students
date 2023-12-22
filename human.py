from tkinter import *

class Human() :
    def __init__ (self, canvas, x, y, name):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.name = name
        
    def display(self):
        self._drawHead()
        self._drawBody()
        self._TEXT()
        self._Weapon()
        
    def _drawHead(self) :
        self.canvas.create_oval(self.x, self.y-170, self.x+100, self.y-270, width=2)

        
        self.canvas.create_arc(self.x+24, self.y-200, self.x+69, self.y-230, start=0, extent=-180, style=ARC, outline="blue", width=3)
        
        self.canvas.create_oval(self.x+60, self.y-220, self.x+75, self.y-235, width=0, fill="red")
        
        self.canvas.create_oval(self.x+15, self.y-220, self.x+30, self.y-235, width=0, fill="red")
         
        
       

    def _drawBody(self) :
        self.canvas.create_line(self.x, self.y, self.x+50, self.y-50, self.x+50, self.y-170, width=2)
 
        self.canvas.create_line(self.x, self.y-110, self.x+50, self.y-150, self.x+100, self.y-110, width=2)

        self.canvas.create_line(self.x, self.y, self.x+50, self.y-50, self.x+100, self.y, width=2)
        

        

        
    def _TEXT(self) : 
        self.canvas.create_text(self.x+50, self.y-300, 
              text=self.name,
              justify=CENTER, font="Verdana 14")
        
        
            
            
              
        
        
        
        
        
