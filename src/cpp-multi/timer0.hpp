/**
 * @file timer0.hpp
 * @brief Timer0 C++ class for PIC16F876A
 * @author Sébastien Celles
 * @date 2025
 * @version 1.0
 *
 * @details C++ class wrapper for Timer0 configuration and management
 *          for PIC16F876A for delay generation and timing.
 *          This file will be transpiled to C using xc8plusplus.
 */

#ifndef TIMER0_HPP
#define TIMER0_HPP

#include <xc.h>

/**
 * @brief Timer0 C++ class for PIC16F876A
 * @details Provides object-oriented interface for Timer0 operations
 */
class Timer0 {
private:
    bool initialized;
    
public:
    /**
     * @brief Timer0 constructor
     * @details Initializes the Timer0 instance
     */
    Timer0();
    
    /**
     * @brief Timer0 destructor
     * @details Cleanup Timer0 resources
     */
    ~Timer0();
    
    /**
     * @brief Initialize Timer0
     * @details Configures Timer0 for timer mode operation
     *          with appropriate prescaler for 4MHz frequency
     */
    void initialize();
    
    /**
     * @brief Check if Timer0 is initialized
     * @return true if initialized, false otherwise
     */
    bool isInitialized() const;
    
    /**
     * @brief 50ms delay using Timer0
     * @details Delay function based on Timer0 for precise timing
     */
    void delay50ms();
    
    /**
     * @brief Custom delay using Timer0
     * @param milliseconds Delay time in milliseconds
     */
    void delay(unsigned int milliseconds);
    
    /**
     * @brief Start Timer0
     * @details Start the timer counting
     */
    void start();
    
    /**
     * @brief Stop Timer0
     * @details Stop the timer counting
     */
    void stop();
    
    /**
     * @brief Reset Timer0
     * @details Reset the timer counter to 0
     */
    void reset();
    
    /**
     * @brief Get Timer0 value
     * @return Current timer value
     */
    unsigned char getValue() const;
};

#endif // TIMER0_HPP
