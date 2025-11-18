#!/usr/bin/env python
"""Setup script for GRAPE: Grammatical Algorithms in Python for Evolution"""

from setuptools import setup, find_packages
import os

# Read the README
readme_path = os.path.join(os.path.dirname(__file__), 'GRAPE README.md')
if os.path.exists(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        long_description = f.read()
else:
    long_description = 'GRAPE: Grammatical Algorithms in Python for Evolution'

setup(
    name='grape',
    version='0.1.0',
    description='Grammatical Algorithms in Python for Evolution',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Allan de Lima, Samuel Carvalho, et al.',
    url='https://github.com/tsbertalan/grape',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.7',
    install_requires=[
        # commented out for offline install.
        # 'deap',
        # 'numpy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
