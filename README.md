# 🚦 PIC 16F876A Project with XC8 v3.00

A demonstration project for the PIC 16F876A (4MHz crystal) using the XC8 v3.00 compiler and PlatformIO. The program blinks LEDs connected to the microcontroller.

## 📦 Quick Start

1. **Install prerequisites:** Python 3.x, XC8 v3.00, MPLAB X IDE
2. **Install wrappers:**
   ```bash
   pip install git+https://github.com/s-celles/xc8-wrapper.git
   pip install git+https://github.com/s-celles/ipecmd-wrapper.git
   ```
3. **Install PlatformIO:** [platformio.org/install](https://platformio.org/install)
4. **Build:** `pio run`
5. **Upload:** `pio run --target upload` (with programmer connected)

## 🛠️ Hardware
- **MCU:** PIC 16F876A
- **Crystal:** 4MHz + 2×22pF
- **LEDs:** 8× (PORTB)
- **Resistors:** 8× 220–470Ω
- **Capacitor:** 100nF (decoupling)
- **Programmer:** PICkit3, PICkit4, or PICkit5

## 🐍 Python Wrappers
- [`xc8-wrapper`](https://github.com/s-celles/xc8-wrapper) ([docs](https://s-celles.github.io/xc8-wrapper/)) — XC8 toolchain
- [`ipecmd-wrapper`](https://github.com/s-celles/ipecmd-wrapper) ([docs](https://s-celles.github.io/ipecmd-wrapper/)) — MPLAB IPE command-line

## ⚡ PlatformIO Platform
- [`platform-pic8bit`](https://github.com/s-celles/platform-pic8bit) ([docs](https://s-celles.github.io/platform-pic8bit/)) — PlatformIO for 8-bit PIC

## 📄 License & Legal
- **This project:** Apache 2.0
- **Wrappers:** MIT
- **Microchip tools:** Proprietary (get your own license)

> ⚠️ You are responsible for obtaining proper licenses for any Microchip tools you use with these wrappers.

## 🔗 Resources
- [XC8 Documentation](https://www.microchip.com/en-us/tools-resources/develop/mplab-xc-compilers)
- [PIC16F876A Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/39582b.pdf)
- [MPLAB X IDE](https://www.microchip.com/en-us/tools-resources/develop/mplab-x-ide)

---

<div align="center">

Made with ❤️ by [Sébastien Celles](https://github.com/s-celles) for the PIC developer community.

</div>
