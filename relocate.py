import idc
import idaapi
import idautils

import os

def get_bootblock_start_address():
	file_path = idaapi.get_input_file_path()
	file_size = os.path.getsize(file_path)
	addr = file_size - 0x10000
	return addr

def relocate_segment(source, destination, size):
	buf = idaapi.get_many_bytes(source, size)
	idaapi.patch_many_bytes(destination, buf)

bootblk_start = 0xF000 << 4
bootblk_end = 0x10000 << 4
bootblk_baseparagraph = 0xF000
bootblk_size = 0x10000 # 64 Kbyte

idaapi.add_segm(bootblk_baseparagraph, bootblk_start, bootblk_end, "BOOTBLK", "CODE")
bootblk_addr = get_bootblock_start_address()
relocate_segment(bootblk_addr, bootblk_start, bootblk_size)

