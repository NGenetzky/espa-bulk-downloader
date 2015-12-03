#!/usr/bin/env python

from setuptools import setup

setup(
    # Application name:
    name="espa_bulk_downloader",

    # Version number:
    version="1.0",

    # Application author details:
    author="David V. Hill",
    author_email="@usgs.gov",

    license=open('LICENSE.txt').read(),
    long_description=open('README.md').read(),

    # Packages
    packages=["espa_bulk_downloader"],

    # Scripts
    # Moves the script to the user's bin directory so that it can be executed.
    # Usage is 'download_espa_order.py' not 'python download_espa_order.py'
    scripts=["espa_bulk_downloader/download_espa_order.py"],

    # Dependent packages (distributions)
    install_requires=[
        "feedparser <= 5.1.2, >=5.1.2"
    ],
)
