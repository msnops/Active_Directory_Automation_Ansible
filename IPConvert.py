# importing the module
import ipaddress
import sys
param1 = sys.argv[0]
addr1 = ipaddress.ip_address(param1)
print(int(addr1))

# converting int to IPv4 address
#print(ipaddress.ip_address(3221225000))
#print(ipaddress.ip_address(123))

# converting int to IPv6 address
#print(ipaddress.ip_address(42540766400282592856903984001653826561))

# importing the module
#import ipaddress

# converting IPv4 address to int

#addr2 = ipaddress.ip_address('0.0.0.123')

#print(int(addr2))

# converting IPv6 address to int
#addr3 = ipaddress.ip_address('2001:db7:dc75:365:220a:7c84:d796:6401')
#print(int(addr3))
