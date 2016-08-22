#!/usr/bin/python
"""
fib.py (c) 2016 tarunchhabra.com, Apache licence

Generates nth fibonacci number using dynamic programming

For more on this kind of programming, see
https://www.youtube.com/watch?v=OQ5jsbhAv_M
"""
memo = {}
def fib(n):
	if n in memo:
		return memo[n]
	if n <= 2:
		f=1
	else:
		f = fib(n-1) + fib(n-2)
		memo[n] = f
	return f