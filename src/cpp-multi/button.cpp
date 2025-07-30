/**
 * @file button.cpp
 * @brief Button C++ class implementation for PIC16F876A
 * @author Sébastien Celles
 * @date 2025
 * @version 1.0
 *
 * @details Implementation of Button C++ class for PIC16F876A.
 *          This file will be transpiled to C using xc8plusplus.
 */

#include "button.hpp"
#include "pin_manager.h"
#include <xc.h>

Button::Button(ButtonId id) 
    : buttonId(id), currentState(ButtonState::RELEASED), 
      previousState(ButtonState::RELEASED), debounceCounter(0) {
    // Constructor - initialize button state
}

Button::~Button() {
    // Destructor - nothing special to clean up
}

void Button::update() {
    // Read raw hardware state
    bool rawPressed = readHardwareState();
    
    // Convert raw state to ButtonState (inverted logic with pull-up)
    ButtonState rawState = rawPressed ? ButtonState::RELEASED : ButtonState::PRESSED;
    
    // Debouncing logic
    if (rawState == currentState) {
        // State is stable, reset counter
        debounceCounter = 0;
    } else {
        // State changed, increment counter
        debounceCounter++;
        
        // If counter reaches threshold, accept the new state
        if (debounceCounter >= DEBOUNCE_THRESHOLD) {
            previousState = currentState;
            currentState = rawState;
            debounceCounter = 0;
        }
    }
}

bool Button::isPressed() const {
    return currentState == ButtonState::PRESSED;
}

bool Button::wasJustPressed() {
    // Edge detection: was released, now pressed
    if (previousState == ButtonState::RELEASED && currentState == ButtonState::PRESSED) {
        previousState = currentState; // Reset edge detection
        return true;
    }
    return false;
}

bool Button::wasJustReleased() {
    // Edge detection: was pressed, now released
    if (previousState == ButtonState::PRESSED && currentState == ButtonState::RELEASED) {
        previousState = currentState; // Reset edge detection
        return true;
    }
    return false;
}

ButtonId Button::getId() const {
    return buttonId;
}

ButtonState Button::getState() const {
    return currentState;
}

bool Button::readHardwareState() const {
    // Read appropriate hardware pin based on button ID
    switch (buttonId) {
        case ButtonId::PB_0:
            return (PB0 == 1);
        case ButtonId::PB_1:
            return (PB1 == 1);
        case ButtonId::PB_2:
            return (PB2 == 1);
        default:
            return false;
    }
}
