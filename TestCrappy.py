import turtle
import os

#The window and input names
window = turtle.Screen()
window.title("Crappy Footfootball")
#window.bgcolor("black") #Chobi load na hoile
screen_width = 960
screen_length = 540
hscreen_width = 960/2
hscreen_length = 540/2
window.setup(screen_width, screen_length)
window.bgpic("CrpF.png")
Spaceship_1= window.textinput("Spaceship_1", " First player : ")
Spaceship_2=window.textinput("Spaceship_2", " Second player : ")
window.tracer(0)  #Keeps window from updating so main loop e nijera korbo.
window.bgpic("bg_space.png")


#Score
score_G1 = 0
score_G2 = 0


# Football, The Ball
football = turtle.Turtle()
football.speed(9)
window.addshape('fball.gif')
football.shape('fball.gif')
#football.color("white")
football.penup()
football.goto(0, 0)
football.dx = .5
football.dy = .4


#Showing Scores
show_scores = turtle.Turtle()
show_scores.speed(0)
show_scores.shape("square")
show_scores.color("white")
show_scores.penup()
show_scores.hideturtle()
show_scores.goto(0, 240)
show_scores.write("Get Ready, {} , {} ".format(Spaceship_1, Spaceship_2), align='center', font=('Courier', 24, 'bold'))


#Spaceship 1
Spaceship_1 = turtle.Turtle()
Spaceship_1.speed(9)
Spaceship_1.shape("square")
Spaceship_1.color("brown")
Spaceship_1.shapesize(stretch_wid=5,stretch_len=0.7)
Spaceship_1.penup()
Spaceship_1.goto(-hscreen_width+50, 0)


#Spaceship 2
Spaceship_2 = turtle.Turtle()
Spaceship_2.speed(9)
Spaceship_2.shape("square")
Spaceship_2.color("blue")
Spaceship_2.shapesize(stretch_wid=5,stretch_len=0.7)
Spaceship_2.penup()
Spaceship_2.goto(hscreen_width-50, 0)


# Functions
def Spaceship_1_up():
    y = Spaceship_1.ycor()
    y += 35
    Spaceship_1.sety(y)

def Spaceship_1_dowindow():
    y = Spaceship_1.ycor()
    y -= 35
    Spaceship_1.sety(y)

def Spaceship_2_up():
    y = Spaceship_2.ycor()
    y += 35
    Spaceship_2.sety(y)

def Spaceship_2_dowindow():
    y = Spaceship_2.ycor()
    y -= 35
    Spaceship_2.sety(y)


# Keyboard bindings
window.listen()
window.onkeypress(Spaceship_1_up, "w")
window.onkeypress(Spaceship_1_dowindow, "s")
window.onkeypress(Spaceship_2_up, "Up")
window.onkeypress(Spaceship_2_dowindow, "Down")


# Game loop
while True:
    window.update()

    # Move the football
    football.setx(football.xcor() + football.dx)
    football.sety(football.ycor() + football.dy)

    # Border checking

    # Top and bottom
    if football.ycor() > hscreen_length-15:
        football.sety(hscreen_length-15)
        football.dy *= -1
        os.system("afplay Jump.wav&")

    elif football.ycor() < -hscreen_length+15:
        football.sety(-hscreen_length+15)
        football.dy *= -1
        os.system("afplay Jump.wav&")

    # Left and right
    if football.xcor() > hscreen_width-50:
        score_G1 += 1
        show_scores.clear()
        show_scores.write(" {} : {}  VS {} : {} ".format(Spaceship_1, score_G1, Spaceship_2, score_G2), align='center', font=('Courier', 24, 'bold'))
        football.goto(0, 0)
        football.dx *= -1

    elif football.xcor() < -hscreen_width+50:
        score_G2 += 1
        show_scores.clear()
        show_scores.write(" {} : {}  VS {} : {} ".format(Spaceship_1, score_G1, Spaceship_2, score_G2), align='center', font=('Courier', 24, 'bold'))
        football.goto(0, 0)
        football.dx *= -1

    # Paddle and football collisions
    if football.xcor() < -hscreen_width+60 and football.ycor() < Spaceship_1.ycor() + 50 and football.ycor() > Spaceship_1.ycor() - 50:
        football.dx *= -1
        os.system("afplay Jump.wav&")

    elif football.xcor() > hscreen_width-60 and football.ycor() < Spaceship_2.ycor() + 50 and football.ycor() > Spaceship_2.ycor() - 50:
        football.dx *= -1
        os.system("afplay Jump.wav&")
