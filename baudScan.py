import serial
import serial.tools.list_ports
import subprocess


def print_banner():
    banner = """
    
:::::::::      :::     :::    ::: :::::::::   ::::::::   ::::::::      :::     ::::    ::: 
:+:    :+:   :+: :+:   :+:    :+: :+:    :+: :+:    :+: :+:    :+:   :+: :+:   :+:+:   :+: 
+:+    +:+  +:+   +:+  +:+    +:+ +:+    +:+ +:+        +:+         +:+   +:+  :+:+:+  +:+ 
+#++:++#+  +#++:++#++: +#+    +:+ +#+    +:+ +#++:++#++ +#+        +#++:++#++: +#+ +:+ +#+ 
+#+    +#+ +#+     +#+ +#+    +#+ +#+    +#+        +#+ +#+        +#+     +#+ +#+  +#+#+# 
#+#    #+# #+#     #+# #+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#     #+# #+#   #+#+# 
#########  ###     ###  ########  #########   ########   ########  ###     ### ###    #### 

                                             
    
                   \033[91mAuthor: Darkmatter91 (https://github.com/darkmatter91)\033[0m
    
    """
    print(banner)


# List of common baud rates to check
baud_rates = [9600, 19200, 38400, 57600, 115200]


def check_baud_rate(port, baud_rate):
    try:
        with serial.Serial(port, baud_rate, timeout=1) as ser:
            ser.write(b"AT\r")
            response = ser.read(10)
            if response:
                return True
    except serial.SerialException:
        pass
    return False


def get_serial_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]


def run_baudscan():
    ports = get_serial_ports()
    if not ports:
        print("\033[91m[!] No serial ports found.\033[0m")
        return

    for port in ports:
        print(f"\033[92m[*] Checking port: {port}\033[0m")
        for baud_rate in baud_rates:
            print(f"\033[94m[*] Trying baud rate: {baud_rate}\033[0m")
            if check_baud_rate(port, baud_rate):
                print(
                    f"\033[92m[+] Found working baud rate: {baud_rate} on port {port}\033[0m"
                )
                interact = input(
                    "\033[94m[*] Do you want to interact with this device using picocom? (yes/no): \033[0m"
                )
                if interact.lower() == "yes":
                    subprocess.run(["picocom", "-b", str(baud_rate), port])
                return

    print("\033[91m[!] No working baud rate found.\033[0m")


def main():
    print_banner()
    while True:
        print("Run Options:")
        print("1. Run BaudScan (Serial cables are configured)")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            run_baudscan()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
