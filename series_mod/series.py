# this is an implementation of the 'series' functionality using a module.

n = 0
print "this is before add_one()"
print n
print "__________________________"
b = 7

def add_one():
    global n
    global b 
    print "In the func, n is %d"%(n)
    n = n + 1
    b = b + 1
    print n
    return n

print "this is after add_one()"
print n
print "____________________"
# additional questions to address:
#  - what does 'global' do, above?
#  - what naming limitations are there on series.py? Could we name it
#        series_mod.py or series-mod.py, and still have it work as a module?
