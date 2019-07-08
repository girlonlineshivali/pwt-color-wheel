from turtle import *
t1 = Turtle()

#imports turtle + window for graphics

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

#color list

import random

#necessary to import to make sure the same color isn't being draw 

t1.up()
t1.goto(-200,0)
t1.down()
t1.width(5)
t1.hideturtle()
t1.speed(0)

#draws the lines
# speed is max to make it go faster
# hide turtle so you don't see the cursor which is drawing the lines

for i in range (9001):
  colorchoice = random.choice(colors)
  t1.color (colorchoice)
  t1.forward(500)
  t1.right(181)

#uses random import to randomize color choice 


