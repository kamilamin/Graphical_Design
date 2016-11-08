import turtle

def drawsquare(some_turtle):
    for i in range (1,5):
      some_turtle.forward(100)
      some_turtle.right(90)

def drawsart():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.speed(5)
    brad.shape("turtle")
    brad.color("blue")
    for i in range(1,36):
        drawsquare(brad)
        brad.right(10)
drawsart()
