/**
 * @file main.c
 * @brief Main program for PIC16F876A
 * @author Sébastien Celles
 * @date 2025
 * @version 1.0
 *
 * @details Test program for PIC16F876A with LED and button management
 *          Uses device_config, pin_manager and timer0 modules
 */

#include <xc.h>
#include "device_config.h"
#include "pin_manager.h"
#include "timer0.h"

/**
 * @brief Main program
 * @details Initializes the system and runs the main loop
 */
void main(void) {
    // System initialization
    PIN_MANAGER_Initialize();
    TIMER0_Initialize();

    LED0 = 0;
    LED1 = 0;
    LED2 = 0;
    LED3 = 0;
    LED4 = 0;        
    // Main loop
    while(1) {
        // LED test - blinking sequence
        LED0 = 1;
        __delay_ms(100);
        LED0 = 0;
        
        LED1 = 1;
        __delay_ms(100);
        LED1 = 0;
        
        LED2 = 1;
        __delay_ms(100);
        LED2 = 0;
        
        LED3 = 1;
        __delay_ms(100);
        LED3 = 0;
        
        LED4 = 1;
        __delay_ms(100);
        LED4 = 0;
        
        // Pause between sequences
        __delay_ms(500);
        
        // Button test
        if (PB0 == 0) {  // Button pressed (inverted logic with pull-up)
            LED0 = 1;
            LED1 = 1;
        } else {
            LED0 = 0;
            LED1 = 0;
        }
        
        if (PB1 == 0) {
            LED2 = 1;
            LED3 = 1;
        } else {
            LED2 = 0;
            LED3 = 0;
        }
        
        if (PB2 == 0) {
            LED4 = 1;
        } else {
            LED4 = 0;
        }
    }
}
