import turtle
def draw_circle(xcor,ycor,rad,filcol):
    turtle.up()
    turtle.goto(xcor,ycor)
    turtle.down()
    turtle.fillcolor(filcol)
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()
def main():
    draw_circle(0,10,50,"blue")
main()