#!/usr/bin/env python

# DuzeruWifi
#	No Copyright Claudio A. Silva <claudiosilva@duzeru.org>
#
# as published by the Free Software Foundation; Version 2
# of the License.

try:
	import os
	import commands
	import sys
	import string
except Exception, detail:
	print detail
	pass

# checking the card type
print("-------------------------")
print("* I. scanning WIFI PCI devices...")
os.system("lspci | grep \"Network controller\" > /tmp/detected_wireless_devices")
devices_file = open("/tmp/detected_wireless_devices")
for device_item in devices_file.readlines():
	deviceArray = device_item.split()
	device = ' '.join(deviceArray[3:])
	pci_id_line = commands.getoutput("lspci -n | grep " + deviceArray[0]) 
	pci_id_array = pci_id_line.split()
	pci_id = ' '.join(pci_id_array[2:])	
	print "  -- " + device 
	print "      ==> PCI ID = " + pci_id	
print("-------------------------")
print("* II. querying ndiswrapper...")
os.system("ndiswrapper -l")	
print("-------------------------")
print("* III. querying iwconfig...")
os.system("iwconfig")
print("-------------------------")
print("* IV. querying ifconfig...")
os.system("ifconfig")
print("-------------------------")
print("* V. querying DHCP...")
os.system("sudo dhclient")
print("-------------------------")
print("* VI. querying nslookup google.com...")
os.system("nslookup google.com")
