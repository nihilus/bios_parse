# 1. You need these logs:
#
# lspci -nnvvvxxxx > lscpi.log
# lspnp -vv > lspnp.log
# lsusb -vvv > lsusb.log
# superiotool -deV > superiotool.log
# inteltool -a > inteltool.log
# ectool > ectool.log
# msrtool > msrtool.log
# dmidecode > dmidecode.log
# biosdecode > biosdecode.log
# nvramtool -x > nvramtool.log
# acpidump > acpitable.log
# dmesg > dmesg.log
#

import idc
import idaapi
import idautils

import math
  
import abstract
import file_parser

# ******************************** MSR stuff ******************************

import msr-amd
import msr-intel

# try find rdmsr and wrmsr instructions and add adresses here

def msr_parse():
	start = idc.MinEA()
	stop = idc.MaxEA()
	rdmsr_addr = idaapi.find_binary(start, stop, "0F 32", 0, 0) # find_binary(ea_t startea, ea_t endea, char ubinstr, int radix, int sflag) -> ea_t
	wrmsr_addr = idaapi.find_binary(start, stop, "0F 30", 0, 0)
	cpuid_addr = idaapi.find_binary(start, stop, "0F A2", 0, 0)
	idc.MakeCode(each)

# ************************************************ PORTS ***********************************************

PCI_CONFIG_ADDRESS = 0xCF8
PCI_CONFIG_DATA = 0xCFC
DUMMY_DELAY_PORT = 0xEB

#address, name, description

ports = (
	(0x92, "A20Init", "Fast A20 and Init Register"),
	(0x4D0, "MPIC_ELT", "Master PIC Edge/Level Triggered (R/W)"),
	(0x4D1, "SPIC_ELT", "Slave PIC Edge/Level Triggered (R/W)"),
	(0x70, "RTC_Index", "Real-Time Clock (Standard RAM) Index Register"),
	(0x74, "RTC_Index", "Real-Time Clock (Standard RAM) Index Register"),
	(0x71, "RTC_Target", "Real-Time Clock (Standard RAM) Target Register"),
	(0x75, "RTC_Target", "Real-Time Clock (Standard RAM) Target Register"),
	(0x72, "ExtRAM_Index", "Extended RAM Index Register"),
	(0x76, "ExtRAM_Index", "Extended RAM Index Register"),
	(0x73, "ExtRAM_Target", "Extended RAM Target Register"),
	(0x77, "ExtRAM_Target", "Extended RAM Target Register")
)

# search patterns:
#
# % mov dx, 0CF8h - Configuration of PCI
# % out dx,
# 
# % mov dx, 0CFCh - Read PCI 
# % in dx,
#
# % mov dx, 0CFCh - Write PCI
# % out dx, 

# in al, dx : EC
# in ax, dx : ED
# in al, <num> : E4 <NUM>
# in ax, <num> : E5 <NUM>
# out dx, al : EE
# out dx, ax : EF
# out <num>, al : E6 <NUM>
# out <num>, ax : E7 <NUM>

def ports_analisys():
	ports_struc = idc.AddEnum(-1, "ports", (FF_WRD|FF_DATA))
	idc.AddConstEx(ports_struc, "PCI_CONFIG_ADDRESS", PCI_CONFIG_ADDRESS, -1)
	idc.AddConstEx(ports_struc, "PCI_CONFIG_DATA", PCI_CONFIG_DATA, -1)

	for each in idaapi.find_binary(start, stop, "", 0, 0): # find_binary(ea_t startea, ea_t endea, char ubinstr, int radix, int sflag) -> ea_t
		idc.MakeCode(each)

def pci_analisys():
	# searching snippets:
	# ------------------- 
	# mov eax, 8000xxxxh
	# mov dx, CF8h
	# out dx, eax

# ******************************************** PARSE LOGS ********************************************

# trying to found:

def import_data_dumps():
	key_value_regex = re.compile(r"^\s*(?P<key>[^ =]+)\s*=\s*"
								 r"(?P<value>.+)\s*$", re.MULTILINE)
	
	is_intel = True
	is_amd = False
	# dmesg parse

	# CPU Vendor/Model

	if is_intel:
		# inteltool output parse
		# GPIOBASE ; PMBASE ; MCHBAR ; EPBAR ; DMIBAR ; PCIEXBAR
		try:
			log = open(filename, encoding="utf8")
			self.clear()
			for match in key_value_regex.finditer(log.read()):
				data = {}
				data[match.group("key")] = int(match.group("value"))
			return True
		except (EnviromentError) as err:
			print "import error"
			return False
		finally:
			if log is not None:
				log.close()

		BASE_GPIO = data["GPIOBASE"]
		BASE_PM	  = data["PMBASE"]
		BASE_MCH  = data["MCHBAR"]
		BASE_EP   = data["EPBAR"]
		BASE_DMI  = data["DMIBAR"]
		BASE_PCIE = data["PCIEXBAR"]
		# BASE_SMBUS = data["SMBUSBAR"]
		
		bases_struc = idc.AddEnum(-1, "bases", (FF_DWRD|FF_DATA))
		idc.AddConstEx(bases_struc, "BASE_GPIO", BASE_GPIO, -1)
		idc.AddConstEx(bases_struc, "BASE_PM", BASE_PM, -1)
		idc.AddConstEx(bases_struc, "BASE_MCH", BASE_MCH, -1)
		idc.AddConstEx(bases_struc, "BASE_EP", BASE_EP, -1)
		idc.AddConstEx(bases_struc, "BASE_DMI", BASE_DMI, -1)
		idc.AddConstEx(bases_struc, "BASE_PCIE", BASE_PCIE, -1)
		# idc.AddConstEx(bases_struc, "BASE_SMBUS", BASE_SMBUS, -1)



	elif is_amd:
		#other outputs parse
	
	else
		print "Error: Unknown CPU"



# ********************************************* STRUCTURES ********************************************

import smm_intel
import smm_amd

def phoenix_process():
	phoenix_cpu_smi_table = idc.AddStrucEx(-1, "phx_cpu_smi_table", 0)
	for register in INTEL_CPU_SMI_TABLE:
		idc.AddStrucMember(phoenix_cpu_smi_table, register[1], -1, (FF_WRD|FF_DATA)&0xFFFFFFFF, -1, 2)


# Phoenix-Award

# AMI

# Insyde


def big_endian(n):
	s = '%x' % n
	if len(s) & 1:
		s = '0' + s
	return s.decode('hex')

# 1. Try to find Stings for the BIOS Vendor
# 2. Add standard HW adresses


