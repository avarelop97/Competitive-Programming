# Project Euler (Register) — Problem Zero: Sum of Odd Squares Among the First *N* Squares

## Enunciado (resumen)
Considera los primeros *N* números cuadrados:

\[
1^2, 2^2, 3^2, \dots, N^2
\]

Se pide la suma de **los cuadrados impares** dentro de esa lista.

---

## 1) Hecho clave: un cuadrado es impar ⇔ su base es impar

Para cualquier entero \(k\):

- Si \(k\) es **par**, \(k = 2t\) ⇒ \(k^2 = (2t)^2 = 4t^2\) ⇒ **par**.
- Si \(k\) es **impar**, \(k = 2t-1\) ⇒ \(k^2\) es **impar** (en módulo 2, \(1^2 \equiv 1\)).

**Conclusión:**  
Dentro de \(1^2,\dots,N^2\), los “odd squares” son exactamente:

\[
1^2, 3^2, 5^2, \dots
\]

hasta el mayor impar \(\le N\).

---

## 2) Cuántos términos impares hay entre 1 y N

El número de impares en \(\{1,2,\dots,N\}\) es:

\[
m = \left\lceil \frac{N}{2} \right\rceil
\]

En enteros, esto se implementa como:

\[
m = \frac{N+1}{2}\ \text{(división entera)}\quad\Rightarrow\quad m = (N+1)//2
\]

---

## 3) Reindexación: escribir los impares como \(2k-1\)

Los impares positivos son:

\[
1, 3, 5, \dots, (2m-1)
\]

Así que la suma pedida es:

\[
S = \sum_{k=1}^{m} (2k-1)^2
\]

---

## 4) Derivación de fórmula cerrada (sin bucles)

Expansión:

\[
(2k-1)^2 = 4k^2 - 4k + 1
\]

Aplicamos linealidad de la suma:

\[
S = \sum_{k=1}^{m} (4k^2 - 4k + 1)
  = 4\sum_{k=1}^{m} k^2\ -\ 4\sum_{k=1}^{m} k\ +\ \sum_{k=1}^{m} 1
\]

Usamos identidades clásicas:

\[
\sum_{k=1}^{m} 1 = m,\qquad
\sum_{k=1}^{m} k = \frac{m(m+1)}{2},\qquad
\sum_{k=1}^{m} k^2 = \frac{m(m+1)(2m+1)}{6}
\]

Sustituyendo:

\[
S = 4\cdot\frac{m(m+1)(2m+1)}{6}\ -\ 4\cdot\frac{m(m+1)}{2}\ +\ m
\]

Simplificamos coeficientes:

\[
S = \frac{2}{3}m(m+1)(2m+1) - 2m(m+1) + m
\]

Se simplifica (factorizando y reduciendo) a:

\[
\boxed{
S = \frac{m(2m-1)(2m+1)}{3}
}
\]

---

## 5) Por qué la división entre 3 es exacta (integridad)
El numerador:

\[
m(2m-1)(2m+1) = m(4m^2-1) = 4m^3 - m
\]

Módulo 3, \(4 \equiv 1\), así que:

\[
4m^3 - m \equiv m^3 - m = m(m^2-1)=m(m-1)(m+1)\pmod 3
\]

Pero \(m-1, m, m+1\) son 3 enteros consecutivos ⇒ uno es múltiplo de 3 ⇒ el producto es múltiplo de 3 ⇒ la división es exacta.

---

## 6) Código Python (O(1))
```python
def sum_odd_squares_among_first_n_squares(n: int) -> int:
    """
    Among the first n square numbers (1^2..n^2), return the sum of the odd squares.
    Odd squares are exactly squares of odd integers <= n.
    """
    m = (n + 1) // 2  # count of odd integers in [1..n]
    return m * (2 * m - 1) * (2 * m + 1) // 3
```

---

## 7) Casos resueltos en la conversación

### Caso A: N = 718_000
- \(m = (718000+1)//2 = 359000\)
- Resultado:

\[
\boxed{61691038666547000}
\]

### Caso B: N = 839_000
- \(m = (839000+1)//2 = 419500\)
- Resultado:

\[
\boxed{98431619833193500}
\]

---

## 8) Nota de eficiencia
- Solución ingenua: iterar \(k=1..N\), filtrar impares y sumar \(k^2\) ⇒ \(O(N)\).
- Solución derivada: 3 multiplicaciones + 1 división ⇒ \(O(1)\).

El salto conceptual es: (i) **caracterizar el conjunto** (paridad), (ii) **reindexar**, (iii) usar **sumas polinómicas** + linealidad.
