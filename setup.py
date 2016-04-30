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
    url='https://github.com/Tiago-Lira/scrapyd-mongodb',
    download_url='https://github.com/Tiago-Lira/scrapyd-mongodb/tarball/0.1.0',
    keywords=['scrapy', 'scrapyd', 'mongodb', 'queue',
              'scrapyd-queue', 'scrapyd-backend', 'backend'],
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'scrapy',
        'pymongo',
    ],
    classifiers=[],
)
