import turtle
import pandas
from states import State_Creation

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Check if the guess is among the 50 States
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

state_creation = State_Creation()

# keep track of the score
score = 0
# record the correct guesses in a list
correct_guesses = []
game_on = True
# use a loop to allow the user to keep guessing
while game_on:
    answer_state = screen.textinput(title=f"Guess the State {score}/50", prompt="What's another state's name?")
    # Convert the guess to title case
    answer_state = answer_state.title()



    guess_info = data[data["state"] == answer_state]
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if guess_info.empty:
        print("incorrect")
    else:
        guess_info['state'] = guess_info['state'].astype(str)
        state = answer_state
        x_cords = int(guess_info["x"])
        y_cords = int(guess_info["y"])
        # Write correct guesses onto the map
        state_creation.create_state(state, x_cords, y_cords)
        correct_guesses.append(state)
        score += 1

    if score == 50:
        game_on = False

