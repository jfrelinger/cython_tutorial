from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("cyprimes", ["cyprimes.pyx"]),
                   Extension("cyprimes2", ['cyprimes2.pyx']),
                   Extension("cyprimes3", ['cyprimes3.pyx', 'ffiprimes.c'])]
)