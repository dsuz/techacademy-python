import numpy

# 例1
print((numpy.arange(1,10)*numpy.arange(1,10)[:,numpy.newaxis]).tolist())

# 例2
print(numpy.arange(1,10)*numpy.arange(1,10)[:,numpy.newaxis])