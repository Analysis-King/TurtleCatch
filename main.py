import turtle
import random

# Ekran ayarları
screen = turtle.Screen()
screen.title("Catch the Turtle!")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Oyuncu turtle'ı
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# Hedef turtle'ı
target = turtle.Turtle()
target.shape("turtle")
target.color("red")
target.penup()
target.speed(0)
target.goto(random.randint(-280, 280), random.randint(-280, 280))

# Skor
score = 0

# Hareket fonksiyonları
def go_left():
    x = player.xcor()
    x -= 20
    if x < -290:
        x = -290
    player.setx(x)

def go_right():
    x = player.xcor()
    x += 20
    if x > 290:
        x = 290
    player.setx(x)

def go_up():
    y = player.ycor()
    y += 20
    if y > 290:
        y = 290
    player.sety(y)

def go_down():
    y = player.ycor()
    y -= 20
    if y < -290:
        y = -290
    player.sety(y)

# Klavye kontrolleri
screen.listen()
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

# Oyun döngüsü
while True:
    target.goto(random.randint(-280, 280), random.randint(-280, 280))

    # Yakalama kontrolü
    if player.distance(target) < 20:
        score += 1
        print(f"Skor: {score}")
        target.goto(random.randint(-280, 280), random.randint(-280, 280))

    screen.update()

# Ekranı kapatma
turtle.done()
