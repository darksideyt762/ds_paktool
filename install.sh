#!/bin/bash

# Install required packages
pkg install python -y

# Move Python script to the Termux bin folder
mv ~/storage/downloads/ds_paktool.py $PREFIX/bin/ds_paktool
chmod +x $PREFIX/bin/ds_paktool

# Run the Python script to set up the directories
ds_paktool

echo "Installation complete! Type 'ds_paktool' to unpack .pak files."