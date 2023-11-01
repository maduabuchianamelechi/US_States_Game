import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pd.read_csv("50_states.csv")
correct_guess = []

# check the User's guess
def check_user_guess(guess):
    '''
    :param guess:
    :returns True and the index of the state if found:
    '''
    all_states = states_data["state"].to_list()
    if guess in all_states:
        return True


# Write the state to the map
def write_state(x, y, text):
    my_turtle = turtle.Turtle()
    my_turtle.penup()
    my_turtle.hideturtle()
    my_turtle.goto(x=x, y=y)
    my_turtle.write(text)


while len(correct_guess) < 50:
    user_answer = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt="What's another state's name").title()
    if user_answer == "Exit":
        break
    guess_check = check_user_guess(user_answer)
    if guess_check:
        correct_guess.append(user_answer)
        needed_row = states_data[states_data["state"] == user_answer]
        state_x = needed_row.iloc[0][1]
        state_y = needed_row.iloc[0][2]
        write_state(text=user_answer, x=state_x, y=state_y)

# Save the states gotten wrong

