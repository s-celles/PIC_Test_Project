/**
 * @file main.c
 * @brief Programme principal pour PIC16F876A
 * @author Sébastien Celles
 * @date 2025
 * @version 1.0
 *
 * @details Programme de test pour PIC16F876A avec gestion des LEDs et boutons
 *          Utilise les modules device_config, pin_manager et timer0
 */

#include <xc.h>
#include "device_config.h"
#include "pin_manager.h"
#include "timer0.h"

/**
 * @brief Programme principal
 * @details Initialise le système et exécute la boucle principale
 */
void main(void) {
    // Initialisation du système
    PIN_MANAGER_Initialize();
    TIMER0_Initialize();
    
    // Boucle principale
    while(1) {
        // Test des LEDs - séquence de clignotement
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
        
        // Pause entre les séquences
        __delay_ms(500);
        
        // Test des boutons
        if (PB0 == 0) {  // Bouton pressé (logique inversée avec pull-up)
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
