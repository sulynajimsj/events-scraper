from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='events-scraper',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Suleiman Najim',
    author_email='Sulysalim@hotmail.com',
    description='A Python package to fetch events using Ticketmaster API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sulynajimsj/events-scraper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)