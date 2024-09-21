"""
Setup script for the dpm-ml project.

This script handles the packaging and distribution of the dpm-ml project,
a machine learning project for disease prediction using scikit-learn.
"""

from setuptools import setup, find_packages

setup(
    name='dpm-ml',
    version='1.0.0',
    author="Neeraj Singh",
    author_email="nsinghh.04@gmail.com",
    description="A machine learning project for disease prediction",
    url="https://github.com/neeraj-395/dpm-ml",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    python_requires='>=3.7'
)
