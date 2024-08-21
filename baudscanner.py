import serial
import serial.tools.list_ports
import subprocess

# List of common baud rates to check
baud_rates = [9600, 19200, 38400, 57600, 115200]

# Function to check if a baud rate works
def check_baud_rate(port, baud_rate):
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        ser.write(b'AT\r')  # Send a test command
        response = ser.read(10)  # Read response
        ser.close()
        if response:
            return True
    except serial.SerialException:
        pass
    return False

# Function to get the list of available serial ports
def get_serial_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]

# Main script logic
def main():
    ports = get_serial_ports()
    if not ports:
        print("\033[91m[!] No serial ports found.\033[0m")
        return

    for port in ports:
        print(f"\033[94m[*] Checking port: {port}\033[0m")
        for baud_rate in baud_rates:
            print(f"\033[94m[*] Trying baud rate: {baud_rate}\033[0m")
            if check_baud_rate(port, baud_rate):
                print(f"\033[92m[+] Found working baud rate: {baud_rate} on port {port}\033[0m")
                interact = input("\033[94m[*] Do you want to interact with this device using picocom? (yes/no): \033[0m")
                if interact.lower() == 'yes':
                    subprocess.run(["picocom", "-b", str(baud_rate), port])
                return

    print("\033[91m[!] No working baud rate found.\033[0m")

if __name__ == "__main__":
    main()
