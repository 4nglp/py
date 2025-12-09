import numpy as np

m1 = np.array([
    [1,2,3],[4,5,6],[7,8,9]
])
print(m1)
m2 = np.array([
    [8,-1,8],[2,1,3],[18,2,32]
])
add = m1 + m2
mul = m1 @ m2
m2_tr = m2.T
col2_mul =mul[:,1]