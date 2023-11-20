#Credtis: Eric Pogue, Dr. Ray Klump, ChatGPT, Zoom meetings (for formula)

import turtle
import math

def calcDist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

print('\nTurtle Draw\n')

#Prompt the user for the name of the text file.
print('Please provide the name of the text file:\n')
txtFIleName = input()

#Open the text file.
txtFile = open(txtFIleName, 'r')

Turtle = turtle.Turtle()
turtle.screensize(canvwidth=450, canvheight=450)
Turtle.speed(0)
Turtle.penup()

#Read the lines of the text file
line = txtFile.readline()
#While loop allowing each line to be printed and interpreted    
while line:
    print(line, end='')
    line = txtFile.readline()
    #prints each line as a split list with whitespace stripped.
    comps = line.split(' ')

    if len(comps) == 3:
        color = comps[0]
        x = comps[1]
        y = comps[2]
        Turtle.color(color)
        Turtle.goto(int(x),int(y))
        Turtle.pendown()

    if len(comps) == 1:
        Turtle.penup()

Turtle.goto(25, -150)
Turtle.write("Total Distance marked:")

turtle.done()
txtFile.close

turtle.Screen().exitonclick()

