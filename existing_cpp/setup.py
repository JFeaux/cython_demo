from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

sourcefiles = ['primes.pyx', '_primes.cpp']
extra_compile_args = []
libraries = []

ext = [Extension('*', 
        sourcefiles, 
        extra_compile_args=extra_compile_args,
        libraries=[],
        language='c++')
        ]

setup(ext_modules=cythonize(ext))

