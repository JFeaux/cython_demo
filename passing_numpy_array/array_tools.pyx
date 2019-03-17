cimport cython
cimport numpy as np

# Utilize previously written C++ function
cdef extern from '_sum.h':
    double _sum(double* array, int size)

def sum(np.ndarray[double, ndim=1] array):
    # Passes a numpy array to C++ code
    return _sum(&array[0], array.size)








