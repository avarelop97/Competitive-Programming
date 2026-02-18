#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int a, b;

    while (scanf("%d %d", &a, &b) == 2) {
        int diff, ans;

        if (a == 0 && b == 0) break;

        diff = a - b;
        if (diff < 0) diff = -diff;

        ans = diff;
        if (99 - diff < ans) ans = 99 - diff;

        printf("%d\n", ans);
    }

    return 0;
}