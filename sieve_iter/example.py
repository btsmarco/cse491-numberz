import sieve

c = 0
for n in sieve.Is_prime():
    print n 
    c += 1

    if c >= 10:
        break

