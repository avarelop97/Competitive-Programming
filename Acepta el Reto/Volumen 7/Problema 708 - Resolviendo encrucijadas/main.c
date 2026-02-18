#include <stdio.h>

typedef unsigned long long ull;

typedef struct {
    ull cnt;   /* cuántos números válidos */
    ull sum;   /* suma total de sumDigits sobre esos números */
} Node;

/* -------- fast input -------- */
static int read_ll(long long *out) {
    int c = getchar_unlocked();
    long long x = 0;

    while (c != EOF && c <= ' ') c = getchar_unlocked();
    if (c == EOF) return 0;

    while (c > ' ') {
        x = x * 10 + (c - '0');
        c = getchar_unlocked();
    }
    *out = x;
    return 1;
}

/* -------- digit DP -------- */
static int digits[32];
static int len;

static Node memo[32][3];
static char vis[32][3];

static Node dfs(int pos, int mod, int tight) {
    Node res;
    int limit, d;

    if (pos == len) {
        res.cnt = (mod == 0) ? 1ULL : 0ULL;
        res.sum = 0ULL;
        return res;
    }

    if (!tight && vis[pos][mod]) return memo[pos][mod];

    limit = tight ? digits[pos] : 9;
    res.cnt = 0ULL;
    res.sum = 0ULL;

    for (d = 0; d <= limit; ++d) {
        Node sub = dfs(pos + 1, (mod * 10 + d) % 3, tight && (d == limit));
        res.cnt += sub.cnt;
        res.sum += sub.sum + (ull)d * sub.cnt;
    }

    if (!tight) {
        vis[pos][mod] = 1;
        memo[pos][mod] = res;
    }
    return res;
}

static ull G(long long n) {
    int i;
    Node ans;

    if (n < 0) return 0ULL;

    /* construir dígitos de n en base 10 */
    if (n == 0) {
        digits[0] = 0;
        len = 1;
    } else {
        int tmp[32];
        int k = 0;
        long long x = n;
        while (x > 0) {
            tmp[k++] = (int)(x % 10);
            x /= 10;
        }
        len = k;
        for (i = 0; i < len; ++i) digits[i] = tmp[len - 1 - i];
    }

    /* limpiar memo para este len */
    for (i = 0; i <= len; ++i) {
        vis[i][0] = vis[i][1] = vis[i][2] = 0;
    }

    ans = dfs(0, 0, 1);
    return ans.sum;
}

int main(void) {
    long long a, b;

    while (read_ll(&a)) {
        if (!read_ll(&b)) break;
        if (a == 0 && b == 0) break;

        /* respuesta = G(b) - G(a-1) */
        {
            ull right = G(b);
            ull left  = G(a - 1);
            ull ans = right - left;
            printf("%llu\n", ans);
        }
    }
    return 0;
}