# this is an implementation of the 'series' functionality using
# Python's iterator functionality.  Here, 'adder' is a class that
# obeys the iterator protocol.

class adder(object):
    def __init__(self):
		print "I am in init"
		self.n = 0

    def __iter__(self):
		print "I am in iter"
		return self

    def next(self):
		print "I am in next"
		self.n += 1
		return self.n
