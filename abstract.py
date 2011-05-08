class BIOS_Function(object):
	def __init__(self, name, attributes, body_disasm, body_binary, signature):
		self.name = name
		self.attributes = attributes
		self.signature = signature
	@property
	def body_disasm(self):
	    return body_disasm

	@property
	def body_binary(self):
		return body_binary
	
	@property
	def signature(self):
		return signature # sha1 hash of body_binary


class PCI_dev(object):
	def __init__(self, bus = 0, device = 0, function = 0, name = ""):
		self.bus = bus
		self.device = device
		self.function = function
		self.name = name
		self.space = []
		self.header = [
		#   Register Value | Register Name | Register Description
			['', "DeviceID", "Device ID"],
			['', "VendorID", "Vendor ID"],
			['', "Status", "Status"],
			['', "Command", "Command"],
			['', "ClassCode", "Class Code"],
			['', "RevID", "Revision ID"],
			['', "BIST", "BIST"],
			['', "HeaderType", "Header Type"],
			['', "LatencyTimer", "Latency Timer"],
			['', "CacheLineSize", "CacheLineSize"],
			['', "BAR0", "Base Address Register 0"],
			['', "BAR1", "Base Address Register 1"],
			['', "BAR2", "Base Address Register 2"],
			['', "BAR3", "Base Address Register 3"],
			['', "BAR4", "Base Address Register 4"],
			['', "BAR5", "Base Address Register 5"],
			['', "CardbusCIS", "Cardbus CIS Pointer"],
			['', "SubsystemID", "Subsystem ID"],
			['', "SubsystemVID", "Subsystem Vendor ID"],
			['', "ExpansionBase", "Expansion ROM Base Address"],
			['', "CapPointer", "Capabilities Pointer"],
			['', "Max_Lat", ""],
			['', "Min_Gnt", ""],
			['', "InterruptPin", "Interrupt PIN"],
			['', "InterruptLine", "Interrupt Line"]
		]

	@property
	def bus(self):
		return self._bus

	@bus.setter
	def bus(self, bus):
		self._bus = bus

	@property
	def device(self):
		return self._device

	@device.setter
	def device(self, device):
		self._device = device

	@property
	def function(self):
		return self._function

	@function.setter
	def function(self, function):
		self._function = function

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def space(self):
		return self._space

	@space.setter
	def space(self, space):
		self._space = space

	@property
	def header(self):
		return self._header

	@header.setter
	def header(self, header):
		self._header = header

	def register(self, address):
		return self.space[address//16][address%16]


class Bridge(PCI_dev):
	def __init__(self):
		super(Bridge, self).__init__()
		self.BAR = {
			"GPIOBASE" : 0x0,
			"PMBASE" : 0x0,
			"RCBA" : 0x0,
			"MCHBAR" : 0x0,
			"EPBAR" : 0x0,
			"DMIBAR" : 0x0
			}
		self.GPIO = []
		self.PM = []
		self.RCB = []
		self.MCH = []
		self.EP = []
		self.DMI = []

		
	@property
	def BAR(self):		# Base Adress Register Array
		return self._bar
	
	@BAR.setter
	def BAR(self, BAR):
		self._bar = BAR

	@property   
	def GPIO(self):    # General Purpose I/O
		return self._gpio

	@GPIO.setter
	def GPIO(self, GPIO):
		self._gpio = GPIO

	@property
	def PM(self):	   # Power Management
		return self._pm

	@PM.setter
	def PM(self, PM):
		self._pm = PM

	@property
	def RCB(self):		# Root Complex Bus
		return self._rcb

	@RCB.setter
	def RCB(self, RCB):
		self._rcb = RCB

	@property   
	def MCH(self):    # General Purpose I/O
		return self._mch

	@MCH.setter
	def MCH(self, MCH):
		self._mch = MCH

	@property
	def EP(self):	   # Egress Port Root Complex
		return self._ep

	@EP.setter
	def EP(self, EP):
		self._ep = EP

	@property
	def DMI(self):		# MCH-ICH Serial Interconnect Ingress Root Complex
		return self._dmi

	@DMI.setter
	def DMI(self, DMI):
		self._dmi = DMI




	
	
	
