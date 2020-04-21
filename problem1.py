#! usr/bin/env python

numbers = []
for jj in range(1000):
    if jj%3==0 or jj%5==0:
        numbers.append(jj)

sum = sum(numbers)
print "sum = {}".format(sum)
