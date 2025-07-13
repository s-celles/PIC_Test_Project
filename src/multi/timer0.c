/**
 * @file timer0.c
 * @brief Implementation of Timer0 functions for PIC16F876A
 * @author Sébastien Celles
 * @date 2025
 * @version 1.0
 */

#include <xc.h>
#include "timer0.h"
#include "device_config.h"

void TIMER0_Initialize(void)
{
    // Timer0 configuration
    // Prescaler 1:256, timer mode
    OPTION_REG = 0b10000111;
    TMR0 = 0;           // Initialize counter
    TMR0IF = 0;         // Clear interrupt flag
}

void delay_50ms_timer0(void)
{
    OPTION_REG = 0b10000111;
    TMR0IF = 0;
    TMR0 = 60;

    while (!TMR0IF);
}

void TIMER0_ISR(void)
{
    // Timer0 interrupt handler
    // To be implemented according to needs
    TMR0IF = 0;  // Clear interrupt flag
}