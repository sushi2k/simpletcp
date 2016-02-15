__author__ = "Thomas D. Fischer"

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="simpletcp",
      author="Thomas D. Fischer",
      author_email="tdf.tomfischer@gmail.com",
      url="http://gragas.github.io/simpletcp",
      version="1.0.2",
      license="Apache Version 2.0",
      description="Simple non-blocking TCP communcation.",
      keywords="tcp server non-blocking async asynchronous socket",
      packages=["simpletcp",]
      )
