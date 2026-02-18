#include <stdio.h>

int main(void) {
    int S;

    while (scanf("%d", &S) == 1 && S != 0) {
        int q = S / 9;
        int r = S % 9;
        int i;

        if (r != 0) {
            putchar('0' + r);  /* r está en 1..8 */
        }
        for (i = 0; i < q; ++i) {
            putchar('9');
        }
        putchar('\n');
    }

    return 0;
}