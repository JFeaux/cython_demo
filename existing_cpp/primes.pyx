cimport cython
from libcpp cimport bool

# Utilize previously written C++ function
cdef extern from '_primes.h':
    bool _is_prime(int n)

cpdef bool is_prime(int n):
    return _is_prime(n)








