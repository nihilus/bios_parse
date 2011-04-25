class BIOS_Function:
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


class PCI_dev:
	def __init__(self, bus = 0, device = 0, function = 0, name = ""):
		self.bus = bus
		self.device = device
		self.function = function
		self.name = name
		self.space = []

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

