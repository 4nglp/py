import numpy as np
# all val between 0 and 1 and the sum of each line is 1
m = np.array([
    [0.5,0.3,0.2],
    [0.2,0.8,0],
    [0.3,0.3,0.4]
]) 
rows, cols = m.shape

def is_sato(p):
   is_valid = np.all((p >=0) & (p <= 1)) 
   sum_row = np.all(np.sum(p, axis =1) == 1)
   return is_valid,sum_row
print(is_sato(m))

def is_bisto(p):
    is_valid = np.all((p >= 0) & (p <= 1))
    sum_row = np.all(np.sum(p,axis=1) == 1)
    sum_cols = np.all(np.sum(p,axis=0) == 1)
    return is_valid,sum_row,sum_cols
print(is_bisto(m))


