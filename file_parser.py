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
				if head_group_name_by_index[group_index+1] == "id" :
					device.id = group.split(":")
				if head_group_name_by_index[group_index+1] == "name" :
					device.name = group
				
		devices.append(device)
	
	# fill registers values

	line = -1;
	device_count = -1;
	
	pci_regs = pci_space.finditer(text)

	for match in pci_regs :
		for group_index, group in enumerate(match.groups()) :
			if group :
				if space_group_name_by_index[group_index+1] == "line" :
					line += 1
					if group == "00":
						device_count += 1
						line = -1
						print("{0}:{1}.{2}".format(hex(devices[device_count].bus), hex(devices[device_count].device), hex(devices[device_count].function)))
						bios_num = 0x80000000 + (devices[device_count].bus << 16) + (devices[device_count].device << 11) + (devices[device_count].function << 8)
						print("For BIOS: {0}".format(hex(bios_num)))
						print("	| Name: {0} ID: {1}".format(devices[device_count].name, devices[device_count].id))
						print("______")
				if space_group_name_by_index[group_index+1] == "registers" :
					devices[device_count].space.append(group[1:].split(" "))
					# print(devices[device_count].space[line])

	return devices

def inteltool_parse(text):
	
	bridge = abstract.Bridge()

	bar_re =  re.compile("(?m)^(?P<barname>[A-Z]{4,}) = (?P<barvalue>0x[\dA-Fa-f]{4,8})")
	bar_group_name_by_index = dict( [ (v, k) for k, v in bar_re.groupindex.items() ])
	gpio_re = re.compile("(?m)^gpiobase\+(?P<address>0x[\dA-Fa-f]{4})\: (?P<value>0x[\dA-Fa-f]{1,8})\s+\((?P<name>[\w]{1,})\)")
	gpio_group_name_by_index = dict( [ (v, k) for k, v in gpio_re.groupindex.items() ])
	pm_re = re.compile("(?m)^pmbase\+(?P<address>0x[\dA-Fa-f]{4})\: (?P<value>0x[\dA-Fa-f]{1,8})\s+\((?P<name>[\w]{1,})\)")
	pm_group_name_by_index = dict( [ (v, k) for k, v in pm_re.groupindex.items() ])

	bar = bar_re.finditer(text)
	for match in bar :
		for group_index, group in enumerate(match.groups()) :
			if group :
				if bar_group_name_by_index[group_index+1] == "barname" :
					prev_group = group
				if bar_group_name_by_index[group_index+1] == "barvalue" :
					bridge.BAR[prev_group] = group

	for item in bridge.BAR.items():
		print(item)

	gpio = gpio_re.finditer(text)
	for match in gpio :
		gpio_reg = []
		for group_index, group in enumerate(match.groups()) :
			if group :
				if gpio_group_name_by_index[group_index+1] == "address" :
					gpio_reg.append(group)
				if gpio_group_name_by_index[group_index+1] == "value" :
					gpio_reg.append(group)
				if gpio_group_name_by_index[group_index+1] == "name" :
					gpio_reg.append(group)
		bridge.GPIO.append(gpio_reg)

	for item in bridge.GPIO:
		print(item)

	pm = pm_re.finditer(text)
	for match in pm :
		pm_reg = []
		for group_index, group in enumerate(match.groups()) :
			if group :
				if pm_group_name_by_index[group_index+1] == "address" :
					pm_reg.append(group)
				if pm_group_name_by_index[group_index+1] == "value" :
					pm_reg.append(group)
				if pm_group_name_by_index[group_index+1] == "name" :
					pm_reg.append(group)
		bridge.PM.append(pm_reg)

	for item in bridge.PM:
		print(item)



				
lspci_log = open("/home/xvilka/RE/vostro/lspci.log", "r")
lspci = lspci_log.read()
lspci_parse(lspci)
lspci_log.close()
inteltool_log = open("/home/xvilka/RE/vostro/inteltool.log", "r")
inteltool = inteltool_log.read()
inteltool_parse(inteltool)
inteltool_log.close()
