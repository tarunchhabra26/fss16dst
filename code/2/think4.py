"""
    Exercise questions from Think like a Computer Scientist
    http://www.greenteapress.com/thinkpython/html/index.html
    
    Exercises 4.2,4.3
    
    Uses polygon.py for basic polygon drawing operations
    Uses approach similar to http://www.greenteapress.com/thinkpython/code/pie.py and 
    http://www.greenteapress.com/thinkpython/code/flower.py
    
"""
from polygon import arc, lt, pu, fd, pd, math, rt, Turtle, TurtleWorld, die, wait_for_user,bk


def petal(t, r, angle):
    """Draws a petal using two arcs.
        :param t: Turtle
        :param r: radius of the arcs
        :param angle: angle (degrees) that subtends the arcs
        """
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180 - angle)


def flower(t, n, r, angle):
    """Draws a flower with n petals.
        :param t: Turtle
        :param n: number of petals
        :param r: radius of the arcs
        :param angle: angle (degrees) that subtends the arcs
        """
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0 / n)


def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
        Leaves the pen down.
        :param t: Turtle
        :param length: Length of turtle movement
        """
    pu(t)
    fd(t, length)
    pd(t)


def draw_pie(t, n, r):
    """Draws a pie, then moves into position to the right.
        
        :param t: Turtle
        :param n: number of segments
        :param r: length of the radial spokes
        """
    polypie(t, n, r)
    pu(t)
    fd(t, r * 2 + 10)
    pd(t)


def polypie(t, n, r):
    """Draws a pie divided into radial segments.
        :param t: Turtle
        :param n: number of segments
        :param r: length of the radial spokes
        """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle / 2)
        lt(t, angle)


def isosceles(t, r, angle):
    """Draws an isosceles triangle.
        The turtle starts and ends at the peak, facing the middle of the base.
        :param t: Turtle
        :param r: length of the equal legs
        :param angle: peak angle in degrees
        """
    y = r * math.sin(angle * math.pi / 180)
    
    rt(t, angle)
    fd(t, r)
    lt(t, 90 + angle)
    fd(t, 2 * y)
    lt(t, 90 + angle)
    fd(t, r)
    lt(t, 180 - angle)

# Answer to 4.2
world = TurtleWorld()
bob = Turtle()
bob.delay = 0

move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

die(bob)

wait_for_user()


# Answer to 4.3
world = TurtleWorld()
bob = Turtle()
bob.delay = 0
pu(bob)
bk(bob, 130)
pd(bob)

size = 40
draw_pie(bob, 5, size)
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)

die(bob)


wait_for_user()
