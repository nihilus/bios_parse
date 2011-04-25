import re

import abstract

def lspci_parse(text):

	devices = []

	pci_devnum = re.compile("(?m)^(?P<devnum>[\dA-Fa-f]{2}:[\dA-Fa-f]{2}.[\dA-Fa-f])(?P<class>.*)\[(?P<some>[\dA-Fa-f]{4})\]:(?P<name>.*)\[(?P<id>[\dA-Fa-f]{4}:[\dA-Fa-f]{4})\]")
	pci_space = re.compile("(?m)^(?P<line>[\dA-Fa-f]{2,4}):(?P<registers>(?: [\dA-Fa-f]{2}){16})$")

	head_group_name_by_index = dict( [ (v, k) for k, v in pci_devnum.groupindex.items() ])
	space_group_name_by_index = dict( [ (v, k) for k, v in pci_space.groupindex.items() ])

	pci_num = pci_devnum.finditer(text)
		
	# fill generic PCI information in PCI object

	for match in pci_num :
		device = abstract.PCI_dev()
		for group_index, group in enumerate(match.groups()) :
			if group :
				if head_group_name_by_index[group_index+1] == "devnum" :
					device.bus = int(group[0:2], 16)
					device.device = int(group[3:5], 16)
					device.function = int(group[6:7], 16)
					# print("device number: {0} : {1} . {2}".format(device.bus, device.device, device.function))
				if head_group_name_by_index[group_index+1] == "id" :
					device.id = group.split(":")
					# print("device id : {0}".format(device.id))
				if head_group_name_by_index[group_index+1] == "name" :
					device.name = group
					# print("device name : {0}".format(device.name))
				
			#	print("{0}: {1}".format(head_group_name_by_index[group_index+1], group))

		devices.append(device)
	
	# fill registers values

	line = 0;
	device_count = -1;
	
	pci_regs = pci_space.finditer(text)

	for match in pci_regs :
		for group_index, group in enumerate(match.groups()) :
			if group :
				if space_group_name_by_index[group_index+1] == "line" :
					line += 1
					if group == "00":
						device_count += 1
						print("{0}:{1}.{2}".format(hex(devices[device_count].bus), hex(devices[device_count].device), hex(devices[device_count].function))) 
						print("	| Name: {0} ID: {1}".format(devices[device_count].name, devices[device_count].id))
						print("______")
				if space_group_name_by_index[group_index+1] == "registers" :
					devices[device_count].space.append(group[1:].split(" "))
					#print(devices[device_count].space[line])
				
lspci_log = open("lspci.log", "r")
lspci = lspci_log.read()
lspci_parse(lspci)
lspci_log.close()
