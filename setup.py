"""UNS library command line interface setup script."""
# pylama:ignore=D203,D102
import re

from os.path import join, dirname
from setuptools import setup, find_packages


# reading package version (same way the sqlalchemy does)
with open(join(dirname(__file__), 'cargs.py')) as v_file:
    package_version = re.compile('.*__version__ = \'(.*?)\'', re.S).\
        match(v_file.read()).group(1)


dependencies = [
    'easycli',
]


setup(
    name='cargs',
    version=package_version,
    py_modules=['cargs'],
    install_requires=dependencies,
    include_package_data=True,
    license='MIT',
    entry_points={
        'console_scripts': [
            'cargs = cargs:CArgs.quickstart',
        ]
    }
)
