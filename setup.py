import re
import setuptools


with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="flajt",
    version="0.0.2",
    author="Marcus Näslund",
    author_email="naslundx@gmail.com",
    description="Play the Flajt video with a simple import",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.github.com/naslundx/flajt",
    python_requires=">=3.0",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
