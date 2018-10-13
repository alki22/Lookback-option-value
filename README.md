# Modelos Matemáticos en Finanzas Cuantitativas - Trabajo práctico 1

## Introducción
---------------
El trabajo consiste en obtener el valor de una opción call de tipo _Lookback_ dados los valores para los parámetros _S0_, _u_, _d_, _tasa de interés_ y _cantidad de periódos_ a través de dos metodos:
- Montecarlo
- Árbol binomial

Además se comparará la eficiencia de ambos según distintos criterios.

## Métodos utilizados
---------------------
### Método de Montecarlo
Consiste en generar trayectorias aleatorias para aproximar la prima de la opción en base a _S0_. Esto mediante variables aleatorias binomiales, que en caso de ser 1 hacen que el precio suba y 0 que baje, para luego aproximar la esperanza del valor del subyacente en base a los valores obtenidos y calcular la prima de la opción en _t=0_, dada por __1/(1+i)^n * E(Vt)__.
Se modificó además el algoritmo para calcular la media y varianza recursivamente, deteniéndose éste cuando el error de las simulaciones sea menor a 0.001

### Método de árbol binomial
Para este método se diseñó una estructura para implementar al árbol binomial y a sus nodos. Consiste en crear un árbol de _n_ niveles, con _n_ nodos por nivel, esto da un total de _n(n+1)/2_ nodos. Luego llenaremos los valores para cada nodo en cada nivel con el valor del subyacente correspondiente. Luego recorreremos con _BFS_ el arbol, llenando para cada nodo una lista con los valores mínimos del subyacente y su probabilidad de ocurrir obtenidos de sus padres en el árbol. Finalmente obtenemos la esperanza para el valor de _Vt_ y obtenemos _V0_ aplicando la misma fórmula que en el método de Montecarlo.

## Complejidad Algorítmica
--------------------------
### Método de Montecarlo
Para este método la complejidad estará dada por los siguientes procedimientos:
- Realizar __m__ simulaciones
- En cada simulación computar una trayectoria del precio de la acción en __n__ períodos. En cada período sólo se genera una variable aleatoria binomial para decidir el camino y se almacena el valor mínimo del subyacente en la trayectoria, estas tareas son __0(1)__

Lo cual nos da una complejidad de __m*n__

### Método de árbol binomial
Complejidad dada por:
- Crear y llenar un árbol con n(n+1)/2 ≈ __n²__ nodos
- Recorrer trayectorias de longitud igual a la cantidad de períodos = __n__
- Realizar comparaciones para los mínimos, con complejidad __O(1)__

Por lo que, despreciando las constantes inferiores, nos queda una complejidad de __n²__ 

## Ejecución
------------
### Ejemplo

Para comparar el funcionamiento de ambos métodos, realizaremos una prueba para __n=30 períodos__ con los parámetros __S0 = 1__, __u = 1.1__, __d = 0.9__, __tasa de interés efectiva = 0.025__ . Y para el primer método buscaremos un __margen de error__ menor a __0.001__, dado que en este método no obtenemos un valor exacto, sino que lo aproximamos. Tendremos en cuenta el resultado obtenido en cada caso, el tiempo de ejecución usando el comando _time_ de Linux .

### Resultados

| Método  |      Resultado      |  Tiempo de ejecución | N° de simulaciones
|----------|:-------------:|------:|----:|
| Montecarlo |  0.5917354729923145 | 14.025s | 1185723 |
| Árbol binomial |    0.5848972562822754   | 0.273s  | X |




## Conclusión
-------------
Dados los resultados obtenidos, podemos concluir que:
- El primer método es conveniente en cuanto a facilidad de programación. Sin embargo, cuando se busca obtener resultados con un margen de error muy pequeño, se requiere un número muy elevado de simulaciones. En este ejemplo, para obtener un margen de error menor a __0.001__ debieron realizarse __1285723 simulaciones__, tardando así aproximadamente 52 veces lo que tarda el método del árbol binomial para obtener un valor __aproximado__. Sin embargo, considerando el tiempo que se tardó en implementar ambos métodos, si el margen de error utilizado se ajusta bien a nuestro problema, el primer método es más conveniente.
- El segundo método, si bien requirió mucho más tiempo en cuanto a implementación de las estructuras y sus algoritmos, prueba ser mucho más eficiente y escalable en una cantidad más elevada de períodos, con un tiempo de ejecución mucho menor. Obteniendo además el __valor exacto__, por lo que se debe optar por este método si es un problema crítico que requiere de alta precisión.
