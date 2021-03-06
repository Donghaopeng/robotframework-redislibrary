#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from RedisLibrary.version import VERSION

requirements = [
    'tox',
    'coverage',
    'robotframework==3.0.4',
    'redis==2.10.5',
    'deco'
]

test_requirements = [
    'fakeredis==0.8.2'
]

CLASSIFIERS = """
Development Status :: 5 - Production/Stable
License :: Public Domain
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

setup(
    name='robotframework-redislibrary2',
    version=VERSION,
    description="robotframework-redislibrary is a Robot Framework test library for manipulating in-memory data which store in Redis",
    author="Donghaopeng",
    author_email='1173619682@qq.com',
    url='https://github.com/Donghaopeng/robotframework-redislibrary.git',
    packages=[
        'RedisLibrary'
    ],
    package_dir={'robotframework-redislibrary':
                 'RedisLibrary'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='robotframework redislibrary redis',
    classifiers=CLASSIFIERS.splitlines(),
    test_suite='tests',
    tests_require=test_requirements
)

