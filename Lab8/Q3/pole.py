import turtle

class Pole:
    def __init__(self,name="",xpos=0,ypos=0,thick=10,length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        turtle.lt(90)
        turtle.penup()
        turtle.goto(self.pxpos,self.pypos)
        turtle.pendown()
        turtle.rt(90)
        for x in range(2):
            turtle.fd(self.pthick/2)
            turtle.lt(90)
            turtle.fd(self.plength)
            turtle.lt(90)
            turtle.fd(self.pthick/2)

    def pushdisk(self,disk):
        disk.newpos(self.pxpos,self.toppos)
        disk.showdisk()
        self.stack.append(disk)
        self.toppos += disk.dheight
        self.toppos += 1


    def popdisk(self):
        d = self.stack.pop()
        d.cleardisk()
        self.toppos -= 1
        self.toppos -= d.dheight
        return d