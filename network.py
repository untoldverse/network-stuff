from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
import requests

mini = {
    "device_type" : "linux",
    "host" : "192.168.0.94",
    "username" : input("Enter Username: "),
    "password" : getpass()

}

    
def main():
    try:
        net_connect = ConnectHandler(**mini)
        output = net_connect.send_command("ls -la /opt")
        pprint(output)
        net_connect.disconnect()
    except:
        print("Failed to connect")
if __name__ == "__main__":
    main()