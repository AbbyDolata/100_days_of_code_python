import turtle
tommy = turtle.Turtle()
print(tommy)
tommy.shape("turtle")
#changes shape into a turtle

tommy.color("coral")
#changes the color of object tommy the turtle

tommy.forward(100)
#moves tommy forward by 100 paces
my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
#allows program to continue running until you click on the screen

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
