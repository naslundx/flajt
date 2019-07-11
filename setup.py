import re
import setuptools


with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="flajt",
    version="0.0.1",
    author="Marcus Näslund",
    author_email="naslundx@gmail.com",
    description="Play the Flajt video with a simple import",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.arlanda.se",
    python_requires=">=3.0",
    packages=["src"],
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7.3",
        "License :: MIT",
        "Operating System :: OS Independent",
    ],
)
