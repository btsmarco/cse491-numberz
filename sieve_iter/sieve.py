# The implementation of the sieve by an iterator.

class Is_prime(object):
    def __init__(self):
        self._primeslist = [2]

    def __iter__(self):
        return self

    def _is_prime(self):
        for i in self._primeslist:
            if  self.start % i == 0:
                return False
        return True

    def next(self):
        self.start = self._primeslist[-1] + 1
        while 1:
            if self._is_prime():
                self._primeslist.append(self.start)
                return self.start

            self.start += 1

