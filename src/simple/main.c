/*
 * PIC 16F876A Project with PlatformIO
 * 4MHz Crystal - LED Blinking on PORTB
 */

#include <xc.h>

// Configuration bits for PIC16F876A with 4MHz crystal
#pragma config FOSC = HS        // HS oscillator (high speed crystal)
#pragma config WDTE = OFF       // Watchdog Timer disabled
#pragma config PWRTE = OFF      // Power-up Timer disabled
#pragma config BOREN = ON       // Brown-out Reset enabled
#pragma config LVP = OFF        // Low Voltage Programming disabled
#pragma config CPD = OFF        // Data EEPROM Memory Code Protection disabled
#pragma config WRT = OFF        // Flash Program Memory Write Enable disabled
#pragma config CP = OFF         // Flash Program Memory Code Protection disabled

/** Define crystal frequency (4MHz) */
#define _XTAL_FREQ 4000000

#define LED4 PORTCbits.RC2
#define LED3 PORTCbits.RC1
#define LED2 PORTCbits.RC0
#define LED1 PORTAbits.RA5
#define LED0 PORTAbits.RA3

#define BUT0 PORTAbits.RA2
#define BUT1 PORTAbits.RA1
#define BUT2 PORTAbits.RA4

void main(void) {
    TRISC = 0b00100000;
    TRISA = 0b00010110;
    TRISB = 0b00000000;
    ADCON1 = 0b00000110;

    LED0 = 0;
    LED1 = 0;
    LED2 = 0;
    LED3 = 0;
    LED4 = 0;

    // Main loop
    while(1) {
        // Blinking sequence
        LED2 = !LED2;        
        __delay_ms(500);       // 500 ms before toggle
    }
}
