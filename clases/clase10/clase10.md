# Clase 10: 23 de octubre de 2023

En esta clase comenzamos repasando y dando indicaciones de como afrontar los ejercicios de dibujar figuras de asteriscos. Resolvimos los ejercicios 2 y 3 de la relación 5.

A continuación comenzamos con el Tema 4, donde se introdujo la necesidad de dividir el código en pequeños trozos para facilitar su escritura y su reutilización. También vimos cómo se hacen y se usan funciones en python. Como ejemplo para ilustrar todo esto vimos el cálculo de un número combinatorio

# Figura: cuadrado
Dibujar un cuadrado hueco de doble pared como el siguiente, pidiendo antes el lado:
```Lado: 6```
```******```
```******```
```**  **```
```**  **```
```******```
```******```

[[Ver código](t3e43.figuracuadrado.py)]

# Figura: rombo
Dibujar un rombo como el siguiente, pidiendo antes la semialtura:
```Semialtura: 4```
```   *```
```  ***```
``` *****```
```*******```
``` *****```
```  ***```
```   *```

[[Ver código](t3e44.figurrombo.py)]


## Ejemplo: Números combinatorios

La idea es hacer el cálculo de un número combinatorio que es la división entre m! y n!\*(m-n)! Como se observa se necesitan calcular 3 veces el factorial de diferentes valores y entonces crear una trozo de código que lo calcule y lo podamos reutilizar facilita mucho realizar el programa.

[[Ver código sin funciones](t4e01.combinatorio1.py)]

[[Ver código con funciones](t4e02.combinatorio2.py)]


## Cilindro 

*Realice dos funciones, una que calcule el área a partir del radio del círculo y otra que calcule su longitud.*

*Realice una función que calcule el área de un rectángulo.*

*Realice otra función que calcule el área del cilindro a partir de su radio y su altura. El área de un cilindro es la suma de sus componentes, es decir, es 2 veces área de la base (círculo) más el área del rectángulo.*

*Realice el programa principal que lea el radio y la altura del cilindro y nos muestre su área.*

[[Solución](t4e03.cilindro.py)]