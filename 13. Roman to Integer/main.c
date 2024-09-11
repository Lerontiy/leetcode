#include <stdio.h>
#include <string.h>

int romanToInt(char[10]);

int main() {
    char all_romans[][10] = {"XV", "III", "LVIII", "MCMXCIV"};
    unsigned char all_romans_length = sizeof(all_romans)/sizeof(all_romans[0]);
    short all_decimals[] = {15, 3, 58, 1994};
    
    printf("\nlen: %d", all_romans_length);

    for (unsigned char i; i<all_romans_length; i++){

        int decimal_roman = romanToInt(all_romans[i]);

        printf("\nans #%d (%d): %d", i, all_decimals[i], decimal_roman);
    }

    return 0;
}

int romanToInt(char *roman) {
    //printf("\n%d", sizeof(roman));

    //printf("\n%c%c", roman[0], roman[1]);
    unsigned char roman_length = strlen(roman);
    unsigned char index = 0;
    int decimal = 0;

    short all_decimals[] =  {1,   5,  10,  50,  100, 500, 1000};
    char all_romans[] =    {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
    unsigned char all_length = sizeof(all_romans)/sizeof(all_romans[0]);

    char previous_roman_index = -1;
    
    while (index < roman_length) {
        for (unsigned char current_roman_index=0; current_roman_index<all_length; current_roman_index++) {
            if (roman[index] == all_romans[current_roman_index]) {
                //printf("\ncurr: %d, index: %d", current_roman_index, index);
                //printf("\nall_d[?]: %d", all_decimals[current_roman_index]);
                //printf("\nprev: %d", previous_roman_index);
                if (previous_roman_index < 0 || previous_roman_index >= current_roman_index) {
                    decimal += all_decimals[current_roman_index];
                } else if (previous_roman_index < current_roman_index) {
                    decimal = (decimal - all_decimals[previous_roman_index]) + (all_decimals[current_roman_index] - all_decimals[previous_roman_index]);
                }
                //printf("\ndec: %d", decimal);
                previous_roman_index = current_roman_index;
            }
        }
        
        index++;
    }
    //printf("\n%u", length);

    return decimal;
}