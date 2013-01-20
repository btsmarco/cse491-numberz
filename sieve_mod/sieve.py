# This is an implementaion of sieve using a module

_primeslist = [2]

def _is_prime(primes, n):
    for i in primes:
        if n % i == 0:
            return False
    return True

def next():
    start = _primeslist[-1] + 1 #takes the last element in the list and adds one
    while 1:
        if _is_prime(_primeslist, start):
            _primeslist.append(start)
            return start

        start += 1

