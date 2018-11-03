# -*- coding: utf-8 -*-
from setuptools import find_packages, setup


setup(
    name='wagtail_tinify',
    version='0.0.3',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Automatically compress images (.jpg and .png) using tinypng.com.',
    long_description='',
    url='https://github.com/KalobTaulien/wagtail_tinify',
    author='Kalob Taulien',
    author_email='kalob@kalob.io',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Wagtail',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    keywords='development',
    install_requires=[
        'wagtail>=2.1.0',
        'Django>=2.0',
        'tinify>=1.5.1'
    ]
)
