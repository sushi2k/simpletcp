__author__ = "Thomas D. Fischer"

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="simpletcp",
      author="Thomas D. Fischer",
      version="1.0.0",
      py_modules=["simpletcp",]
      )
