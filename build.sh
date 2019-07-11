#!/bin/bash -ex

rm -rf build/ dist/ flajt.egg-info/
python setup.py bdist_wheel
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
