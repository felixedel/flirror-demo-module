import os
from setuptools import find_packages, setup


# Utility function  read the README file.
def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


requires = [
    # Flirror version 1.1.0 is the minimal version that supports the plugin
    # mechanism.
    "flirror>=1.1.0",
]

setup(
    name="flirror-demo-modules",
    version="0.1.0",
    author="Felix Edel",
    author_email="felix.edel@mein.gmx",
    description="A demo module for Flirror",
    python_requires=">=3.6",
    install_requires=requires,
    license="MIT",
    keywords="smartmirror magicmirror flask",
    url="https://github.com/felixedel/flirror-demo-module",
    packages=find_packages(),
    long_description=read("README.md"),
)
