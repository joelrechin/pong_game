from turtle import Turtle

NET_COLOR = "white"

class Net(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.color(NET_COLOR)
        self.speed("fastest")
        self.create_net(screen_height)

    def create_net(self, screen_height):
        self.penup()
        self.goto(0,screen_height/2)
        self.setheading(270)
        self.pensize(5)
        for _ in range(int(screen_height/20)):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)









