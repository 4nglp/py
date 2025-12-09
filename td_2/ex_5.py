import numpy as np

M = [
    [3, 0, 0],
    [0, 5, 0],
    [0, 0, 1]
]

def is_diag(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            if i != j and M[i][j] != 0: # i = j diags
                return False
    return True

def is_diag_np(M):
    M = np.array(M)
    return np.all(M == np.diag(np.diag(M))) # compares the old m with a new matrix that is built to be the diagonal ver

print(is_diag(M))
print(is_diag_np(M))
