def ip_address(address):
    newAddres = ""
    splitAddress = address.split('.')
    newAddres = '[.]'.join(splitAddress)
    return newAddres


ipad = input('Enter your IP address : ')
ipaddress  = ip_address(ipad)
print(ipaddress)

