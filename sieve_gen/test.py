import sieve 

def test1():
    g = sieve.next()
    n = g.next() 
    assert n  == 3
    print "done test1: success"

def test2():
    g = sieve.next()
    n = g.next() 
    assert n  == 5
    print "done test2: success"

def test3():
    g = sieve.next()
    n = g.next() 
    assert n  == 7
    print "done test3: success"

#    def test1():
#        c = 0
#        for n in sieve.next():
        #    print n
#            c += 1
#            if c >= 1:
#                break
        #assert n  == 3
#        print "done test1: success"
#
test1()
test2()
test3()

