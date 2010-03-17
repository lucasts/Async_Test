#!/usr/bin/env python
# make a horizontal bar chart

from pylab import *

# data dict
data = dict()

# read summary file
lines = open('summary.txt').read().split('\n')
lines.pop()

for l in lines:
   llist = l.split(':')
   data[llist[0]] = llist[1]

pos = [1,2,3,4,5]
val = []
tit = []

for k in data:
   val.append(float(data[k]))
   tit.append(k)
  

#val = 3+10*rand(5)    # the bar lengths
#pos = arange(5)+.5    # the bar centers on the y axis

#figure(1)
barh(pos,val, align='center')
yticks(pos, tit)
xlabel('Request per second')
title('Async Implementations Bench')
grid(True)
savefig('result.png');
show()

