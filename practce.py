#!/usr/bin/env python3
import re
import socket
from geoip import geolite2
import argparse
import json
import geoip2.database

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(host_ip)

# Setup commandline arguments
parser = argparse.ArgumentParser(description='Get IP Geolocation info')
parser.add_argument('--hostname', action="store", dest="hostname", required=True)

# Parse arguments
given_args = parser.parse_args()
hostname = given_args.hostname
ip_address = socket.gethostbyname(hostname)

print("IP address: {0}".format(ip_address))

match = geolite2.lookup(ip_address)

if match is not None:
    print('Country: ',match.country)
    print('Continent: ',match.continent)
    print('Time zone: ', match.timezone)
    print('Location: ', match.location)
