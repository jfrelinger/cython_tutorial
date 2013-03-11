cimport cython


cdef extern from "ffiprimes.h":
    void primes(int[10])


def cprimes():
    cdef int a[10]
    primes(a)
    return [i for i in a]
