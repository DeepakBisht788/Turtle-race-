import turtle as t
import random

screen = t.Screen()
screen.setup(height=400, width=500)
t.colormode(255)

def colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


colours = ["green", "red", "blue", "purple", "yellow", "brown"]
positions = [70, 40, 10, -20, -60, -90]
all_turtle = []

# Create turtles
for i in range(6):
    timy = t.Turtle(shape="turtle")
    timy.penup()
    timy.goto(x=-230, y=positions[i])
    timy.color(colours[i])
    all_turtle.append(timy)

# Get user bet
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color:")

# Start the race
if user_bet:
    race_on = True
else:
    race_on = False

while race_on:
    for i in all_turtle:
        if i.xcor() > 230:
            race_on = False
            winner_color = i.pencolor()
            if winner_color == user_bet:
                print("You won!")
            else:
                print("You lose!")
            break
        i.forward(random.randint(0, 10))

screen.exitonclick()
