import requests,json

NETBOX_URL = ""
NETBOX_API_ENDPOINTS = {
    "circuits": "/api/circuits/",
    "core": "/api/core/",
    "dcim": "/api/dcim/",
    "extras": "/api/extras/",
    "ipam": "/api/ipam/",
    "plugins": "/api/plugins/",
    "status": "/api/status/",
    "tenancy": "/api/tenancy/",
    "users": "/api/users/",
    "virtualization": "/api/virtualization/",
    "vpn": "/api/vpn/",
    "wireless": "/api/wireless/"
}


class netbox():
    def __init__(self,netbox_url,netbox_token):
        self.netbox_url = netbox_url
        self.headers = {'Authorization' : 'Token ' + netbox_token}

    def get_devices(self,args: str = ""):
        return requests.get(url=self.netbox_url+NETBOX_API_ENDPOINTS["dcim"]+"/devices"+args,headers=self.headers).json()['results']

    def get_device_interfaces(self,args: str = ""):
        return requests.get(url=self.netbox_url+NETBOX_API_ENDPOINTS["dcim"]+"/interfaces"+args,headers=self.headers).json()['results']

    def get_available_ips(self,args: str = ""):
        return requests.get(url=self.netbox_url+NETBOX_API_ENDPOINTS["ipam"]+"/ip-addresses"+args,headers=self.headers).json()['results']

    def get_vms(self,args: str = ""):
        return requests.get(url=self.netbox_url+NETBOX_API_ENDPOINTS["virtualization"]+"/virtual-machines/"+args,headers=self.headers).json()['results']

    def get_vm_interfaces(self,args: str = ""):
        return requests.get(url=self.netbox_url+NETBOX_API_ENDPOINTS["virtualization"]+"/interfaces"+args,headers=self.headers).json()['results']

    def get_vdisks(self,args: str = ""):
        return requests.get(url=self.netbox_url+NETBOX_API_ENDPOINTS["virtualization"]+"/virtual-disks"+args,headers=self.headers).json()['results']

    def new_device(self,name: str, device_type,site,status,**kwargs):
        pass

    def new_device_interfaces(self,**kwargs):
        pass

    def new_ip_assignment(self,**kwargs):
        pass

    def new_vms(self,**kwargs):
        pass

    def new_vm_interfaces(self,**kwarg):
        pass