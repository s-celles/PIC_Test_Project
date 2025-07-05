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

// Define crystal frequency (4MHz)
#define _XTAL_FREQ 4000000

void main(void) {
    // Port configuration
    TRISB = 0x00;           // Port B configured as output (all pins)
    PORTB = 0x00;           // Initialize port B to 0
    
    // ADC configuration (disable to save power)
    ADCON1 = 0x06;          // All AN pins as digital I/O
    
    // Main loop
    while(1) {
        // Blinking sequence optimized for 4MHz
        
        // Simple blinking
        PORTB = 0xFF;           // Turn on all LEDs
        __delay_ms(1000);       // Wait 1 second
        PORTB = 0x00;           // Turn off all LEDs
        __delay_ms(1000);       // Wait 1 second
        
        // Alternating blink pattern
        PORTB = 0xAA;           // 10101010
        __delay_ms(500);
        PORTB = 0x55;           // 01010101
        __delay_ms(500);
        
        // Fast blinking
        for(int i = 0; i < 5; i++) {
            PORTB = 0xFF;
            __delay_ms(100);
            PORTB = 0x00;
            __delay_ms(100);
        }
        
        __delay_ms(2000);       // 2 second pause before repeat
    }
}

/*
 * Hardware configuration for 4MHz:
 * - 4MHz crystal between OSC1/OSC2 with 22pF capacitors
 * - LEDs on PORTB with current limiting resistors (220-470 ohms)
 * - 100nF decoupling capacitor on VDD/VSS
 * - 10k pull-up resistor on MCLR if used
 * 
 * Note: With 4MHz, delays are more precise for small values
 * Maximum recommended __delay_ms(): 1000ms to avoid overflows
 */
