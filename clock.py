import time
import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.title("Clock")
wn.tracer(0)
#Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, m, s, pen):
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color('green')
    pen.pendown()
    pen.circle(210)

    #Lines for hour
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)

    for i in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)
    #Ghanta ka kaanta
    pen.penup()
    pen.goto(0, 0)
    pen.color('gold')
    pen.setheading(90)
    angle = (h / 12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)
    
    #Minute ka kaanta
    pen.penup()
    pen.goto(0, 0)
    pen.color('white')
    pen.setheading(90)
    angle = (m / 60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)
    
    #Second ka kaanta
    pen.penup()
    pen.goto(0, 0)
    pen.color('white')
    pen.setheading(90)
    angle = (s / 60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(65)
while True:

    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    draw_clock(h, m, s, pen)
    wn.update()
    time.sleep(1)
    pen.clear()
    

wn.mainloop()