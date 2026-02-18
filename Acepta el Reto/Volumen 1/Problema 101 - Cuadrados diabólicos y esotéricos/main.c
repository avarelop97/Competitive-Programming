#include <stdio.h>
#include <stdlib.h>

/* -------- fast input -------- */
#define BUFSIZE (1 << 16)
static unsigned char buf[BUFSIZE];
static size_t buf_len = 0, buf_pos = 0;

static int read_byte(void) {
    if (buf_pos >= buf_len) {
        buf_len = fread(buf, 1, BUFSIZE, stdin);
        buf_pos = 0;
        if (buf_len == 0) return EOF;
    }
    return (int)buf[buf_pos++];
}

static int read_ll(long long *out) {
    int c;
    long long x;
    int sign;

    c = read_byte();
    while (c != EOF && c <= ' ') c = read_byte();
    if (c == EOF) return 0;

    sign = 1;
    if (c == '-') {
        sign = -1;
        c = read_byte();
    }

    x = 0;
    while (c != EOF && c > ' ') {
        x = x * 10 + (c - '0');
        c = read_byte();
    }

    *out = x * (long long)sign;
    return 1;
}

/* -------- bitset helpers -------- */
static int bitset_get(unsigned char *bs, int idx) {
    return (bs[idx >> 3] & (unsigned char)(1u << (idx & 7))) != 0;
}
static void bitset_set(unsigned char *bs, int idx) {
    bs[idx >> 3] |= (unsigned char)(1u << (idx & 7));
}

int main(void) {
    long long nll;

    while (read_ll(&nll)) {
        int n;
        int i, j;

        n = (int)nll;
        if (n == 0) break;

        /* n up to 1024 */
        {
            int total = n * n;
            int bytes = (total + 7) / 8;

            long long *col = (long long *)calloc((size_t)n, sizeof(long long));
            unsigned char *seen = (unsigned char *)calloc((size_t)bytes, 1);

            int diabolico = 1;
            int set_ok = 1;
            int unique = 0;

            long long cm = -1;
            long long diag1 = 0, diag2 = 0;

            long long corners = 0;
            long long mids_odd = 0;     /* odd: 4 mid-side cells */
            long long center_val = 0;   /* odd: center cell */
            long long center4 = 0;      /* even: 4 center cells */
            long long mids_even8 = 0;   /* even: 8 side-center cells */

            int mid = n / 2;
            int mid1 = (n / 2) - 1;
            int mid2 = (n / 2);

            for (i = 0; i < n; ++i) {
                long long row = 0;

                for (j = 0; j < n; ++j) {
                    long long v;

                    read_ll(&v);

                    row += v;
                    col[j] += v;

                    if (i == j) diag1 += v;
                    if (i + j == n - 1) diag2 += v;

                    /* corners */
                    if ((i == 0 || i == n - 1) && (j == 0 || j == n - 1)) {
                        corners += v;
                    }

                    /* parity-specific cells */
                    if (n & 1) {
                        if ((i == 0 && j == mid) ||
                            (i == n - 1 && j == mid) ||
                            (i == mid && j == 0) ||
                            (i == mid && j == n - 1)) {
                            mids_odd += v;
                        }
                        if (i == mid && j == mid) center_val = v;
                    } else {
                        if ((i == mid1 || i == mid2) && (j == mid1 || j == mid2)) {
                            center4 += v;
                        }
                        if ((i == 0 || i == n - 1) && (j == mid1 || j == mid2)) {
                            mids_even8 += v;
                        }
                        if ((j == 0 || j == n - 1) && (i == mid1 || i == mid2)) {
                            mids_even8 += v;
                        }
                    }

                    /* check set {1..n^2} */
                    if (set_ok) {
                        if (v < 1 || v > (long long)total) {
                            set_ok = 0;
                        } else {
                            int idx = (int)v - 1;
                            if (bitset_get(seen, idx)) {
                                set_ok = 0;
                            } else {
                                bitset_set(seen, idx);
                                unique++;
                            }
                        }
                    }
                }

                if (cm < 0) cm = row;
                else if (row != cm) diabolico = 0;
            }

            /* validate cols + diagonals */
            if (diabolico) {
                for (j = 0; j < n; ++j) {
                    if (col[j] != cm) {
                        diabolico = 0;
                        break;
                    }
                }
                if (diabolico && (diag1 != cm || diag2 != cm)) diabolico = 0;
            }

            if (!diabolico) {
                puts("NO");
            } else {
                int esoterico = 1;

                /* condition 1: exactly 1..n^2 */
                if (!set_ok || unique != total) esoterico = 0;

                /* avoid division: CM2 = (4*CM)/n, so check X*n == 4*CM */
                if (esoterico) {
                    long long rhs4 = 4LL * cm;

                    /* condition 2: corners sum == CM2 */
                    if (corners * (long long)n != rhs4) esoterico = 0;

                    if (esoterico) {
                        if (n & 1) {
                            /* odd:
                               mid-side 4 cells sum == CM2  => mids_odd*n == 4*CM
                               center*4 == CM2 => center*n == CM
                            */
                            if (mids_odd * (long long)n != rhs4) esoterico = 0;
                            if (center_val * (long long)n != cm) esoterico = 0;
                        } else {
                            /* even:
                               center4 sum == CM2 => center4*n == 4*CM
                               8 side-center cells sum == 2*CM2 => mids_even8*n == 8*CM
                            */
                            if (center4 * (long long)n != rhs4) esoterico = 0;
                            if (mids_even8 * (long long)n != 8LL * cm) esoterico = 0;
                        }
                    }
                }

                if (esoterico) puts("ESOTERICO");
                else puts("DIABOLICO");
            }

            free(col);
            free(seen);
        }
    }

    return 0;
}