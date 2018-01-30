import numpy as np
x, y = np.array(range(1, 10)), np.array(range(1, 10)) 
print(x[:, np.newaxis]*y)
