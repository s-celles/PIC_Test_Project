/**
 * @file led.cpp
 * @brief LED C++ class implementation for PIC16F876A
 * @author Sébastien Celles
 * @date 2025
 * @version 1.0
 *
 * @details Implementation of LED C++ class for PIC16F876A.
 *          This file will be transpiled to C using xc8plusplus.
 */

#include "led.hpp"
#include "pin_manager.h"
#include "device_config.h"
#include <xc.h>

Led::Led(LedId id) : ledId(id), state(false) {
    // Constructor - turn off LED initially
    turnOff();
}

Led::~Led() {
    // Destructor - turn off LED
    turnOff();
}

void Led::turnOn() {
    state = true;
    
    // Set appropriate hardware pin based on LED ID
    switch (ledId) {
        case LedId::LED_0:
            LED0 = 1;
            break;
        case LedId::LED_1:
            LED1 = 1;
            break;
        case LedId::LED_2:
            LED2 = 1;
            break;
        case LedId::LED_3:
            LED3 = 1;
            break;
        case LedId::LED_4:
            LED4 = 1;
            break;
    }
}

void Led::turnOff() {
    state = false;
    
    // Clear appropriate hardware pin based on LED ID
    switch (ledId) {
        case LedId::LED_0:
            LED0 = 0;
            break;
        case LedId::LED_1:
            LED1 = 0;
            break;
        case LedId::LED_2:
            LED2 = 0;
            break;
        case LedId::LED_3:
            LED3 = 0;
            break;
        case LedId::LED_4:
            LED4 = 0;
            break;
    }
}

void Led::toggle() {
    if (state) {
        turnOff();
    } else {
        turnOn();
    }
}

void Led::setState(bool newState) {
    if (newState) {
        turnOn();
    } else {
        turnOff();
    }
}

bool Led::isOn() const {
    return state;
}

LedId Led::getId() const {
    return ledId;
}

void Led::blink(unsigned int count, unsigned int delayMs) {
    for (unsigned int i = 0; i < count; i++) {
        turnOn();
        __delay_ms(delayMs);
        turnOff();
        __delay_ms(delayMs);
    }
}
