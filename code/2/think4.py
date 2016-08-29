"""
Exercise questions from Think like a Computer Scientist
http://www.greenteapress.com/thinkpython/html/index.html

Exercises 4.2,4.3

"""
from swampy.TurtleWorld import *
import math
world = TurtleWorld()
bob = Turtle()

print bob
bob.delay=0.01

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def arc(t, r, angle):
    """Draws an arc
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n


    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

def leaf(t, r, angle):
    """Draws a petal using two arcs.

    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180 - angle)

def whole(t, n, r, angle):
    """Draws a flower with n petals.

    t: Turtle
    n: number of petals
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        leaf(t, r, angle)
        lt(t, 360.0/n)

def move(t, length):
    
    pu(t)
    fd(t, length)
    pd(t)

whole(bob,7,40,55)
move(bob,88)
whole(bob,10,40,80)
move(bob,88)
whole(bob,10,90,10)

wait_for_user()