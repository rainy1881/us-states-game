from turtle import Turtle, Screen


class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def game_over(self):
        self.write("Game over!")
        self.goto(0, 0)
