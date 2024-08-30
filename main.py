import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
turtle_instance_2 = turtle.Turtle()
turtle_instance_2.left(180)
turtle_instance_2.forward(100)

#square

turtle_instance_3 = turtle.Turtle()

for i in range(4):
    turtle_instance_3.left(90)
    turtle_instance_3.forward(100)

turtle.done()