#include <stdio.h>
#include <stdlib.h>

static int is_repdigit_4(int x) {
    int d0 = x % 10; x /= 10;
    int d1 = x % 10; x /= 10;
    int d2 = x % 10; x /= 10;
    int d3 = x % 10;
    return (d0 == d1 && d1 == d2 && d2 == d3);
}

static int kaprekar_step(int x) {
    int d[4];
    d[0] = x % 10; x /= 10;
    d[1] = x % 10; x /= 10;
    d[2] = x % 10; x /= 10;
    d[3] = x % 10;

    // ordenar ascendente (4 elementos -> burbuja simple)
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (d[j] > d[j + 1]) {
                int tmp = d[j];
                d[j] = d[j + 1];
                d[j + 1] = tmp;
            }
        }
    }

    int asc  = d[0]*1000 + d[1]*100 + d[2]*10 + d[3];
    int desc = d[3]*1000 + d[2]*100 + d[1]*10 + d[0];
    return desc - asc;
}

int main(void) {
    int T;
    if (scanf("%d", &T) != 1) return 0;

    char s[64];
    while (T--) {
        if (scanf("%63s", s) != 1) break;
        int x = atoi(s);                // ok: los ceros a la izquierda no afectan
        if (x < 0) x = -x;              // por si acaso, aunque no debería ocurrir
        x %= 10000;                     // asegurar 0..9999

        if (x == 6174) {
            puts("0");
            continue;
        }
        if (is_repdigit_4(x)) {
            puts("8");
            continue;
        }

        int cnt = 0;
        while (x != 6174) {
            x = kaprekar_step(x);
            cnt++;
        }
        printf("%d\n", cnt);
    }
    return 0;
}