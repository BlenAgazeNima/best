import turtle
def draw_circle(xcor,ycor,rad,filcol):
    turtle.up()
    turtle.goto(xcor,ycor)
    turtle.down()
    turtle.fillcolor(filcol)
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()
def draw_centered_circle(xcor1,ycor1,rad1,filcol1):
    turtle.up()
    turtle.goto(xcor1,ycor1)
    turtle.down()
    turtle.fillcolor(filcol1)
    turtle.begin_fill()
    turtle.circle(rad1)
    turtle.end_fill()

def main():
    draw_circle(0,10,50,"blue")
    draw_centered_circle(0,47.5,10,"yellow")
main()