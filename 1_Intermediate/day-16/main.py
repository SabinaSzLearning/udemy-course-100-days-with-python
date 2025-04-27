# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("Blue")
# timmy.forward(25)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon",["a1","a2","a4"])
table.add_column("Type",["a1","a2","a4"])
table.align = "l"
print(table)