from tkinter import Tk, Canvas, ARC, SE, W
from grid import Grid
from human import Human
from student import Student
from hero import Hero
import random

root = Tk()
canvas = Canvas (root,width=800,height=800)
canvas.pack()

grid = Grid(canvas)
grid.display()

f = open('students.txt', 'r', encoding="utf-8")
students=[]
for student in f:
    s=student.split(';')
    id=int(s[0])
    n=s[1]
    v=int(s[3])
    g='ИП-21'
    gen=s[2]
    students.append({'id':id,'f_n':n, 'variant':v, 'group':g, 'gender':gen })
  
f.close()





f.close()
'''
x = random.randint(0,10)
'''
s1 = random.choice(students)
n = s1['f_n']
p1 = Hero(canvas, 100, 700,n)
p1.display()

s2 = random.choice(students)
n = s2['f_n']
p2 = Hero(canvas, 250, 600,n)
p2.display()

s3 = random.choice(students)
n = s3['f_n']
p3 = Hero(canvas, 400, 700,n)
p3.display()

s4 = random.choice(students)
n = s4['f_n']
p4 = Hero(canvas, 550, 600,n)
p4.display()






root.mainloop()









'''
canvas.create_line( 100, 110, 100,300,)#туловище

canvas.create_line( 150, 450, 100,300,)# ножки
canvas.create_line( 50, 450, 100,300,)


canvas.create_line( 100, 150, 200,200,)# ручки
canvas.create_line( 100, 150, 0,200,)

canvas.create_oval(50, 10, 150, 110, width=2)






root.mainloop'''
