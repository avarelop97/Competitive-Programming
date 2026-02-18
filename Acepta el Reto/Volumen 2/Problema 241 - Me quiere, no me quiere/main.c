#include <stdio.h>

int main(void) {
    int T;
    if (scanf("%d", &T) != 1) return 0;

    while (T--) {
        int N;
        int r;
        if (scanf("%d", &N) != 1) break;

        r = N % 3;

        if (r == 0) {
            puts("0");
        } else if (r == 1) {
            if (N >= 4) puts("1");
            else puts("IMPOSIBLE");
        } else { /* r == 2 */
            if (N >= 8) puts("2");
            else puts("IMPOSIBLE");
        }
    }
    return 0;
}