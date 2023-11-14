import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# create screen object and set screen size and turn off automatic screen update
screen = Screen()
screen.setup(width=600, height=600)
screen.title("CrossyTurtle")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# set screen to listen for events
screen.listen()
# move turtle up when "Up" button is pressed
screen.onkey(player.go_up, "Up")

# keep looping while player hasn't lost
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create new car
    car_manager.create_car()
    # move all cars
    car_manager.move_cars()

    # detect collision between player and cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            # switch to end game
            game_is_on = False
            scoreboard.game_over()

    # detect if player passed level
    if player.level_passed():
        # reset position
        player.goto(0, -280)
        # increase car speed
        car_manager.level_up()
        # update scoreboard
        scoreboard.increase_level()


# exit screen after click
screen.exitonclick()
