/**
 * @file button.hpp
 * @brief Button C++ class for PIC16F876A
 * @author Sébastien Celles
 * @date 2025
 * @version 1.0
 *
 * @details C++ class for managing push buttons on PIC16F876A.
 *          This file will be transpiled to C using xc8plusplus.
 */

#ifndef BUTTON_HPP
#define BUTTON_HPP

/**
 * @brief Button identifier enumeration
 */
enum class ButtonId {
    PB_0 = 0,
    PB_1 = 1,
    PB_2 = 2
};

/**
 * @brief Button state enumeration
 */
enum class ButtonState {
    RELEASED = 0,
    PRESSED = 1
};

/**
 * @brief Button C++ class for push button management
 * @details Provides object-oriented interface for button operations
 *          with debouncing and state management
 */
class Button {
private:
    ButtonId buttonId;
    ButtonState currentState;
    ButtonState previousState;
    unsigned int debounceCounter;
    static const unsigned int DEBOUNCE_THRESHOLD = 5;
    
public:
    /**
     * @brief Button constructor
     * @param id Button identifier (PB0 to PB2)
     */
    Button(ButtonId id);
    
    /**
     * @brief Button destructor
     */
    ~Button();
    
    /**
     * @brief Update button state (call regularly in main loop)
     * @details Reads hardware state and applies debouncing
     */
    void update();
    
    /**
     * @brief Check if button is currently pressed
     * @return true if pressed, false if released
     */
    bool isPressed() const;
    
    /**
     * @brief Check if button was just pressed (edge detection)
     * @return true if button transitioned from released to pressed
     */
    bool wasJustPressed();
    
    /**
     * @brief Check if button was just released (edge detection)
     * @return true if button transitioned from pressed to released
     */
    bool wasJustReleased();
    
    /**
     * @brief Get button identifier
     * @return Button identifier
     */
    ButtonId getId() const;
    
    /**
     * @brief Get current button state
     * @return Current button state (PRESSED or RELEASED)
     */
    ButtonState getState() const;
    
private:
    /**
     * @brief Read raw hardware button state
     * @return Raw button state from hardware
     */
    bool readHardwareState() const;
};

#endif // BUTTON_HPP
