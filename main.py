from banner import generate_banner
import subprocess
import socket
import ipaddress
from utility import find_local_ip, find_subnet_range, ip_range
from scanner import scan_subnet

if __name__ == "__main__":
    tool_name = ""

    while True:
        generate_banner(tool_name)

        local_ip = find_local_ip()

        if local_ip:
            print(f"Your local IP Address is: {local_ip}")
            subnet = find_subnet_range(local_ip)
            print(f"The calculated CIDR notation is: {subnet}")
            ip_range(subnet)

            # Asks users for their choice of scan

            print()
            print("Choose a scan option:")
            print()
            print("1. Scan all hosts for open ports")
            print("2. Scan active hosts for the first 1000 ports and identify running services")
            print("3. Conduct a full vulnerability scan on all open ports of active hosts")
            print("4. Perform a prioritized vulnerability scan on the first 1000 ports of active hosts")

            print()
            choice = input("Enter your choice (1/2/3/4): ")

            # Based on choice run the appropriate scan

            if choice == "1":
                print()
                print("Scanning all active hosts to find if there are any open ports and determine running services.....")
                scan_result = scan_subnet(subnet)

            elif choice == "2":
                print()
                print("Scanning all the active hosts for the first 1000 ports to determine running services.....")
                scan_result = scan_subnet(subnet, ports="1-1000")

            elif choice == "3":
                print()
                print("Scanning all the active hosts on all ports to determine if any running services have vulnerabilities.....")
                scan_result = scan_subnet(subnet, script="vuln")

            elif choice == "4":
                print()
                print("Scanning all active hosts on the first 1000 ports to determine if any services have vulnerabilities.....")
                scan_result = scan_subnet(subnet, ports="1-1000", script="vuln")
            else:
                print("Invalid choice.")  # Error handling, print invalid choice if any other option is entered
                scan_result = None

            if scan_result:
                print()
                print("Scan Results:")
                print()
                print(scan_result)
            else:
                print("Scan failed or no vulnerabilities found.")  # Error handling, print error message if scan was unsuccessful
        else:
            print("Unable to retrieve local IP address.")  # Error handling, print error if unable to find the local IP
        print()
        run_again = input("Do you want to run the program again? (yes/no): ")
        if run_again.lower() != 'yes':
            break