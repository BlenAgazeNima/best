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

   # Same code as the one written above so there is no need for smiley function

def main():
    draw_circle(0,10,50,"yellow")
    draw_centered_circle(0,47.5,10,"pink")
    draw_smiley()
main()