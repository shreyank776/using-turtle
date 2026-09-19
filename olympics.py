from datetime import datetime
import turtle
import draw_USA_flag
import print_me_first

program_filename = "olympics.py"
print_me_first.print_me_first(program_filename)

#This sets up the screen
screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.title("Lab 7 - Olympics")
screen.bgpic("usa.png")

#Draws the title "USA OLYMPIC TEAM" at the top of the screen
t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()
t.color("blue")
t.goto(0, 240)
t.write("USA", align="center", font=("Helvetica", 60, "bold"))
t.goto(0, 170)
t.write("OLYMPIC TEAM", align="center", font=("Helvetica", 60, "bold"))

#Draws the USA flag using the draw_USA_flag module
draw_USA_flag.draw_USA_flag()

#Draw the Olympic rings using turtle graphics
def drawCircle(x, y, color):
    ring = turtle.Turtle()
    ring.speed(0)
    ring.penup()
    ring.goto(x, y)
    ring.pendown()
    ring.color(color)
    ring.width(8)
    ring.circle(55)
    ring.hideturtle()

# Top Row: Blue, black, and red
drawCircle(-130, -210, "blue")
drawCircle(0, -210, "black")
drawCircle(130, -210, "red")

# Bottom Row: Yellow and green
drawCircle(-65, -265, "yellow")
drawCircle(65, -265, "green")

#Print my name, program, and the current time
info_turtle = turtle.Turtle()
info_turtle.speed(0)
info_turtle.penup()
info_turtle.hideturtle()
info_turtle.color("blue")
current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

labels = [
    ("Name", "Shreyank Kamatala"),
    ("Program", program_filename),
    ("Current Time", current_time_str)
]

start_y = -290
for label, value in labels:
    info_turtle.goto(210, start_y)
    info_turtle.write(label, align="left", font=("Arial", 9, "bold"))
    info_turtle.goto(295, start_y)
    info_turtle.write(":", align="left", font=("Arial", 9, "bold"))
    info_turtle.goto(305, start_y)
    info_turtle.write(value, align="left", font=("Arial", 9, "bold"))
    start_y -= 15

turtle.done()
