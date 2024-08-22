#!/bin/bash

# Update package list and upgrade all packages
sudo apt update && sudo apt upgrade -y

# Install Python3 and pip if not already installed
sudo apt install -y python3 python3-pip

# Install pyserial using pip
pip3 install pyserial

# Install picocom for serial communication
sudo apt install -y picocom

# Verify installations
echo "Verifying installations..."
python3 --version
pip3 --version
picocom --version

echo "Setup complete. You can now run the BaudScan tool."
