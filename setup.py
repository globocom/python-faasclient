#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from os.path import dirname, abspath, join

from pip.download import PipSession
from pip.req import parse_requirements
from setuptools import setup, find_packages


def get_version(package):
    """Return package version as listed in `__version__` in `init.py`."""
    init_py = open(join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_path(*p):
    return join(dirname(abspath(__file__)), *p)


install_reqs = parse_requirements(get_path('requirements.txt'), session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]


setup(
    name="python-faasclient",
    url="https://gitlab.globoi.com/storm/python-faasclient",
    version=get_version("faasclient"),
    description='Python bindings to the Filer as a Service API.',
    author='STORM',
    author_email='storm@corp.globo.com',
    packages=find_packages(),
    install_requires=reqs,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'faas = bin.commands:cli',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=False,
)
