import math
import turtle
import random
import time
import os

turtle.tracer(False)
turtle.setundobuffer(None)

turtle.shape("square")
turtle.pu()

count = 0

players = []

tag_count = turtle.clone()
tag_count.hideturtle()
tag_count.goto(-290,300)

class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self, shape="square")
        self.pu()
        self.color("red")
        self.speed = random.randint(70,130)/100.0
        self.move = True

for i in range(5):

    t = Player()
    players.append(t)

tags = 0

start_time = time.time()

def left():

    turtle.goto(turtle.xcor()-10,turtle.ycor())

def right():

    turtle.goto(turtle.xcor()+10,turtle.ycor())

def up():

    turtle.goto(turtle.xcor(),turtle.ycor()+10)

def down():

    turtle.goto(turtle.xcor(),turtle.ycor()-10)

turtle.onkey(left, "Left")
turtle.onkey(right,"Right")
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")

turtle.listen()

go = True

while(go):

    for t in players:

        t.right(math.sin(count)*5)
        t.right(random.randint(-1,1))
        t.forward(t.speed)
            
        if abs(t.xcor()) > 300:
            t.right(45)

        if abs(t.ycor()) > 300:
            t.right(45)

        if abs(t.xcor()) > 400 or abs(t.ycor()) > 400:
            t.goto(0,0)
            
        turtle.setheading(turtle.towards(t.pos()))
        turtle.forward(0.4)

        if turtle.xcor() > 300:
            turtle.goto(-300, turtle.ycor())

        if turtle.xcor() < -300:
            turtle.goto(300, turtle.ycor())

        if turtle.ycor() > 300:
            turtle.goto(turtle.xcor(), -300)

        if turtle.ycor() < -300:
            turtle.goto(turtle.xcor(), 300)

        if count > 100:
            if abs(t.xcor() - turtle.xcor()) < 10 and abs(t.ycor() - turtle.ycor()) < 10:

                turtle.forward(-10)
                t.forward(5)
                tags += 1
                tag_count.clear()
                os.popen("say tag")
                tag_count.write("tags : " + str(tags) + "\n time : " + str(int(elapsed)) + " seconds", font=("Arial", 16, "bold"), align="left")
                if t.color()[0] == "red":
                    t.color("blue")
                    t.speed = t.speed / 2.0
                else:
                    t.color("red")
                    t.speed = t.speed * 2.0
        
    count+= 1

    curr_time = time.time()
    elapsed = curr_time - start_time
       

    if elapsed > 60:

        os.popen("say " + "You had " + str(tags) + " tags in 60 seconds")
        
        go = False
        tag_count.clear()
        tag_count.write("tags : " + str(tags) + "\n time : " + str(int(elapsed)) + " seconds", font=("Arial", 16, "bold"), align="left")
    else:
        turtle.update()

turtle.mainloop()
