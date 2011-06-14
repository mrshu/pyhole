import os
import sys
from setuptools import setup, find_packages
from pyhole import utils

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = ['eventlet', 'pywapi', 'simplejson']
if sys.version_info < (2,6):
    requirements.append('simplejson')

version = utils.version(short=True)

setup(
    name = "pyhole",
    version = version,
    description = "Modular IRC Bot for Python",
    long_description = read('README'),
    url = 'https://github.com/jk0/pyhole',
    license = 'Apache',
    author = 'Josh Kearney',
    author_email = 'josh@jk0.org',
    packages = find_packages(exclude=['tests']),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Service',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = requirements,
)