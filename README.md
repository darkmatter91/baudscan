# Baud Rate Scanner

This script checks for the correct baud rate of a serial device. If it detects the right baud rate, it prompts the user to interact with the device using `picocom`.

![ray-so-export (1)](https://github.com/user-attachments/assets/505344bf-c494-4a18-aa92-798e576be628)


## Installation

1. **Run** `setup.sh` to configure your enviornment

## Usage

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/baudscan.git
    cd baudscan
    ```

2. **Run the Script**:
    ```sh
    python baudScan.py
    ```

3. **Follow the Prompts**:
    - The script will list available serial ports and try common baud rates.
    - If a working baud rate is found, you will be prompted to interact with the device using `picocom`.


### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing
1. Fork the repository.
2. Create your feature branch (git checkout -b feature/your-feature).
3. Commit your changes (git commit -am 'Add some feature').
4. Push to the branch (git push origin feature/your-feature).
5. Create a new Pull Request.

### Acknowledgments
pyserial

picocom
