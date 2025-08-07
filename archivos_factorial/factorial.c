
#include <stdio.h>
#include <time.h>

unsigned long long facto_i(int n) {
    unsigned long long resultado = 1;
    for (int i = 2; i <= n; i++) {
        resultado *= i;
    }
    return resultado;
}

unsigned long long facto_r(int n) {
    if (n == 0 || n == 1)
        return 1;
    return n * facto_r(n - 1);
}

int main() {
    int n = 20;
    clock_t start, end;
    double tiempo;

    start = clock();
    printf("Iterativo (%d!): %llu\n", n, facto_i(n));
    end = clock();
    tiempo = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Tiempo iterativo: %f segundos\n", tiempo);

    start = clock();
    printf("Recursivo (%d!): %llu\n", n, facto_r(n));
    end = clock();
    tiempo = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Tiempo recursivo: %f segundos\n", tiempo);

    return 0;
}
