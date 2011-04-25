# *************************** BOOTBLOCK ********************************

post_tbl = (
(0x7F, "TP_BB_LOCK", "Lock Boot Block"),
(0x80, "TP_BB_CS_INIT", "Chipset Init"),
(0x81, "TP_BB_BRIDGE_INIT", "Bridge Init"),
(0x82, "TP_BB_CPU_INIT", "CPU Init"),
(0x83, "TP_BB_TIMER_INIT", "System timer Init"),
(0x84, "TP_BB_IO_INIT", "System IO init"),
(0x85, "TP_BB_FORCE", "Check force recovery boot"),
(0x86, "TP_BB_CHKSUM", "Check BIOS checksum"),
(0x87, "TP_BB_GOTOBIOS", "Go to BIOS"),
(0x88, "TP_BB_MP_INIT", "Init Multi Processor"),
(0x89, "TP_BB_SET_HUGE", "Set Huge Seg"),
(0x8A, "TP_BB_OEM_INIT", "OEM Special Init"),
(0x8B, "TP_BB_HW_INIT", "Init PIC and DMA"),
(0x8C, "TP_BB_MEM_TYPE", "Init Memory Type"),
(0x8D, "TP_BB_MEM_SIZE", "Init Memory Size"),
(0x8E, "TP_BB_SHADOW", "Shadow Boot Block"),
(0x8F, "TP_BB_SMM_INIT", "Init SMM"),
(0x90, "TP_BB_RAMTEST", "System Memory test"),
(0x91, "TP_BB_VECS_INIT", "Init Interrupt vectors"),
(0x92, "TP_BB_RTC_INIT", "Init RTC"),
(0x93, "TP_BB_VIDEO_INIT", "Init Video"),
(0x94, "TP_BB_OUT_INIT", "Init Beeper"),
(0x98, "TP_BB_USB_INIT", "Initialize the USB controller"),
(0x95, "TP_BB_BOOT_INIT", "Init Boot"),
(0x96, "TP_BB_CLEAR_HUGE", "Clear Huge Seg"),
(0x97, "TP_BB_BOOT_OS", "Boot to OS"),
(0x99, "TP_BB_SECUR_INIT", "Init Security")
)

# Return with NZ flag set:
# mov al, 01   ; 88
# or  al, al
# jmp si

# phoenix entry

sig_asm = (
"cli
shl edx,16
mov fs, ax
ror eax, 16
mov gs, ax
jmp <symbol>
mov si, 0F000h
mov ds, si
mov si, 0FFF0h
mov bl, ds:[si]
cmp bl, 0E9h
jne <symbol>
jmp_far <symbol>
<symbol>:
DB  0EAh
DW  0E05Bh
DW  0F000h"
)

phoenix_BB_start = BIOS_Function("BB_boot_start", 0, sig_asm[i], sig_bin[i], signature)
