import turtle
import time
import random

hiz = 0.10

screen = turtle.Screen()
screen_title = turtle.title("snake game")
screen.bgcolor("lightgreen")
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 0)
food.shapesize(0.80, 0.80)

tails = []
score = 0

write = turtle.Turtle()
write.speed(0)
write.shape("square")
write.color("white")
write.penup()
write.goto(0, 260)
write.hideturtle()
write.write(f"score:{score}", align="center", font=("Courier", 24, "normal"))



def move():
    if head.direction == "Up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "Down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "Right":
        x = head.xcor()
        head.setx(x+20)
    if head.direction == "Left":
        x = head.xcor()
        head.setx(x-20)

def go_up():
    if head.direction != "Down":
        head.direction = "Up"
def go_down():
    if head.direction != "Up":
        head.direction = "Down"
def go_right():
    if head.direction != "Left":
        head.direction = "Right"
def go_left():
    if head.direction != "Right":
        head.direction = "Left"

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")



while True:
    screen.update()

    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor()<-300:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for tail in tails:
            tail.goto(1000, 1000)

        tails = []
        score = 0
        write.clear()
        write.write(f"puan:{score}", align="center", font=("Courier", 24, "normal"))

        hiz = 0.10



    if head.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)

        score = score + 10
        write.clear()
        write.write(f"puan:{score}", align="center", font=("Courier", 24, "normal"))


        hiz = hiz - 0.0001

        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.color("white")
        new_tail.penup()
        tails.append(new_tail)

    for i in range(len(tails) - 1, 0, -1):
            x = tails[i - 1].xcor()
            y = tails[i - 1].ycor()
            tails[i].goto(x, y)

    if len (tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x, y)

    move()
    time.sleep(hiz)



