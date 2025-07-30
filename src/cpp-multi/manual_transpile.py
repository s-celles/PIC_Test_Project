#!/usr/bin/env python3
"""
Manual C++ to C transpilation for cpp-multi project
Creates hand-optimized C code that demonstrates the xc8plusplus concept
"""

import os
from pathlib import Path


def create_manual_transpiled_c():
    """Create manually transpiled C files from C++ sources"""

    # Define source and output directories
    cpp_multi_dir = Path(__file__).parent
    output_dir = cpp_multi_dir / "generated_c"

    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)

    print("*** Manual C++ to C Transpilation for cpp-multi project")
    print("=" * 55)
    print(f"Source directory: {cpp_multi_dir}")
    print(f"Output directory: {output_dir}")
    print()

    # Create transpiled timer0.c
    timer0_c = """/*
 * XC8 C++ to C Transpilation - Timer0
 * Generated using manual transpilation to demonstrate xc8plusplus concept
 * Original C++ class: Timer0
 */

#include <stdint.h>
#include <stdbool.h>
#include <xc.h>
#include "device_config.h"
#include "timer0.h"

// === Class Timer0 transformed to C ===

// Constructor for Timer0
void Timer0_init(Timer0* self) {
    self->initialized = false;
}

// Destructor for Timer0
void Timer0_cleanup(Timer0* self) {
    if (self->initialized) {
        Timer0_stop(self);
    }
}

// Method: initialize
void Timer0_initialize(Timer0* self) {
    // Configure Timer0
    // Timer0 configuration for 4MHz oscillator (1MHz instruction cycle)
    // Prescaler 1:256, Timer0 = internal clock
    
    OPTION_REGbits.T0CS = 0;    // Timer0 clock source = internal instruction cycle
    OPTION_REGbits.T0SE = 0;    // Timer0 source edge = increment on low-to-high transition
    OPTION_REGbits.PSA = 0;     // Prescaler assigned to Timer0
    OPTION_REGbits.PS2 = 1;     // Prescaler rate select bits
    OPTION_REGbits.PS1 = 1;     // 111 = 1:256 prescaler
    OPTION_REGbits.PS0 = 1;
    
    TMR0 = 0;                   // Clear Timer0 register
    INTCONbits.T0IF = 0;        // Clear Timer0 interrupt flag
    
    self->initialized = true;
}

// Method: isInitialized
bool Timer0_isInitialized(Timer0* self) {
    return self->initialized;
}

// Method: delay50ms
void Timer0_delay50ms(Timer0* self) {
    if (!self->initialized) {
        return;
    }
    
    // For 50ms delay with 4MHz clock (1MHz instruction cycle) and 1:256 prescaler:
    // Timer0 increments every 256 instruction cycles = 256us
    // For 50ms delay: 50000us / 256us = 195.3 approx 195 counts
    // Load Timer0 with (256 - 195) = 61
    
    TMR0 = 61;                  // Load Timer0 for 50ms delay
    INTCONbits.T0IF = 0;        // Clear overflow flag
    
    while (!INTCONbits.T0IF) {  // Wait for Timer0 overflow
        // Wait for overflow
    }
    
    INTCONbits.T0IF = 0;        // Clear overflow flag
}

// Method: delay
void Timer0_delay(Timer0* self, unsigned int milliseconds) {
    if (!self->initialized) {
        return;
    }
    
    // Delay using multiple 50ms delays for accuracy
    unsigned int fiftyMsCount = milliseconds / 50;
    unsigned int remainder = milliseconds % 50;
    
    // Perform 50ms delays
    for (unsigned int i = 0; i < fiftyMsCount; i++) {
        Timer0_delay50ms(self);
    }
    
    // Handle remainder using proportional calculation
    if (remainder > 0) {
        // Calculate Timer0 load value for remainder
        // remainder ms = remainder * 1000us
        // Timer0 counts needed = (remainder * 1000) / 256
        unsigned int counts = (remainder * 1000) / 256;
        if (counts > 255) counts = 255;
        
        TMR0 = 256 - counts;
        INTCONbits.T0IF = 0;
        
        while (!INTCONbits.T0IF) {
            // Wait for overflow
        }
        
        INTCONbits.T0IF = 0;
    }
}

// Method: start
void Timer0_start(Timer0* self) {
    if (self->initialized) {
        OPTION_REGbits.T0CS = 0;    // Ensure Timer0 uses internal clock
    }
}

// Method: stop
void Timer0_stop(Timer0* self) {
    if (self->initialized) {
        OPTION_REGbits.T0CS = 1;    // Stop Timer0 by switching to external clock
    }
}

// Method: reset
void Timer0_reset(Timer0* self) {
    if (self->initialized) {
        TMR0 = 0;
        INTCONbits.T0IF = 0;
    }
}

// Method: getValue
unsigned char Timer0_getValue(Timer0* self) {
    if (self->initialized) {
        return TMR0;
    }
    return 0;
}
"""

    # Create transpiled led.c
    led_c = """/*
 * XC8 C++ to C Transpilation - LED
 * Generated using manual transpilation to demonstrate xc8plusplus concept
 * Original C++ class: Led
 */

#include <stdint.h>
#include <stdbool.h>
#include <xc.h>
#include "device_config.h"
#include "pin_manager.h"
#include "led.h"

// === Class Led transformed to C ===

// Constructor for Led
void Led_init(Led* self, LedId_t id) {
    self->ledId = id;
    self->state = false;
    Led_turnOff(self);
}

// Destructor for Led
void Led_cleanup(Led* self) {
    Led_turnOff(self);
}

// Method: turnOn
void Led_turnOn(Led* self) {
    self->state = true;
    
    // Set appropriate hardware pin based on LED ID
    switch (self->ledId) {
        case LED_0:
            LED0 = 1;
            break;
        case LED_1:
            LED1 = 1;
            break;
        case LED_2:
            LED2 = 1;
            break;
        case LED_3:
            LED3 = 1;
            break;
        case LED_4:
            LED4 = 1;
            break;
    }
}

// Method: turnOff
void Led_turnOff(Led* self) {
    self->state = false;
    
    // Clear appropriate hardware pin based on LED ID
    switch (self->ledId) {
        case LED_0:
            LED0 = 0;
            break;
        case LED_1:
            LED1 = 0;
            break;
        case LED_2:
            LED2 = 0;
            break;
        case LED_3:
            LED3 = 0;
            break;
        case LED_4:
            LED4 = 0;
            break;
    }
}

// Method: toggle
void Led_toggle(Led* self) {
    if (self->state) {
        Led_turnOff(self);
    } else {
        Led_turnOn(self);
    }
}

// Method: setState
void Led_setState(Led* self, bool newState) {
    if (newState) {
        Led_turnOn(self);
    } else {
        Led_turnOff(self);
    }
}

// Method: isOn
bool Led_isOn(Led* self) {
    return self->state;
}

// Method: getId
LedId_t Led_getId(Led* self) {
    return self->ledId;
}

// Method: blink
void Led_blink(Led* self, unsigned int count, unsigned int delayMs) {
    for (unsigned int i = 0; i < count; i++) {
        Led_turnOn(self);
        __delay_ms(delayMs);
        Led_turnOff(self);
        __delay_ms(delayMs);
    }
}
"""

    # Create transpiled button.c
    button_c = """/*
 * XC8 C++ to C Transpilation - Button
 * Generated using manual transpilation to demonstrate xc8plusplus concept
 * Original C++ class: Button
 */

#include <stdint.h>
#include <stdbool.h>
#include <xc.h>
#include "pin_manager.h"
#include "button.h"

// === Class Button transformed to C ===

// Constructor for Button
void Button_init(Button* self, ButtonId_t id) {
    self->buttonId = id;
    self->currentState = BUTTON_RELEASED;
    self->previousState = BUTTON_RELEASED;
    self->debounceCounter = 0;
}

// Destructor for Button
void Button_cleanup(Button* self) {
    // Nothing special to clean up
}

// Method: update
void Button_update(Button* self) {
    // Read raw hardware state
    bool rawPressed = Button_readHardwareState(self);
    
    // Convert raw state to ButtonState (inverted logic with pull-up)
    ButtonState_t rawState = rawPressed ? BUTTON_RELEASED : BUTTON_PRESSED;
    
    // Debouncing logic
    if (rawState == self->currentState) {
        // State is stable, reset counter
        self->debounceCounter = 0;
    } else {
        // State changed, increment counter
        self->debounceCounter++;
        
        // If counter reaches threshold, accept the new state
        if (self->debounceCounter >= BUTTON_DEBOUNCE_THRESHOLD) {
            self->previousState = self->currentState;
            self->currentState = rawState;
            self->debounceCounter = 0;
        }
    }
}

// Method: isPressed
bool Button_isPressed(Button* self) {
    return self->currentState == BUTTON_PRESSED;
}

// Method: wasJustPressed
bool Button_wasJustPressed(Button* self) {
    // Edge detection: was released, now pressed
    if (self->previousState == BUTTON_RELEASED && self->currentState == BUTTON_PRESSED) {
        self->previousState = self->currentState; // Reset edge detection
        return true;
    }
    return false;
}

// Method: wasJustReleased
bool Button_wasJustReleased(Button* self) {
    // Edge detection: was pressed, now released
    if (self->previousState == BUTTON_PRESSED && self->currentState == BUTTON_RELEASED) {
        self->previousState = self->currentState; // Reset edge detection
        return true;
    }
    return false;
}

// Method: getId
ButtonId_t Button_getId(Button* self) {
    return self->buttonId;
}

// Method: getState
ButtonState_t Button_getState(Button* self) {
    return self->currentState;
}

// Private method: readHardwareState
bool Button_readHardwareState(Button* self) {
    // Read appropriate hardware pin based on button ID
    switch (self->buttonId) {
        case PB_0:
            return (PB0 == 1);
        case PB_1:
            return (PB1 == 1);
        case PB_2:
            return (PB2 == 1);
        default:
            return false;
    }
}
"""

    # Create transpiled main.c
    main_c = """/*
 * XC8 C++ to C Transpilation - Main
 * Generated using manual transpilation to demonstrate xc8plusplus concept
 * Original C++ main function
 */

#include <stdint.h>
#include <stdbool.h>
#include <xc.h>
#include "device_config.h"
#include "pin_manager.h"
#include "timer0.h"
#include "led.h"
#include "button.h"

/**
 * @brief Main C program (transpiled from C++)
 * @details Initializes the system and runs the main loop using transpiled C++ classes
 */
void main(void) {
    // System initialization
    PIN_MANAGER_Initialize();
    
    // Create Timer0 instance and initialize
    Timer0 timer;
    Timer0_init(&timer);
    Timer0_initialize(&timer);
    
    // Create LED instances
    Led led0, led1, led2, led3, led4;
    Led_init(&led0, LED_0);
    Led_init(&led1, LED_1);
    Led_init(&led2, LED_2);
    Led_init(&led3, LED_3);
    Led_init(&led4, LED_4);
    
    // Create Button instances
    Button button0, button1, button2;
    Button_init(&button0, PB_0);
    Button_init(&button1, PB_1);
    Button_init(&button2, PB_2);
    
    // Ensure all LEDs are off initially
    Led_turnOff(&led0);
    Led_turnOff(&led1);
    Led_turnOff(&led2);
    Led_turnOff(&led3);
    Led_turnOff(&led4);
    
    // Main loop
    while(1) {
        // Update button states (for debouncing)
        Button_update(&button0);
        Button_update(&button1);
        Button_update(&button2);
        
        // LED test - blinking sequence using transpiled C++ methods
        Led_turnOn(&led0);
        __delay_ms(100);
        Led_turnOff(&led0);
        
        Led_turnOn(&led1);
        __delay_ms(100);
        Led_turnOff(&led1);
        
        Led_turnOn(&led2);
        __delay_ms(100);
        Led_turnOff(&led2);
        
        Led_turnOn(&led3);
        __delay_ms(100);
        Led_turnOff(&led3);
        
        Led_turnOn(&led4);
        __delay_ms(100);
        Led_turnOff(&led4);
        
        // Pause between sequences
        __delay_ms(500);
        
        // Button test using transpiled C++ button objects
        if (Button_isPressed(&button0)) {
            Led_turnOn(&led0);
            Led_turnOn(&led1);
        } else {
            Led_turnOff(&led0);
            Led_turnOff(&led1);
        }
        
        if (Button_isPressed(&button1)) {
            Led_turnOn(&led2);
            Led_turnOn(&led3);
        } else {
            Led_turnOff(&led2);
            Led_turnOff(&led3);
        }
        
        if (Button_isPressed(&button2)) {
            Led_turnOn(&led4);
        } else {
            Led_turnOff(&led4);
        }
        
        // Demonstrate edge detection
        if (Button_wasJustPressed(&button0)) {
            // Button 0 was just pressed - blink LED4 3 times
            Led_blink(&led4, 3, 50);
        }
        
        if (Button_wasJustPressed(&button1)) {
            // Button 1 was just pressed - toggle LED0
            Led_toggle(&led0);
        }
        
        // Use Timer0 for some delays
        if (Button_wasJustPressed(&button2)) {
            // Button 2 was just pressed - use Timer0 delay
            Timer0_delay(&timer, 200);
            Led_turnOn(&led0);
            Led_turnOn(&led1);
            Led_turnOn(&led2);
            Led_turnOn(&led3);
            Led_turnOn(&led4);
            Timer0_delay(&timer, 200);
            Led_turnOff(&led0);
            Led_turnOff(&led1);
            Led_turnOff(&led2);
            Led_turnOff(&led3);
            Led_turnOff(&led4);
        }
        
        // Small delay to prevent excessive polling
        __delay_ms(10);
    }
}
"""

    # Create C header files
    timer0_h = """/*
 * XC8 C++ to C Transpilation - Timer0 Header
 * Generated using manual transpilation to demonstrate xc8plusplus concept
 * Original C++ class: Timer0
 */

#ifndef TIMER0_H
#define TIMER0_H

#include <stdint.h>
#include <stdbool.h>

// Timer0 struct (transpiled from C++ class)
typedef struct Timer0 {
    bool initialized;
} Timer0;

// Function prototypes (transpiled from C++ methods)
void Timer0_init(Timer0* self);
void Timer0_cleanup(Timer0* self);
void Timer0_initialize(Timer0* self);
bool Timer0_isInitialized(Timer0* self);
void Timer0_delay50ms(Timer0* self);
void Timer0_delay(Timer0* self, unsigned int milliseconds);
void Timer0_start(Timer0* self);
void Timer0_stop(Timer0* self);
void Timer0_reset(Timer0* self);
unsigned char Timer0_getValue(Timer0* self);

#endif // TIMER0_H
"""

    led_h = """/*
 * XC8 C++ to C Transpilation - LED Header
 * Generated using manual transpilation to demonstrate xc8plusplus concept
 * Original C++ class: Led
 */

#ifndef LED_H
#define LED_H

#include <stdint.h>
#include <stdbool.h>

// LED identifier enumeration (transpiled from C++ enum class)
typedef enum {
    LED_0 = 0,
    LED_1 = 1,
    LED_2 = 2,
    LED_3 = 3,
    LED_4 = 4
} LedId_t;

// Led struct (transpiled from C++ class)
typedef struct Led {
    LedId_t ledId;
    bool state;
} Led;

// Function prototypes (transpiled from C++ methods)
void Led_init(Led* self, LedId_t id);
void Led_cleanup(Led* self);
void Led_turnOn(Led* self);
void Led_turnOff(Led* self);
void Led_toggle(Led* self);
void Led_setState(Led* self, bool newState);
bool Led_isOn(Led* self);
LedId_t Led_getId(Led* self);
void Led_blink(Led* self, unsigned int count, unsigned int delayMs);

#endif // LED_H
"""

    button_h = """/*
 * XC8 C++ to C Transpilation - Button Header
 * Generated using manual transpilation to demonstrate xc8plusplus concept
 * Original C++ class: Button
 */

#ifndef BUTTON_H
#define BUTTON_H

#include <stdint.h>
#include <stdbool.h>

// Button identifier enumeration (transpiled from C++ enum class)
typedef enum {
    PB_0 = 0,
    PB_1 = 1,
    PB_2 = 2
} ButtonId_t;

// Button state enumeration (transpiled from C++ enum class)
typedef enum {
    BUTTON_RELEASED = 0,
    BUTTON_PRESSED = 1
} ButtonState_t;

// Button debounce threshold
#define BUTTON_DEBOUNCE_THRESHOLD 5

// Button struct (transpiled from C++ class)
typedef struct Button {
    ButtonId_t buttonId;
    ButtonState_t currentState;
    ButtonState_t previousState;
    unsigned int debounceCounter;
} Button;

// Function prototypes (transpiled from C++ methods)
void Button_init(Button* self, ButtonId_t id);
void Button_cleanup(Button* self);
void Button_update(Button* self);
bool Button_isPressed(Button* self);
bool Button_wasJustPressed(Button* self);
bool Button_wasJustReleased(Button* self);
ButtonId_t Button_getId(Button* self);
ButtonState_t Button_getState(Button* self);
bool Button_readHardwareState(Button* self);

#endif // BUTTON_H
"""

    # Write all files
    files = {
        "timer0.c": timer0_c,
        "led.c": led_c,
        "button.c": button_c,
        "main.c": main_c,
        "timer0.h": timer0_h,
        "led.h": led_h,
        "button.h": button_h,
    }

    for filename, content in files.items():
        output_file = output_dir / filename
        output_file.write_text(content, encoding="utf-8")
        print(f"[OK] Created: {filename}")

    # Copy device_config.h and pin_manager.h
    for h_file in ["device_config.h", "pin_manager.h"]:
        src_file = cpp_multi_dir / h_file
        dst_file = output_dir / h_file
        if src_file.exists():
            dst_file.write_text(src_file.read_text(encoding="utf-8"), encoding="utf-8")
            print(f"[OK] Copied: {h_file}")

    print()
    print("*** Manual transpilation completed!")
    print(f"Generated C files are in: {output_dir}")
    print()
    print("This demonstrates the xc8plusplus concept:")
    print("   * C++ classes -> C structs + functions")
    print("   * C++ methods -> C functions with self parameter")
    print("   * C++ enums -> C typedefs")
    print("   * C++ constructors/destructors -> init/cleanup functions")


if __name__ == "__main__":
    create_manual_transpiled_c()
