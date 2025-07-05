# PIC 16F876A Project with XC8 v3.00

## Description
Demonstration project for PIC 16F876A with 4MHz crystal using XC8 v3.00 compiler.
The program blinks LEDs connected to PORTB with different patterns.

## Project Structure
```
PIC_Test_Project/
├── src/
│   └── main.c              # Main source code
├── platformio.ini          # PlatformIO configuration (optional)
├── compile_xc8.ps1         # XC8 compilation script
├── upload_pickit3.ps1      # PICkit3 upload script
└── README.md               # This file
```

## Hardware Configuration

### Required Components
- **Microcontroller**: PIC 16F876A
- **Crystal**: 4MHz
- **Capacitors**: 2x 22pF (for crystal)
- **LEDs**: 8 LEDs for PORTB
- **Resistors**: 8x 220-470Ω (current limiting for LEDs)
- **Capacitor**: 100nF (power supply decoupling)

### Wiring Diagram
```
OSC1 ---- [4MHz Crystal] ---- OSC2
    |                       |
   [22pF]                  [22pF]
    |                       |
   GND                     GND

RB0-RB7 ---- [Resistor] ---- [LED] ---- VCC

VDD ---- [100nF] ---- VSS
VDD ---- +5V
VSS ---- GND
```

## Compilation and Programming

### Method 1: Direct compilation with XC8
```powershell
# Compile the project
.\compile_xc8.ps1

# Program with PICkit3 (optional)
.\upload_pickit3.ps1
```

### Method 2: With PlatformIO (experimental)
```bash
pio run                    # Compile
pio run -t upload         # Program
```

## Prerequisites

### Required Software
- **XC8 v3.00**: Microchip Compiler
  - Path: `C:\Program Files\Microchip\xc8\v3.00\`
- **MPLAB X IDE** (for programming): 
  - Path: `C:\Program Files\Microchip\MPLABX\v5.50\`
- **PlatformIO** (optional): `pip install platformio`

### Programming Hardware
- **PICkit3** or **PICkit4**
- **Programming socket** or development circuit

## Program Operation

The program executes a blinking sequence:
1. **Simple blinking**: All LEDs ON/OFF (1 second each)
2. **Alternating pattern**: 10101010 then 01010101 (0.5 second each)
3. **Fast blinking**: 5 fast blinks (0.1 second)
4. **Pause**: 2 seconds before repeat

## PIC Configuration

### Configuration bits (in main.c)
- `FOSC = HS`: High speed oscillator (crystal)
- `WDTE = OFF`: Watchdog disabled
- `PWRTE = OFF`: Power-up Timer disabled
- `BOREN = ON`: Brown-out Reset enabled
- `LVP = OFF`: Low Voltage Programming disabled

### Frequency
- **Crystal**: 4MHz
- **Instruction frequency**: 1MHz (Fosc/4)
- **Delays**: Calculated for 4MHz (`_XTAL_FREQ = 4000000`)

## Troubleshooting

### Compilation errors
- Check that XC8 v3.00 is installed
- Check paths in `compile_xc8.ps1`

### Programming errors
- Check PICkit3 connections
- Check circuit power supply
- Check that MPLABX is installed

### Program doesn't work
- Check 4MHz crystal and its capacitors
- Check LED connections
- Check 5V power supply

## Development

To modify the program:
1. Edit `src/main.c`
2. Compile with `.\compile_xc8.ps1`
3. Program with `.\upload_pickit3.ps1`

## Resources

- [XC8 Documentation](https://www.microchip.com/en-us/tools-resources/develop/mplab-xc-compilers)
- [PIC16F876A Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/39582b.pdf)
- [PlatformIO PIC](https://docs.platformio.org/)
