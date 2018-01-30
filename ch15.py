import numpy

line = numpy.array(range(1, 10))
multiplication_table = line.reshape(1, 9)

for i in range(2, 10):
    multiplication_table = numpy.append(multiplication_table, (line * i).reshape(1, 9), axis = 0)

print(multiplication_table)
