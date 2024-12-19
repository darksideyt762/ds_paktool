#!/bin/bash

# Install required Python package
pkg update -y
pkg upgrade -y
pkg install python -y

# Move the Python script to the Termux bin folder for easy access
mv ~/storage/downloads/ds_paktool.py $PREFIX/bin/ds_paktool
chmod +x $PREFIX/bin/ds_paktool

# Run the Python script to set up the directories
ds_paktool

echo "Installation complete! Type 'ds_paktool' to unpack .pak files."
