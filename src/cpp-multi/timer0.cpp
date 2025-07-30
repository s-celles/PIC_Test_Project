/**
 * @file timer0.cpp
 * @brief Timer0 C++ class implementation for PIC16F876A
 * @author Sébastien Celles
 * @date 2025
 * @version 1.0
 *
 * @details Implementation of Timer0 C++ class for PIC16F876A.
 *          This file will be transpiled to C using xc8plusplus.
 */

#include "timer0.hpp"
#include "device_config.h"

Timer0::Timer0() : initialized(false) {
    // Constructor - initialization will be done in initialize() method
}

Timer0::~Timer0() {
    // Destructor - stop timer if it was running
    if (initialized) {
        stop();
    }
}

void Timer0::initialize() {
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
    
    initialized = true;
}

bool Timer0::isInitialized() const {
    return initialized;
}

void Timer0::delay50ms() {
    if (!initialized) {
        return;
    }
    
    // For 50ms delay with 4MHz clock (1MHz instruction cycle) and 1:256 prescaler:
    // Timer0 increments every 256 instruction cycles = 256µs
    // For 50ms delay: 50000µs / 256µs = 195.3 ≈ 195 counts
    // Load Timer0 with (256 - 195) = 61
    
    TMR0 = 61;                  // Load Timer0 for 50ms delay
    INTCONbits.T0IF = 0;        // Clear overflow flag
    
    while (!INTCONbits.T0IF) {  // Wait for Timer0 overflow
        // Wait for overflow
    }
    
    INTCONbits.T0IF = 0;        // Clear overflow flag
}

void Timer0::delay(unsigned int milliseconds) {
    if (!initialized) {
        return;
    }
    
    // Delay using multiple 50ms delays for accuracy
    unsigned int fiftyMsCount = milliseconds / 50;
    unsigned int remainder = milliseconds % 50;
    
    // Perform 50ms delays
    for (unsigned int i = 0; i < fiftyMsCount; i++) {
        delay50ms();
    }
    
    // Handle remainder using proportional calculation
    if (remainder > 0) {
        // Calculate Timer0 load value for remainder
        // remainder ms = remainder * 1000µs
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

void Timer0::start() {
    if (initialized) {
        OPTION_REGbits.T0CS = 0;    // Ensure Timer0 uses internal clock
    }
}

void Timer0::stop() {
    if (initialized) {
        OPTION_REGbits.T0CS = 1;    // Stop Timer0 by switching to external clock
    }
}

void Timer0::reset() {
    if (initialized) {
        TMR0 = 0;
        INTCONbits.T0IF = 0;
    }
}

unsigned char Timer0::getValue() const {
    if (initialized) {
        return TMR0;
    }
    return 0;
}
