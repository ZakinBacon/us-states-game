from turtle import Turtle


class State_Creation(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def create_state(self, state, x_cord, y_cord):
        self.goto(x_cord, y_cord)
        self.write(str(state), True, align="center")
