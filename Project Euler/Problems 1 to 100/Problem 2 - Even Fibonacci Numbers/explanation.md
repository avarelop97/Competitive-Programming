# Project Euler — Problemas 1 y 2 (explicación + Python)

---

# Problem 1 — Multiples of 3 or 5

## Enunciado (resumen)
Sumar todos los naturales **menores que 1000** que sean múltiplos de **3 o 5**.

---

## 1) Suma de múltiplos de k bajo N como progresión aritmética
Los múltiplos positivos de \(k\) estrictamente menores que \(N\) son:

\[
k,\ 2k,\ 3k,\ \dots,\ mk
\quad\text{donde}\quad
m = \left\lfloor \frac{N-1}{k} \right\rfloor
\]

La suma es:

\[
k(1+2+\dots+m)
\]

y

\[
1+2+\dots+m=\frac{m(m+1)}{2}
\]

Por tanto:

\[
\boxed{
\text{sumMultiples}(k,N)=k\cdot\frac{m(m+1)}{2},\quad m=\left\lfloor\frac{N-1}{k}\right\rfloor
}
\]

### Por qué es correcto
Es una progresión aritmética. Factorizas \(k\) y reduces a la suma de los primeros \(m\) enteros, que se demuestra emparejando extremos \((1+m), (2+m-1), \dots\), con suma constante \(m+1\).

---

## 2) Inclusión–exclusión para evitar doble conteo
Si sumas múltiplos de 3 + múltiplos de 5, los múltiplos de 15 aparecen dos veces.

\[
\boxed{
S = \text{sumMultiples}(3,1000) + \text{sumMultiples}(5,1000) - \text{sumMultiples}(15,1000)
}
\]

---

## 3) Cálculo concreto para N = 1000
- \(m_3=\lfloor 999/3\rfloor=333\) ⇒ \(S_3=3\cdot\frac{333\cdot334}{2}=166833\)
- \(m_5=\lfloor 999/5\rfloor=199\) ⇒ \(S_5=5\cdot\frac{199\cdot200}{2}=99500\)
- \(m_{15}=\lfloor 999/15\rfloor=66\) ⇒ \(S_{15}=15\cdot\frac{66\cdot67}{2}=33165\)

\[
S=166833+99500-33165=\boxed{233168}
\]

---

## 4) Código Python (O(1))
```python
def sum_multiples(k: int, N: int) -> int:
    """
    Suma de los múltiplos positivos de k estrictamente menores que N.
    """
    m = (N - 1) // k
    return k * m * (m + 1) // 2

def euler1(N: int = 1000) -> int:
    return sum_multiples(3, N) + sum_multiples(5, N) - sum_multiples(15, N)

print(euler1(1000))  # 233168
```

---

# Problem 2 — Even Fibonacci Numbers

## Enunciado (resumen)
Dada la sucesión de Fibonacci empezando en \(1,2\):

\[
1,2,3,5,8,13,21,34,\dots
\]

Sumar los términos **pares** cuya magnitud **no excede** 4.000.000.

---

## 1) Hecho clave: la paridad en Fibonacci es periódica (periodo 3)
Trabajamos “módulo 2” (par/impar). Como:

\[
F_n = F_{n-1} + F_{n-2}
\]

la paridad queda determinada por las dos anteriores. Con \(F_1=1\) (impar), \(F_2=2\) (par):

\[
1,\ 0,\ 1,\ 1,\ 0,\ 1,\ 1,\ 0,\dots
\]

Se repite cada 3 ⇒ **uno de cada tres** es par.

Equivalente:

\[
F_n \text{ es par } \Longleftrightarrow n \equiv 2 \pmod 3
\]

Esto ya permite optimizar: no hace falta filtrar todos los términos.

---

## 2) Subsucesión de pares y su recurrencia propia
Definimos la subsecuencia de pares:

\[
E_1 = 2,\ E_2 = 8,\ E_3 = 34,\dots
\]

Se cumple:

\[
\boxed{
E_k = 4E_{k-1} + E_{k-2}
}
\]

### Fundamentación (por qué existe esa recurrencia)
Fibonacci es un sistema lineal. Al quedarte con cada 3er término (los pares), estás muestreando una dinámica lineal que sigue siendo lineal ⇒ tiene una recurrencia de orden 2.

Una forma formal de verlo es con Binet en el Fibonacci clásico \(G_n\):

\[
G_n=\frac{\varphi^n-\psi^n}{\sqrt5}
\]

y los pares corresponden a \(G_{3k}\):

\[
E_k = G_{3k} = \frac{(\varphi^3)^k-(\psi^3)^k}{\sqrt5}
\]

Toda secuencia \(\alpha^k\) satisface una recurrencia con polinomio característico \(x^2-(\alpha+\beta)x+\alpha\beta\). Aquí \(\alpha=\varphi^3\), \(\beta=\psi^3\):

- \(\alpha+\beta = \varphi^3+\psi^3 = 4\)
- \(\alpha\beta = (\varphi\psi)^3 = (-1)^3 = -1\)

Por tanto:

\[
E_k = 4E_{k-1} -(-1)E_{k-2} = 4E_{k-1}+E_{k-2}
\]

---

## 3) Algoritmo eficiente
Generas **solo pares**:
- Inicializa \(E_1=2\), \(E_2=8\)
- Repite \(E_{next}=4E_2+E_1\) mientras \(E \le 4{,}000{,}000\)

Complejidad: \(O(\#\text{pares})\), que crece como \(O(\log \text{límite})\).

---

## 4) Código Python (generando solo pares)
```python
def sum_even_fib(limit: int = 4_000_000) -> int:
    # E1=2, E2=8
    e_prev, e = 2, 8
    total = 2  # incluye E1

    while e <= limit:
        total += e
        e_prev, e = e, 4 * e + e_prev

    return total

print(sum_even_fib())  # 4613732
```

Resultado:

\[
\boxed{4613732}
\]

---

## Nota final de eficiencia
- “Naive”: generar todos los Fibonacci hasta el límite y filtrar pares.
- “Óptimo”: explotar estructura (periodicidad de paridad + recurrencia para pares) y generar solo lo necesario.
