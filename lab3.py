# Lab No. 3
# CTEC 121
# Brielle Choquer

from graphics import *

def snowman():
    # create the graphics window
    win = GraphWin('Lab 3 - Snowman',800,800)
    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circl3
    circle1 = Circle(Point(400,650), 150)
    circle1.draw(win)

    circle2 = Circle(Point(400,400), 100)
    circle2.draw(win)

    circle3 = Circle(Point(400,220), 80)
    circle3.draw(win)

    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2
    eye1 = Circle(Point(360,220), 15)
    eye1.setFill("Black")
    eye1.draw(win)

    eye2 = eye1.clone()
    eye2.move(80, 0)
    eye2.draw(win)


    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose
    nose = Polygon(Point(390,220), Point(410,220), Point(420,260))
    nose.setFill("orange")
    nose.draw(win)




    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat
    hat = Rectangle(Point(350,65), Point(450,150))
    hat.setFill('Black')
    hat.draw(win)



    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline
    hatline = Line(Point(300,150), Point(500,150))
    hatline.draw(win)

    #ARMS!!
    arm1 = Line(Point(480,400), Point(530,300))
    arm1.draw(win)

    arm2 = Line(Point(320,400), Point(280,300))
    arm2.draw(win) 
    





    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()