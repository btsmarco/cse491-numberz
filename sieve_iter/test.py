import sieve 

def test1():
    f = sieve.Is_prime()
    i = iter(f)
    assert i.next() == 3
    print "done test1: success"

def test2():
    f = sieve.Is_prime()
    i = iter(f)
    i.next()
    assert i.next() == 5
    print "done test2: success"

def test3():
    f = sieve.Is_prime()
    i = iter(f)
    i.next()
    i.next()
    assert i.next() == 7
    print "done test3: success"

test1()
test2()
test3()

