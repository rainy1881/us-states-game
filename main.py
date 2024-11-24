import pandas
from turtle import Turtle, Screen
from text import Text

turtle = Turtle()
screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
text = Text()
title_score = 0
text.hideturtle()
text.penup()

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
x_cor = data["x"].to_list()
y_cor = data["y"].to_list()

answered_states = []

high_score = 0


game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="Give me a state name!: ").title()

    if answer_state == "Q" or answer_state == "q":
        missing_states = [state for state in states if state not in answered_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        if answer_state not in answered_states:
            title_score += 1
            answered_states.append(answer_state)
            state_index = states.index(answer_state)
            x = x_cor[state_index]
            y = y_cor[state_index]

            text.goto(x, y)
            text.write(answer_state)

        screen.title(f"U.S States Game {title_score}/50")
        if title_score == 50:
            text.game_over()
            game_is_on = False

    else:
        pass

