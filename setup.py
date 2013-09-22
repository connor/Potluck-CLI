#!/usr/bin/env python

from setuptools import setup

setup(
    name="Potluck",
    version="0.1",
    description="A CLI for Potluck!",
    author="Connor Montgomery",
    author_email="c@cnnr.me",
    url="http://github.com/connor/potluck-cli",
    license="MIT",
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    packages=[
        "_potluck"
    ],
    scripts=[
        "potluck"
    ],
    install_requires=[
        "requests",
        "termcolor"
    ]
)