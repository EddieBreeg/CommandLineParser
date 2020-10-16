import glob
import io
import re
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

with open('README.md') as rm:
    long_description=rm.read()

setup(
    name="CommandLineParser",
    version="0.0.1",
    license="MIT",
    description="A simple class to help you parse the arguments passed in the command line",
    long_description=long_description,
    author="Eddie Breeg",
    author_email="eddiebreeg0@protonmail.com",
    url="https://github.com/EddieBreeg/CommandLineParser",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(i))[0] for i in glob.glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: https://pypi.org/classifiers/
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    keywords=[
        # eg: "keyword1", "keyword2", "keyword3",
    ],
    install_requires=[
        # eg: "aspectlib==1.1.1", "six>=1.7",
    ],
    extras_require={
        # eg: 'rst': ["docutils>=0.11"],
    },

)
