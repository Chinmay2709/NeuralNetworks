from numpy import *


vec = [1.2,3.4,5,6]


SOFTMAX = lambda s: exp(s)/sum(exp(s))

print(SOFTMAX(sum(vec)))

