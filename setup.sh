#!/bin/bash

# Ensure we have storage permission in Termux
termux-setup-storage

# Update and upgrade packages
pkg update -y
pkg upgrade -y

# Install necessary dependencies
pkg install git python -y

# Clone the ds_paktool repository from GitHub
git clone https://github.com/darksideyt762/ds_paktool.git

# Navigate into the cloned repository folder
cd ds_paktool

# Set up the necessary folder structure
mkdir -p ~/storage/emulated/0/Download/ds_paktool/PAKS
mkdir -p ~/storage/emulated/0/Download/ds_paktool/UNPACK

# Make sure the Python script is executable
chmod +x ds_paktool.py

# Display completion message
echo "Installation complete! Type 'python ds_paktool.py' to unpack .pak files."
