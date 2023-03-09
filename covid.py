from turtle import *
speed(100)
color('#0d61b6')
bgcolor('black')
draw = 200
while draw >0:
    if draw <150:
        color('#1789FC')
    if draw < 100:
        color('#4aa4ff')
    left(draw)
    forward(draw * 3)
    draw -= 1