#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup file used for install this package.

Copyright (C) 2016 Canux CHENG.
All rights reserved.
Name: setup.py
Author: Canux CHENG canuxcheng@gmail.com
Version: V1.0.0.0
Time: Fri 05 Aug 2016 09:59:29 AM CST

Description:
    ./setup.py -h
"""
import os

from setuptools import setup, find_packages

import wechat

NAME = 'django-wechat-api'
VERSION = wechat.__version__
URL = 'https://github.com/crazy-canux/django-wechat-api'
DESCRIPTION = "Pure python/django for wechat official account interface."
KEYWORD = "python django wechat"


def read(readme):
    """Give reST format README for pypi."""
    extend = os.path.splitext(readme)[1]
    if (extend == '.rst'):
        import codecs
        return codecs.open(readme, 'r', 'utf-8').read()
    elif (extend == '.md'):
        import pypandoc
        return pypandoc.convert(readme, 'rst')

INSTALL_REQUIRES = []

setup(
    name=NAME,
    version=VERSION,
    url=URL,
    author='Canux CHENG',
    author_email='canuxcheng@gmail.com',
    maintainer='Canux CHENG',
    maintainer_email='canuxcheng@gmail.com',
    description=DESCRIPTION,
    keywords=KEYWORD,
    long_description=read('README.rst'),
    license='GPL',
    platforms='any',
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(exclude=['wechat']),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django :: 1.8",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
