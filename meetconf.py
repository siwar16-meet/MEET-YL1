import turtle
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(300,300)
turtle.pendown()
turtle.goto(300,-300)
turtle.goto(-300,-300)
turtle.goto(-300,300)
turtle.goto(300,300)
turtle.penup()
def draw_menu_bar_square(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x,y+50)
    turtle.goto(x+50,y+50)
    turtle.goto(x+50,y)
    turtle.goto(x,y)
    turtle.penup()

for number in range(100, 300, 50):
    draw_menu_bar_square(250, number)

turtle.penup()
turtle.goto(260,260)
turtle.pendown()
turtle.goto(260,290)
turtle.goto(290,290)
turtle.goto(290,260)
turtle.goto(260,260)
turtle.penup()
turtle.goto(275,210)
turtle.pendown()
turtle.circle(15)
turtle.penup()
turtle.goto(250,150)
turtle.color("red")
turtle.begin_fill()
draw_menu_bar_square(250,150)
turtle.end_fill()
turtle.goto(250,100)
turtle.color("green")
turtle.begin_fill()
draw_menu_bar_square(250,100)
turtle.end_fill()
s=0
c=0
r=0
g=0
def add1():
    s+1

def add2():
    c+1

def add3():
    r+1

def add4():
    g+1

turtle.getscreen().onkeypress(add1,"s")
turtle.getscreeb().onkeypress(add2,"c")
turtle.getscreen().onkeypress(add3,"r")
turtle.getscreeb().onkeypress(add4,"g")

spc=0
def add5():
    spc+1

turtle.getscreen().onkeypress(add5,"space")

def draw_square(x,y):
    turtle.penup()
    turtle.goto(x-15,y,15)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x-15,y+15)
    turtle.goto(x+15,y+15)
    turtle.goto(x+15,y-15)
    turtle.goto(x-15,y-15)
    turtle.end_fill()
    turtle.penup()

def draw_circle():
    turtle.penup()
    turtle.goto(x,y-15)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.penup()
    turtle.end_fill()

if s>0 and r>0:
    turtle.color("red")
    turtle.onscreenclick(draw_square, btn=1, add=True)
    turtle.getscreen().onkeypress(add1,"s")
    turtle.getscreen().onkeypress(add2,"c")
    turtle.getscreeb().onkeypress(add3,"r")
    turtle.getscreen().onkeypress(add4,"g")
    turtle.getscreen().onkeypress(add5,"space")

elif s>0 and g>0:
    turtle.color("green")
    turtle.onscreenclick(draw_square, btn=1, add=True)
    turtle.getscreen().onkeypress(add1,"s")
    turtle.getscreen().onkeypress(add2,"c")
    turtle.getscreeb().onkeypress(add3,"r")
    turtle.getscreen().onkeypress(add4,"g")
    turtle.getscreen().onkeypress(add5,"space")

elif c>0 and r>0:
    turtle.color("red")
    turtle.onscreenclick(draw_circle, btn=1, add=True)
    turtle.getscreen().onkeypress(add1,"s")
    turtle.getscreen().onkeypress(add2,"c")
    turtle.getscreeb().onkeypress(add3,"r")
    turtle.getscreen().onkeypress(add4,"g")
    turtle.getscreen().onkeypress(add5,"space")

else:
    turtle.color("green")
    turtle.onscreenclick(draw_circle, btn=1, add=True)
    turtle.getscreen().onkeypress(add1,"s")
    turtle.getscreen().onkeypress(add2,"c")
    turtle.getscreeb().onkeypress(add3,"r")
    turtle.getscreen().onkeypress(add4,"g")
    turtle.getscreen().onkeypress(add5,"space")

turtle.getscreen().listen()
turtle.mainloop()