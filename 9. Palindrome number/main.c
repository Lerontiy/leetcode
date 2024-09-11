#include <stdio.h>
#include <stdbool.h>

unsigned char length(int);
bool isPalindrome(int);


int main() {
    int x = 0;
    bool isp = isPalindrome(x);
    printf("\nisp: %d", isp);
    
    return 0;
}

   
unsigned char length(int num) {
    if (num/1000000000 >= 1) return 10;
    if (num/100000000 >= 1) return 9;
    if (num/10000000 >= 1) return 8;
    if (num/1000000 >= 1) return 7;
    if (num/100000 >= 1) return 6;
    if (num/10000 >= 1) return 5;
    if (num/1000 >= 1) return 4;
    if (num/100 >= 1) return 3;
    if (num/10 >= 1) return 2;
    return 1;
} 

bool isPalindrome(int num){
    if (num < 0) return false;

    //char num_length = length(num);
    int num_array[length(num)+1];
    //sprintf(array_num, "%d", x);
    int num_help = num;

    while (length(num)>0 & num!=0) {
        //printf("\n%d", length(num));
        num_help = (num_help/10)*10;

        //printf("\n%d %d %d %d", num_length, num, num_help, num-num_help);
        num_array[length(num)-1] = num-num_help;
        
        num = num_help = num_help/10;
    }
    
    unsigned char index1 = 0;
    unsigned char index2 = (sizeof(num_array)/sizeof(num_array[0]))-2;
    //printf("\n%d", index2);
    
    while (index1 < index2) {
        //printf("\n%d %d", num_array[index1], num_array[index2]);
        if (num_array[index1] != num_array[index2]) return false;
        index1++;
        index2--;
    }
    
    return true;
}
    