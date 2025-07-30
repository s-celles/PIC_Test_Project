/**
 * @file led.hpp
 * @brief LED C++ class for PIC16F876A
 * @author Sébastien Celles
 * @date 2025
 * @version 1.0
 *
 * @details C++ class for managing individual LEDs on PIC16F876A.
 *          This file will be transpiled to C using xc8plusplus.
 */

#ifndef LED_HPP
#define LED_HPP

/**
 * @brief LED identifier enumeration
 */
enum class LedId {
    LED_0 = 0,
    LED_1 = 1,
    LED_2 = 2,
    LED_3 = 3,
    LED_4 = 4
};

/**
 * @brief LED C++ class for individual LED control
 * @details Provides object-oriented interface for LED operations
 */
class Led {
private:
    LedId ledId;
    bool state;
    
public:
    /**
     * @brief LED constructor
     * @param id LED identifier (LED0 to LED4)
     */
    Led(LedId id);
    
    /**
     * @brief LED destructor
     */
    ~Led();
    
    /**
     * @brief Turn LED on
     */
    void turnOn();
    
    /**
     * @brief Turn LED off
     */
    void turnOff();
    
    /**
     * @brief Toggle LED state
     */
    void toggle();
    
    /**
     * @brief Set LED state
     * @param newState true for on, false for off
     */
    void setState(bool newState);
    
    /**
     * @brief Get current LED state
     * @return true if LED is on, false if off
     */
    bool isOn() const;
    
    /**
     * @brief Get LED identifier
     * @return LED identifier
     */
    LedId getId() const;
    
    /**
     * @brief Blink LED
     * @param count Number of blinks
     * @param delayMs Delay between blinks in milliseconds
     */
    void blink(unsigned int count, unsigned int delayMs);
};

#endif // LED_HPP
