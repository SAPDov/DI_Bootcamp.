import turtle

wn = turtle.Screen()
wn.title('Bricks Breaking')
wn.bgcolor('Black')
wn.setup(width=600, height=400)
wn.tracer(0) # stop the window from updating

#Bottom paddle
bottom_pad = turtle.Turtle()
bottom_pad.speed(0) 
bottom_pad.shape('square')
bottom_pad.color('white')
bottom_pad.shapesize(stretch_wid=2, stretch_len=6)
bottom_pad.penup()
bottom_pad.goto(0, -200)



# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape('circle')
ball.color('white')
ball.shapesize(stretch_wid=2, stretch_len=0)
ball.penup()
ball.goto(0,0)



# #main game loop
while True:
	wn.update()



