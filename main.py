from netbox import netbox
from pprint import pprint
import os,sys



try:
    NETBOX_TOKEN = os.environ["NETBOX_TOKEN"]
    NETBOX_URL = os.environ["NETBOX_URL"]
except KeyError:
    print("ENV values not set")
    sys.exit()

n = netbox(netbox_url=NETBOX_URL,netbox_token=NETBOX_TOKEN)
devices = n.get_devices()
ips = n.get_available_ips()
vms = n.get_vms("?tag=prod")
dev_int = n.get_device_interfaces()
vm_interfaes = n.get_vm_interfaces()
    

pprint(vms)


