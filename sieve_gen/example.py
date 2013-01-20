import sieve

c = 0
for n in sieve.next():
    print n 
    c += 1

    if c >= 10:
        break

