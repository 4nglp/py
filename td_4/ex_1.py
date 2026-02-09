import numpy as np

a = np.array([
    [5,  15, 34, 21, 11, 18],
    [3,  11, 75, 3,  56, 39],
    [19, 30, 24, 95, 99, 90],
    [10, 24, 43, 45, 65, 19],
    [45, 87, 18, 78, 74, 71]
])

b = np.sort(a, axis=0)[::-1] # without the the last [] will get it sorted asec
print(a)
print(b)
