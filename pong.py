import turtle

# Window
window = turtle.Screen()
window.title("Pong by Erick Navarro")
window.bgcolor("black")
window.setup(width=800,height=450)
window.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Score
score_a = 0
score_b = 0

# Scoreboard
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, window.window_height()/2 - 60)
score.write("Player A: 0               Player B: 0", align="center", font=("Times New Roman", 20, "bold"))


# Move Functions
def paddle_a_up():
    paddle_a.sety(paddle_a.ycor() + 20)

def paddle_a_down():
    paddle_a.sety(paddle_a.ycor() - 20)

def paddle_b_up():
    paddle_b.sety(paddle_b.ycor() + 20)

def paddle_b_down():
    paddle_b.sety(paddle_b.ycor() - 20)

# Variables
window.border_hor = window.window_height()/2-15
window.border_ver = window.window_width()/2-15

# Keyword
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "i")
window.onkeypress(paddle_b_down, "k")

# Main Game Loop
while True:
    window.update()

    # Ball Moving
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.xcor() >= window.border_ver:
        ball.dx *= -1
        ball.goto(0,0)
        score_a += 1
        score.clear()
        score.write("Player A: {}               Player B: {}".format(score_a, score_b), align="center", font=("Times New Roman", 20, "bold"))
    if ball.xcor() <= -window.border_ver:
        ball.dx *= -1
        ball.goto(0,0)
        score_b += 1
        score.clear()
        score.write("Player A: {}               Player B: {}".format(score_a, score_b), align="center", font=("Times New Roman", 20, "bold"))
    if abs(ball.ycor()) >= window.border_hor: ball.dy *= -1

    # Paddle & Ball Collision
    if (ball.xcor() >= paddle_a.xcor()-10 and ball.xcor() <= paddle_a.xcor()-9) and (ball.ycor() >= paddle_a.ycor()-50 and ball.ycor() <= paddle_a.ycor()+50):
        ball.dx *= -1
    if (ball.xcor() >= paddle_b.xcor()-10 and ball.xcor() <= paddle_b.xcor()-9) and (ball.ycor() >= paddle_b.ycor()-50 and ball.ycor() <= paddle_b.ycor()+50):
        ball.dx *= -1