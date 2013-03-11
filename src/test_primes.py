'''
Created on Mar 11, 2013

@author: jolly
'''

from timeit import timeit
setup = '''
from cyprimes import primes as cyprimes
from cyprimes2 import primes as cyprimes2
from cyprimes3 import cprimes as cyprimes3
from pyprimes import primes as pyprimes
from pyprimes2 import primes as pyprimes2
'''

if __name__ == '__main__':
    print 'python:', timeit('pyprimes()', setup=setup, number=10000)
    print 'python2:', timeit('pyprimes2()', setup=setup, number=10000)
    print 'cython:', timeit('cyprimes()', setup=setup, number=10000)
    print 'cython2:', timeit('cyprimes2()', setup=setup, number=10000)
    print 'cython3:', timeit('cyprimes3()', setup=setup, number=10000)