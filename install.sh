#!/bin/bash

# Install required Python package
pkg update -y
pkg upgrade -y
pkg install python -y

# Move the Python script to the Termux bin folder for easy access
mv ~/storage/downloads/ds_paktool.py $PREFIX/bin/ds_paktool.py
chmod +x $PREFIX/bin/ds_paktool.py

# Make sure the Python script is executable with the python command
echo "Installation complete! Type 'python ds_paktool.py' to unpack .pak files."
