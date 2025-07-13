/**
 * @file timer0.h
 * @brief Timer0 configuration and management for PIC16F876A
 * @author Sébastien Celles
 * @date 2025
 * @version 1.0
 *
 * @details This file contains configuration and management functions
 *          for PIC16F876A Timer0 for delay generation and timing.
 */

#ifndef TIMER0_H
#define TIMER0_H

#include <xc.h>

/**
 * @brief Timer0 initialization
 * @details Configures Timer0 for timer mode operation
 *          with appropriate prescaler for 4MHz frequency
 */
void TIMER0_Initialize(void);

/**
 * @brief 50ms delay using Timer0
 * @details Delay function based on Timer0 for precise timing
 */
void delay_50ms_timer0(void);

/**
 * @brief Timer0 interrupt service routine
 * @details Function called when Timer0 interrupt occurs
 *          Must be defined by user according to needs
 */
void TIMER0_ISR(void);

#endif // TIMER0_H
