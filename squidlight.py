
from gpsDistance import *
from getVehicleLatLon import *
import turtle #importing turtle graphics to make Traffic Light
import time #importing time for sleep function


winobj=turtle.Screen()
winobj.title("SquidLights by Group 4")
winobj.bgcolor("black")

class TrafficLight():
    #Drawing a Traffic Light Box and its lights
    def __init__(self,x,y):
        self.pen=turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.goto(x-50,y+150)
        self.pen.pendown()
        self.pen.fd(60) 
        self.pen.rt(90) 
        self.pen.fd(150) 
        self.pen.rt(90)
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(150)

        self.color=""

        self.redLight=turtle.Turtle()
        self.yellowLight=turtle.Turtle()
        self.greenLight=turtle.Turtle()

        self.redLight.speed(0)
        self.yellowLight.speed(0)
        self.greenLight.speed(0)

        self.redLight.color('grey')
        self.yellowLight.color('grey')
        self.greenLight.color('grey')

        self.redLight.shape('circle')
        self.yellowLight.shape('circle')
        self.greenLight.shape('circle')

        self.redLight.shapesize(1,1,15)
        self.yellowLight.shapesize(1,1,15)
        self.greenLight.shapesize(1,1,15)

        self.redLight.penup()
        self.yellowLight.penup()
        self.greenLight.penup()

        self.redLight.goto(x-20,y+120)
        self.yellowLight.goto(x-20,y+75)
        self.greenLight.goto(x-20,y+30)

    def changetoRed(self): #changes the Red light to Red
        self.redLight.color('red')
        self.yellowLight.color('grey')
        self.greenLight.color('grey')

    def changetoYellow(self): #changes the Yellow Light to Yellow
        self.redLight.color('grey')
        self.yellowLight.color('yellow')
        self.greenLight.color('grey')
    
    def changetoGreen(self): #changes the Green Light to Green
        self.redLight.color('grey')
        self.yellowLight.color('grey')
        self.greenLight.color('green')
            
#Making three Lights for the Intersection
tl1=TrafficLight(-200,0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-280,-50)
turtle.color("white")
turtle.write("Traffic Light 1",font=("Times New Roman",15,"bold"))
turtle.hideturtle()
turtle.goto(-360,-100)
turtle.write("Hurstville to Allawah",font=("Times New Roman",15,"bold"))

tl2=TrafficLight(0,0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-100,-50)
turtle.color("white")
turtle.write("Traffic Light 2",font=("Times New Roman",15,"bold"))
turtle.hideturtle()
turtle.goto(-100,-100)
turtle.write("Allawah to Hurstville",font=("Times New Roman",15,"bold"))


tl3=TrafficLight(200,0)
turtle.hideturtle()
turtle.penup()
turtle.goto(100,-50)
turtle.color("white")
turtle.write("Traffic Light 3",font=("Times New Roman",15,"bold"))
turtle.hideturtle()
turtle.goto(100,-100)
turtle.write("From The Avenue",font=("Times New Roman",15,"bold"))





# PriorityTimer
while True:
    vehicle=VehicleLatLon()
    if distancetoLight(float(vehicle[0]),float(vehicle[1]))>20: #Priority Timer
        tl3.changetoGreen()
        time.sleep(10)
        tl3.changetoYellow()
        time.sleep(2)
        tl3.changetoRed()
        tl1.changetoGreen()
        tl2.changetoGreen()
        time.sleep(4)
        tl1.changetoYellow()
        time.sleep(2)
        tl1.changetoRed()
        time.sleep(2)
        tl2.changetoYellow()
        time.sleep(2)
        tl2.changetoRed()
    else: #Normal Timer
        tl1.changetoGreen()
        tl2.changetoGreen()
        time.sleep(4)
        tl1.changetoYellow()
        time.sleep(2)
        tl1.changetoRed()
        time.sleep(2)
        tl2.changetoYellow()
        time.sleep(2)
        tl2.changetoRed()
        tl3.changetoGreen()
        time.sleep(4)
        tl3.changetoYellow()
        time.sleep(2)
        tl3.changetoRed()

winobj.mainloop() #to keep the window open