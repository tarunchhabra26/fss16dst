"""
Exercise questions from Think like a Computer Scientist
http://www.greenteapress.com/thinkpython/html/index.html

Exercises 3.1,3.2,3.3,3.4,3.5

@author - Tarun Chhabra
"""

# Exercise 3.1 and 3.2
print '(Exercise 3.1 and 3.2) output of `print_lyrics` and `repeat_lyrics`\n'


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."


repeat_lyrics()


# Unresolved reference types 'repeat_lyrics' if it is moved to the start of the program
# Runs fine if print_lyrics is defined after repeat lyrics

# Exercise 3.3
def right_justify(s):
    """
    A simple method to right justify a string
    :param s: Any string
    :return: Right justified string
    """
    s_len = len(s)
    space_req = 70 - s_len
    return (' ' * space_req) + s


print '\n(Exercise 3.3)Output of `right_justify` '
print right_justify('allen')


# Exercise 3.4

# 1. Type this example into a script and test it.
def do_twice(f):
    f()
    f()


def print_spam():
    print 'spam'


print 'Exercise 3.4 part 1\n'
do_twice(print_spam)


# 2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
# function twice, passing the value as an argument.
# 3. Write a more general version of print_spam, called print_twice, that takes a string as a
# parameter and prints it twice.
# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
# argument.

def do_twice(f, v):
    f(v)
    f(v)


def print_twice(val):
    print val


value = 'spam'

print '\nExercise 3.4 part 2,3,4\n'
do_twice(print_twice, value)

# 5. Define a new function called do_four that takes a function object and a value and calls the
# function four times, passing the value as a parameter. There should be only two statements in
# the body of this function, not four.

print '\nExercise 3.4 part 5\n'


def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)


do_four(print_twice, value)


# Exercise 3.5
print '\nExercise 3.5 part 1\n'


def iter_f(f, v, _iter):
    i = 0
    while i < _iter:
        f(v)
        i += 1


def _print(v):
    print v


row = '+ - - - - + - - - - +'
row2 = '+ - - - - + - - - - + - - - - + - - - - +'
column = '|         |         |'
column2 = '|         |         |         |         |'

iter_f(_print, row, 1)
iter_f(_print, column, 4)
iter_f(_print, row, 1)
iter_f(_print, column, 4)
iter_f(_print, row, 1)

print '\n\n'
print '\nExercise 3.5 part 2\n'

iter_f(_print, row2, 1)
iter_f(_print, column2, 4)
iter_f(_print, row2, 1)
iter_f(_print, column2, 4)
iter_f(_print, row2, 1)
iter_f(_print, column2, 4)
iter_f(_print, row2, 1)
iter_f(_print, column2, 4)
iter_f(_print, row2, 1)
