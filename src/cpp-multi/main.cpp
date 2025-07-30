/**
 * @file main.cpp
 * @brief Main C++ program for PIC16F876A
 * @author Sébastien Celles
 * @date 2025
 * @version 1.0
 *
 * @details C++ test program for PIC16F876A with LED and button management
 *          Uses device_config, pin_manager, Timer0, Led and Button classes
 *          This file will be transpiled to C using xc8plusplus
 */

#include <xc.h>
#include "device_config.h"
#include "pin_manager.h"
#include "timer0.hpp"
#include "led.hpp"
#include "button.hpp"

// Global instances - Arduino style
Timer0 timer;
Led led0(LedId::LED_0);
Led led1(LedId::LED_1);
Led led2(LedId::LED_2);
Led led3(LedId::LED_3);
Led led4(LedId::LED_4);
Button button0(ButtonId::PB_0);
Button button1(ButtonId::PB_1);
Button button2(ButtonId::PB_2);

/**
 * @brief Setup function - Arduino style initialization
 * @details Called once at startup to initialize the system
 */
void setup(void) {
    // System initialization
    PIN_MANAGER_Initialize();
    
    // Initialize Timer0
    timer.initialize();
    
    // Ensure all LEDs are off initially
    led0.turnOff();
    led1.turnOff();
    led2.turnOff();
    led3.turnOff();
    led4.turnOff();
}

/**
 * @brief Loop function - Arduino style main loop
 * @details Called repeatedly - contains the main program logic
 */
void loop(void) {
    // Update button states (for debouncing)
    button0.update();
    button1.update();
    button2.update();
    
    // LED test - blinking sequence using C++ methods
    led0.turnOn();
    __delay_ms(100);
    led0.turnOff();
    
    led1.turnOn();
    __delay_ms(100);
    led1.turnOff();
    
    led2.turnOn();
    __delay_ms(100);
    led2.turnOff();
    
    led3.turnOn();
    __delay_ms(100);
    led3.turnOff();
    
    led4.turnOn();
    __delay_ms(100);
    led4.turnOff();
    
    // Pause between sequences
    __delay_ms(500);
    
    // Button test using C++ button objects
    if (button0.isPressed()) {
        led0.turnOn();
        led1.turnOn();
    } else {
        led0.turnOff();
        led1.turnOff();
    }
    
    if (button1.isPressed()) {
        led2.turnOn();
        led3.turnOn();
    } else {
        led2.turnOff();
        led3.turnOff();
    }
    
    if (button2.isPressed()) {
        led4.turnOn();
    } else {
        led4.turnOff();
    }
    
    // Demonstrate edge detection
    if (button0.wasJustPressed()) {
        // Button 0 was just pressed - blink LED4 3 times
        led4.blink(3, 50);
    }
    
    if (button1.wasJustPressed()) {
        // Button 1 was just pressed - toggle LED0
        led0.toggle();
    }
    
    // Use Timer0 for some delays
    if (button2.wasJustPressed()) {
        // Button 2 was just pressed - use Timer0 delay
        timer.delay(200);
        led0.turnOn();
        led1.turnOn();
        led2.turnOn();
        led3.turnOn();
        led4.turnOn();
        timer.delay(200);
        led0.turnOff();
        led1.turnOff();
        led2.turnOff();
        led3.turnOff();
        led4.turnOff();
    }

    // Small delay to prevent excessive polling
    __delay_ms(10);
}
