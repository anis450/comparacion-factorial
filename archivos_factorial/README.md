Comparación de eficiencia: factorial recursivo vs iterativo



Este proyecto compara dos enfoques para calcular el factorial de un número (n!):



Usando una función recursiva



Usando una función iterativa



Además, se analiza cuál es más rápida y cuál usa menos memoria, implementándolo tanto en Python como en C. Al final, se grafican los resultados para compararlos.



Objetivo:



Comprender las diferencias de eficiencia entre funciones recursivas e iterativas.



Medir el tiempo de ejecución y el uso de memoria.



Representar gráficamente los resultados.



Documentar todo el proceso en un repositorio.



Implementación:



Python – factorial.py

Incluye:



facto\_r(n): función recursiva.



facto\_i(n): función iterativa.



Uso de time y memory\_profiler para medir rendimiento.



Gráfica con matplotlib.



Exportación de datos a datos\_factorial.csv y grafico.png.



C – factorial.c

Incluye:



Las dos funciones recursiva e iterativa.



Medición del tiempo de ejecución con clock() de time.h.



Resultados:



Tiempo de ejecución:



La versión iterativa fue más rápida, especialmente con números grandes.



La versión recursiva puede generar errores por límite de recursión con valores altos.



Uso de memoria:



La versión iterativa es más estable.



La recursiva utiliza más memoria debido al uso del stack de llamadas.



Gráfico:

El archivo grafico.png muestra la comparación visual del tiempo de ejecución entre ambas funciones.



Archivos del proyecto:



factorial.py - Código en Python con funciones, medición y graficación



factorial.c - Código en C con ambas funciones y medición de tiempo



grafico.png - Imagen con la comparación de tiempos



datos\_factorial.csv - Datos generados por el script Python



README.md - Este archivo de documentación



Cómo ejecutar:



Paso 1: Instalar dependencias (Python)

pip install memory\_profiler matplotlib



Paso 2: Ejecutar el script en Python

python factorial.py

Esto genera los archivos:



datos\_factorial.csv



grafico.png



Paso 3: Compilar y ejecutar el código en C

gcc factorial.c -o factorial

./factorial



Autora:

Ana Maria Hernández Zea

Estudiante de Ingeniería en Ciencias de la Computación e Inteligencia Artificial

