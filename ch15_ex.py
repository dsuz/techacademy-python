import numpy

print((numpy.arange(1,10)*numpy.arange(1,10)[:,numpy.newaxis]).tolist())

#以下でも構わない
print(numpy.arange(1,10)*numpy.arange(1,10)[:,numpy.newaxis])