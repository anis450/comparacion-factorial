import time
import pandas as pd
import matplotlib.pyplot as plt
from memory_profiler import memory_usage

def facto_i(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def facto_r(n):
    if n == 0 or n == 1:
        return 1
    return n * facto_r(n - 1)

if __name__ == "__main__":
    datos = []
    valores = range(1, 21)

    for n in valores:
        
        start = time.time()
        mem_i = memory_usage((facto_i, (n,)), max_usage=True)
        duracion_i = time.time() - start

        
        start = time.time()
        mem_r = memory_usage((facto_r, (n,)), max_usage=True)
        duracion_r = time.time() - start

        datos.append({
            "n": n,
            "tiempo_iterativo": duracion_i,
            "memoria_iterativa": mem_i,
            "tiempo_recursivo": duracion_r,
            "memoria_recursiva": mem_r
        })

    
    df = pd.DataFrame(datos)
    df.to_csv("datos_factorial.csv", index=False)

    
    plt.plot(df["n"], df["tiempo_iterativo"], label="Iterativo")
    plt.plot(df["n"], df["tiempo_recursivo"], label="Recursivo")
    plt.xlabel("n")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación de tiempo de ejecución")
    plt.legend()
    plt.savefig("grafico.png")
    plt.show()
