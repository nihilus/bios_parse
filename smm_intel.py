# ****************************** Phoenix *************************************

PHX_INTEL_CPU_RegFormatTable0 = (0xFFD0,0xFFDC,0xFFD4,0xFFD8,0xFFEC,0xFFE8,0xFFE4,0xFFE0,0xFFF0,0xFFF4,0xFFB4,0xFFB0,0xFFAC,0xFFA8,0xFFF8,0xFFFC,0xFEF8,0xFEFC)
PHX_INTEL_CPU_RegFormatTable1 = (0xFF5C,0xFF74,0xFF64,0xFF6C,0xFF94,0xFF8C,0xFF84,0xFF7C,0xFFD8,0xFFE8,0xFFB4,0xFFB0,0xFFAC,0xFFA8,0xFFF8,0xFFFC,0xFEF8,0xFEFC)
PHX_INTEL_CPU_SMI_exit = (0x0F, 0xAA)

# offset, name, description
PHX_INTEL_CPU_SMI_TABLE = (
(0x000, "DFLT_CPU_SMBASE", "Default SMbase"),
(0x002, "CS_SMBASE", "Chipset SMbase"),
(0x004, "CS_SMRAM_SIZE","SMram size/4"),
(0x006, "PM_DISP", "PM Code Dispatcher"),
(0x008, "PM_CS", "PM Code Segment"),
(0x00A, "PM_DS", "PM Data Segment"),
(0x00C, "PM_SS", "PM Stack Segment"),
(0x00E, "SMI_VECT", "SMI Vector"),
(0x010, "CPU_REG_SAVE0", "CPU Register Save Area"),
(0x012, "CPU_REG_SAVE1", "CPU Register Save Size"),
(0x014, "CPU_REGF", "CPU Register Format"),
(0x016, "CPU_CS_TLB_START", "CPU/Chipset Reg Table Addr"),
(0x018, "CPU_CS_TLB_END", "CPU/Chipset Reg Table End Addr"),
(0x01A, "SMI_EXIT_OFF", "Offset for CPU SMI Return"),
(0x01C, "CPU_CS_SMI", "Code Segment for CPU SMI Return"),
(0x01E, "CPU_INIT", "CPU Init (before SMI) Routine"),
(0x020, "CPU_SMI_PREPROC", "Addr to CPU Specific SMI PreProc"),
(0x022, "CPU_CONF_SAVE","Addr to CPU Config Save"),
(0x024, "CPU_CS_CONF_SAVE", "Code Segment of CPU Config Save"),
(0x026, "CPU_CONF_REST", "Addr to CPU Config Restore"),
(0x028, "CPU_CLOCK", "Addr to CPU Clock"),
(0x02A, "CS_SMBASE", "Chipset SMbase (non-smi mode)"),
(0x02C, "PM_CS", "PM Code Segment(non-smi mode)"),
(0x02E, "PM_DS", "PM Data Segment(non-smi mode)")
)

