#include <stdio.h>

int main() {
    int i = 1234567890;

    unsigned char s = sizeof(i);

    printf("\n%d", s);

    int l[s];

    unsigned char s1 = sizeof(l);

    printf("\n%d", s1);

    return 0;
}
