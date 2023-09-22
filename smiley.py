import turtle

def draw_circle(xcor,ycor,rad,filcol):
    turtle.up()
    turtle.goto(xcor,ycor)
    turtle.down()
    turtle.fillcolor(filcol)
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()
def draw_centered_circle(xcor1,ycor1,rad1,filcoln):
    #Move the turtle up to move it to a specified location
    turtle.up()
    #Go to a specific location that will make it possible to draw a circle centered on the first circle
    turtle.goto(xcor1,ycor1)
    #After going to that location put the turtle down and start drawing
    turtle.down()
    #initiate the function that allows to fill the circle with a specific color
    turtle.fillcolor(filcoln)
    #start filling the color
    turtle.begin_fill()
    #specify the radius of the centered cicle regards to the bigger circle radius(to go to the location we need to use specified coordinate which is xcor,0.75*radius+ycor)NEW COORDINATE
    turtle.circle(rad1)
    #End the circle  by ending the color filling
    turtle.end_fill()
def tweak(tspeed,ttracer):
    #Turtle speed ranging from 1-10 (0) for fast
    turtle.speed(tspeed)
    #Turtle tracer can be either True or False. Focus on capitalization
    turtle.tracer(ttracer)
def draw_eye(xcor2,ycor2,rad2,filcole):
    turtle.up()
    turtle.goto(xcor2,ycor2)
    turtle.down()
    turtle.fillcolor(filcole)
    turtle.begin_fill()
    turtle.circle(rad2)
    turtle.end_fill()
def draw_mouth(xcor3,ycor3,rad3,fillcolm):
    turtle.up()
    turtle.goto(xcor3,ycor3)
    turtle.down()
    turtle.fillcolor(fillcolm)
    turtle.begin_fill()
    turtle.setheading(270)
    turtle.circle(rad3,180)
    turtle.setheading(180)
    turtle.forward(2*rad3)
    turtle.end_fill()
def main():
    turtle.hideturtle()
    tweak(0,True)
    draw_circle(0,5,100,"yellow")
    #The centered circle coordinates X(The same as the coordinate of the circle.Y(75%of the circle radius+the y coordinate of circle).And radius must be very smaller than the circle radius
    draw_centered_circle(0,80,15,"pink")
    #(some value must be equal to the amount of radius we decreas to draw the inner circle)
    #Draw x coordinate by using 50% of radius in negative direction and y coordinate by using radius+ y coordinate of the circle
    draw_eye(-50,105,25,"white")
    #draw the second layer x cor= x cor of circle,y cor=y cor of circle+radius+some value
    draw_eye(-50,115,15,"blue")
    #draw the third layer x cor= x cor of circle,y cor=y cor of circle+radius+some value
    draw_eye(-50,125,5,"black")
    #Draw x coordinate by using 50% of radius in positive direction and y coordinate by using radius + y coordinate of the circle
    draw_eye(50,105,25,"white")
    #draw the second layer x cor= x cor of circle,y cor=y cor of circle+radius+some value
    draw_eye(50,115,15,"blue")
    #draw the third layer x cor= x cor of circle,y cor=y cor of circle+radius+some value
    draw_eye(50,125,5,"black")
    # x cor = to the negative direction 25% of radius(as we are moving 25%, radius must be 1/4 of radius of circle )  , ycor=50% of radius of circle+y cor of the circle
    draw_mouth(-25,55,25,"Black")
    input("Continue")
main()