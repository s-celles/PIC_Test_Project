# C++ Multi-Module Example for PIC16F876A

This example demonstrates C++ programming for PIC microcontrollers using the **xc8plusplus** transpiler concept. The C++ code is transpiled to C code that can be compiled with the XC8 compiler.

## Overview

This project showcases:
- **Object-oriented PIC programming** using C++ classes
- **Automatic C++ to C transpilation** using xc8plusplus Python API
- **Multi-module architecture** with separate classes for different components
- **Hardware abstraction** through C++ classes

## Project Structure

```
cpp-multi/
├── C++ Source Files (Original):
│   ├── main.cpp           # Main program using C++ classes
│   ├── led.hpp/.cpp       # LED class for hardware abstraction
│   ├── button.hpp/.cpp    # Button class with debouncing
│   ├── timer0.hpp/.cpp    # Timer0 class for precise timing
│   ├── device_config.h    # PIC configuration (kept as C)
│   └── pin_manager.h      # Pin definitions (kept as C)
│
├── Generated C Files (Transpiled):
│   └── generated_c/       # Transpiled C code ready for XC8
│       ├── main.c         # Transpiled main function
│       ├── led.h/.c       # LED struct and functions
│       ├── button.h/.c    # Button struct and functions
│       ├── timer0.h/.c    # Timer0 struct and functions
│       ├── device_config.h # Copied unchanged
│       └── pin_manager.h   # Copied unchanged
│
└── Transpilation Scripts:
    ├── transpile.py       # xc8plusplus Python API usage
    └── manual_transpile.py # Manual transpilation (demo)
```

## C++ Classes

### Led Class
- **Purpose**: Hardware abstraction for individual LEDs
- **Features**: Turn on/off, toggle, blink patterns, state management
- **Hardware**: Controls LED0-LED4 on PORTA and PORTC

### Button Class  
- **Purpose**: Debounced button input with edge detection
- **Features**: Press detection, edge detection, automatic debouncing
- **Hardware**: Reads PB0-PB2 on PORTA with pull-up resistors

### Timer0 Class
- **Purpose**: Precise timing and delay generation
- **Features**: 50ms delays, custom delays, timer control
- **Hardware**: Uses PIC16F876A Timer0 with prescaler

## Transpilation Process

The xc8plusplus transpiler converts C++ concepts to C:

| C++ Feature | C Equivalent |
|-------------|--------------|
| `class Led` | `struct Led` + `Led_*` functions |
| `Led::turnOn()` | `Led_turnOn(Led* self)` |
| `enum class LedId` | `typedef enum LedId_t` |
| Constructor | `Led_init(Led* self, ...)` |
| Destructor | `Led_cleanup(Led* self)` |

## Usage

### 1. Write C++ Code
```cpp
// Create LED object
Led led0(LedId::LED_0);

// Use object-oriented interface
led0.turnOn();
led0.blink(3, 100);
if (led0.isOn()) {
    led0.toggle();
}
```

### 2. Transpile to C
```bash
# Using xc8plusplus Python API
python transpile.py

# Or using manual transpilation (demonstration)
python manual_transpile.py
```

### 3. Generated C Code
```c
// Transpiled C code
Led led0;
Led_init(&led0, LED_0);

// Object-oriented calls become function calls
Led_turnOn(&led0);
Led_blink(&led0, 3, 100);
if (Led_isOn(&led0)) {
    Led_toggle(&led0);
}
```

## Hardware Configuration

- **Microcontroller**: PIC16F876A
- **Clock**: 4MHz external crystal (1MHz instruction cycle)
- **LEDs**: 5 LEDs on PORTA/PORTC pins
- **Buttons**: 3 push buttons on PORTA with pull-ups
- **Timer**: Timer0 with 1:256 prescaler for timing

## Pin Assignments

| Component | Pin | Port |
|-----------|-----|------|
| LED0 | RA3 | PORTA |
| LED1 | RA5 | PORTA |
| LED2 | RC0 | PORTC |
| LED3 | RC1 | PORTC |
| LED4 | RC2 | PORTC |
| PB0 | RA2 | PORTA |
| PB1 | RA1 | PORTA |
| PB2 | RA4 | PORTA |

## Key Features Demonstrated

1. **C++ Classes → C Structs**: Object-oriented design transpiled to procedural C
2. **Method Calls → Function Calls**: `obj.method()` becomes `Class_method(&obj)`
3. **Encapsulation**: Private data members become struct fields
4. **Inheritance Simulation**: Base functionality through function pointers
5. **Constructor/Destructor**: Initialization and cleanup functions
6. **Type Safety**: Strong typing preserved through typedefs

## Build Process

The transpiled C code integrates seamlessly with the existing PIC build system:

1. **Transpilation**: C++ → C using xc8plusplus
2. **Compilation**: C files compiled with XC8 compiler
3. **Linking**: Standard PIC linking process
4. **Programming**: Upload to PIC16F876A

## Benefits of This Approach

- **Modern C++ features** for embedded development
- **Object-oriented design** for complex projects
- **Code reusability** through class-based architecture
- **Type safety** and compile-time checking
- **Maintainable code** with clear separation of concerns
- **XC8 compatibility** through automatic transpilation

## Comparison with Original C Code

| Aspect | Original C (src/multi) | C++ Version (cpp-multi) |
|--------|------------------------|--------------------------|
| Architecture | Procedural | Object-oriented |
| Code Organization | Functions + globals | Classes + encapsulation |
| Hardware Abstraction | Direct register access | Class-based HAL |
| State Management | Global variables | Object member variables |
| Code Reuse | Copy/paste functions | Instantiate classes |
| Type Safety | Limited | Strong typing |

This example demonstrates how C++ can enhance embedded development while maintaining full compatibility with existing PIC toolchains through automatic transpilation.
