cimport cython
from libcpp cimport bool

@cython.cdivision(True)
cpdef bool is_prime(int n):
    cdef int i
    if (n <= 1):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
