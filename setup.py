#!/usr/bin/env python

import os
import sys

#import djstripe

__title__ = "dj-stripe"
__summary__ = "Django + Stripe Made Easy"
__uri__ = "https://github.com/pydanny/dj-stripe/"

__version__ = "0.7.0"

__author__ = "Daniel Greenfeld"
__email__ = "pydanny@gmail.com"

__license__ = "BSD"
__license__ = "License :: OSI Approved :: BSD License"
__copyright__ = "Copyright 2015 Daniel Greenfeld"

version = __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

INSTALL_REQUIRES = [
    'django>=1.7',
    'stripe>=1.22.2',
    'django-model-utils>=2.2',
    'django-braces>=1.8.0',
    'jsonfield>=1.0.3',
    'pytz>=2015.4'
]

setup(
    name='dj-stripe',
    version=version,
    description=__summary__,
    long_description=readme + '\n\n' + history,
    author=__author__,
    author_email=__email__,
    url=__uri__,
    packages=[
        'djstripe',
    ],
    package_dir={'djstripe': 'djstripe'},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    license=__license__,
    zip_safe=False,
    keywords='stripe django',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
)
