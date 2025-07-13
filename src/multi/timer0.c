/**
 * @verbatim
 *  ____ ___ ____   _____ _____ ____ _____   
 * |  _ \_ _/ ___| |_   _| ____/ ___|_   _|  
 * | |_) | | |       | | |  _| \___ \ | |    
 * |  __/| | |___    | | | |___ ___) || |    
 * |_|__|___\____|__ |_| |_____|____/_|_|___ 
 * |  _ \|  _ \ / _ \    | | ____/ ___|_   _|
 * | |_) | |_) | | | |_  | |  _|| |     | |  
 * |  __/|  _ <| |_| | |_| | |__| |___  | |  
 * |_|   |_| \_\\___/ \___/|_____\____| |_| 
 *  
 * @endverbatim
 * @file timer0.c
 * @brief Main program for PIC16F876A microcontroller
 * @author Sébastien Celles
 * @date 2025-07-13
 * @version 0.1
 *
 * @details This program initializes a PIC16F876A-based system with:
 *          - 5 output LEDs
 *          - 3 input push buttons
 *
 */

/**
 * @name Include files (or header files)
 * @brief Headers required for program operation
 * @{
 */

/** @brief XC8 Compiler - basic functions and macros */
#include <xc.h>

/** @brief Pin definitions */
#include "pin_manager.h"

/** @brief Microcontroller configuration */
#include "device_config.h"

/** @} */

void delay_50ms_timer0(void)
{
    OPTION_REG = 0b10000111;
    TMR0IF = 0;
    TMR0 = 60;

    while (!TMR0IF);
}

/**
 * @brief System initialization function prototype
 */
void init_system(void);

/**
 * @brief Main program function
 *
 * @details This function initializes the system then enters an infinite
 *          loop for the main program operation.
 *
 * @return EXIT_SUCCESS (0) on success (although never reached in this case)
 */
int main(void)
{
    init_system();

    while (1) {
        /*
        delay_50ms_timer0();
        LED0 = !1;
        delay_50ms_timer0();
        LED0 = 0;
        */
        LED1 = !LED1;
        delay_50ms_timer0();
    }

    return EXIT_SUCCESS;
}

/**
 * @brief Complete system initialization
 *
 * @details This function configures:
 *          - Microcontroller registers (via PIN_MANAGER_Initialize())
 *          - Initial state of LEDs (all off)
 *          - Initial state of SPI signals
 *          - Initial state of MONO signal
 *
 * @note Pin assignment is done in the pin_manager.h file
 *       Initial register configuration is done in the pin_manager.c file
 *
 */
void init_system(void)
{
    /**
     * @brief Microcontroller register initialization
     */
    PIN_MANAGER_Initialize();
    /**
     * @brief Turn off all LEDs at initialization
     */
    LED0 = 0;
    LED1 = 0;
    LED2 = 0;
    LED3 = 0;
    LED4 = 0;
}