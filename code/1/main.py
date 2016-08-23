"""
main.py (c) 2016 tarunchhabra.com, Apache licence

main.py to test utest.py program
"""
import utest
import who1
import who2
import who3
from fib import fib


def is_equal(x,y):
	return x==y

@utest.ok
def fail_test():
	"Adding another test to check results"
	assert 1 == 2
@utest.ok
def get_fib5():
	"To get the fibonacci number for 5th term in series"
	number = fib(5)
	print '5th term is fibonacci series is : %d' % number
	assert 5 == number
@utest.ok
def get_fib100():
	"To get the fibonacci number for 100th term in series"
	number = fib(100)
	print '100th term is fibonacci series is : %d' % number
	assert number == 354224848179261915075
@utest.ok
def get_fib3():
	number = fib(3)
	print '3rd term in the fibonacci series is : %d' % number
	assert number == 2
