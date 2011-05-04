import idc
import idaapi
import idautils

import os

def get_bootblock_start_address():
	file_path = idaapi.get_input_file_path()
	file_size = os.path.getsize(file_path)
	print("File size is {0}".format(file_size))
	addr = file_size - 0x10000
	return addr

def relocate_segment(source, destination, size):
	buf = idaapi.get_many_bytes(source, size)
	idaapi.patch_many_bytes(destination, buf)

def relocate_bootblock():
	bootblk_start = 0xF000 << 4
	bootblk_end = 0x10000 << 4
	bootblk_baseparagraph = 0xF000
	bootblk_size = 0x10000 # 64 Kbyte

	idaapi.add_segm(bootblk_baseparagraph, bootblk_start, bootblk_end, "BOOTBLK", "CODE")
	bootblk = idaapi.get_segm_by_name("BOOTBLK")
	idaapi.set_segm_addressing(bootblk, 16)
	bootblk_addr = get_bootblock_start_address()
	print("Found bootblock at {0} addr!".format(hex(bootblk_addr)))
	relocate_segment(bootblk_addr, bootblk_start, bootblk_size)

relocate_bootblock()
