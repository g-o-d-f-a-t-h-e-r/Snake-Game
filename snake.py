# Simple Snake Game
# By funwithcodes

# Part 1 : Set up the Screen.
# Part 2 : Create Snake Head and make a function to move the head.
# Part 3 : Create FOOD for the snake.
# Part 4 : Create the body of the snake.
# Part 5 : Solve the collisions of the snake with border,[Line: 99-104].
# Part 6 : Game reset for  Body Collisions.
# Part 7 : Set the Score Board.


import turtle
import time
import random

delay = 0.06
score = 0
high_score = 0

# Part 1 : Set up the screen ---------------------------------------
wn = turtle.Screen()
wn.title('Snake Game by funwithcodes')
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0)        # This turn off the screen updates.
# -------------------------------------------------------------------




# Part 2 : Create Snake Head and funcion for movement----------------
head = turtle.Turtle()
head.speed(0)    # animation speed of Turtle module
head.shape('square')
head.color('white')
head.penup()
head.goto(0,0)
head.direction = 'Stop'

# Funcitons

def go_Up():
    if head.direction != 'Down':
        head.direction = 'Up'
def go_Down():
    if head.direction != 'Up':
        head.direction = 'Down'
def go_Left():
    if head.direction != 'Right':
        head.direction = 'Left'
def go_Right():
    if head.direction != 'Left':
        head.direction = 'Right'
def go_Stop():
    head.direction = 'Stop'

def move():
    if head.direction == 'Up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'Down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'Left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'Right':
        x = head.xcor()
        head.setx(x + 20)

# Keyboard Bindings

wn.listen()
wn.onkeypress(go_Up,'Up')
wn.onkeypress(go_Down,'Down')
wn.onkeypress(go_Left,'Left')
wn.onkeypress(go_Right,'Right')
wn.onkeypress(go_Stop,'x')
# -------------------------------------------------------------------






#  Part 3 : Create FOOD for the Snake -------------------------------
food= turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)
# -------------------------------------------------------------------


# Create the BODY of the SNAKE -------------------------------------
segments = []
# ------------------------------------------------------------------


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0   High Score:0   RESET-Press X", align="center", font=("Courier", 18, "normal"))


# Main Game LOOP
while True:
    wn.update()

    # ---------------------------------------------------------------
    # Part 5 : Check for collision of snake with border.
    if head.xcor()>300:
        head.goto(-head.xcor()+10,head.ycor())
    elif head.xcor()<-290:
        head.goto(-head.xcor(),head.ycor())
    elif head.ycor()>230:
        head.goto(head.xcor(),-head.ycor()-70)

    elif head.ycor()<-300:
        head.goto(head.xcor(),-head.ycor()-90)
    # ---------------------------------------------------------------


    if head.distance(food) < 20:   # Check for the collision of snake with food

        # Move the food to the random part of the screen
        x = random.randint(-280, 280)
        y = random.randint(-280, 230)
        food.goto(x,y)


        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)

        # Increment the Score
        score+=10
        if score == 100:
            delay=0.05
        elif score == 200:
            delay=0.04
        elif score == 300:
            delay=0.03
        elif score == 400:
            delay = 0.02
        elif score == 500:
            delay = 0.01


        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score:{}  High Score:{}  RESET-Press X".format(score,high_score), align="center", font=("Courier", 18, "normal"))



    # Move the end segment 1st in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        # head.shape('circle')
        segments[0].goto(x,y)

    move()


    # -------------------------------------------------------------
    # Part 6 : Check for the head collisions with body segments.

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction='Stop'


            # Hide the segments.
            for segment in segments:
                segment.hideturtle()

            # clear the segment
            segments.clear()
            # RESET THE SCORE TO 0 AFTER COLLIDING WITH THE BODY SEGMENTS
            score=0
            delay=0.06
            pen.clear()
            pen.write("Score:{}  High Score:{}  RESET-Press X".format(score, high_score), align="center",
                      font=("Courier", 18, "normal"))


    # -------------------------------------------------------------


    time.sleep(delay)

wn.mainloop()