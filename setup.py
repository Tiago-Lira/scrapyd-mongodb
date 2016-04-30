#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='scrapyd-mongodb',
    version='0.1.0',
    description='Scrapyd Queue Management with MongoDB',
    author='Tiago Lira',
    author_email='tiagolira.dev@gmail.com',
    license='MIT',
    keywords=['scrapy', 'scrapyd', 'mongodb', 'queue',
              'scrapyd-queue', 'scrapyd-backend', 'backend'],
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'scrapy',
        'pymongo',
    ]
)
