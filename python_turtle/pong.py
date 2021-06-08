import turtle

score = 0

window = turtle.Screen()
window.setup(width = 450, height = 700)
window.title("Pong Single Player")
window.bgcolor("green")

#square = turtle.Turtle()

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.shapesize(1,6)
player.color("black")

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")

#variaveis de movimento da bola
movX = 5
movY = 5

#positions
player.penup()
ball.penup()
player.goto(0,300)


def player_right():
    x = player.xcor()
    x += 20
    player.setx(x)
def player_left():
    x = player.xcor()
    x -= 20
    player.setx(x)
def change_sides():
    y = player.ycor()
    player.sety(-y+10)

window.listen()
window.onkeypress(player_right, "Right")
window.onkeypress(player_left, "Left")
window.onkeypress(change_sides, "z")

while True:
    window.update
    ball.setx(ball.xcor() + movX)
    ball.sety(ball.ycor() + movY)

    if ball.xcor() > 170 or ball.xcor() < -170: movX *= -1

    if ball.ycor() > 350 or ball.ycor() < -350:
        ball.goto(0,0)
        score -= 1
    elif player.ycor() == (ball.ycor()-20) or player.ycor() == (ball.ycor()+20):
        movY *= -1
        score += 1
        
