/**
 * @file pin_manager.c
 * @brief Implementation of register initialization and interrupt management functions
 * @author Sébastien Celles
 * @date 2025
 * @version 1.0
 */

#include "pin_manager.h"

void PIN_MANAGER_Initialize(void)
{
    /**
    LATx registers
    */
    /**
     * TRISx registers
     * @brief Port direction configuration
     * @details 0 = Output, 1 = Input
     * TRISC must be configured according to LED and SPI signal needs
     * @todo Complete TRISC configuration according to electrical schematic
     * @warning Verify compatibility with SPI signals
     */
    TRISC = 0b00100000; // Configuration to be completed according to wiring
    /**
     * @brief Port A configuration
     * @details Must account for LEDs, push buttons and MONO signal
     * @todo Define directions according to actual wiring
     * @note Push buttons require pull-up resistors
     */
    TRISA = 0b00010110; // Configuration to be completed according to wiring
    /**
     * @brief Port B configuration
     * @details Configuration according to system needs
     * @todo Verify if port B is used in this project
     */
    TRISB = 0b00000000; // Configuration to be completed according to wiring
    /**
     * @brief Analog-to-digital converter configuration
     * @details Configure pins as digital or analog inputs
     * @todo Define which pins are analog/digital
     * @warning Default value may cause reading problems
     */
    ADCON1 = 0b00000110; // Configuration to be completed according to wiring
    /**
    ANSELx registers
    */
    /**
    WPUx registers
    */
    /**
    SLRCONx registers
    */
    /**
    APFCONx registers
    */
}

/*
void PIN_MANAGER_IOC(void)
{
    // Interrupt management routine for changes
    // This function is called when an interrupt occurs on pins.
    // It must handle the logic for specific pin changes.
    // Currently, it does nothing, but can be extended as needed.
}
*/
