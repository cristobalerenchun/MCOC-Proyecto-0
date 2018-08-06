# Proyecto-0---Perdida-de-Significancia-CE
# MCOC-Proyecto-0


Introducción
==============

En este proyecto se busca demostrar como ocurre elefecto de perdida de significancia y el por quw este sucede. 


Ejemplo
==============


Aquí a modo de ejemplo ocupamos la funcion f(x)=(1-cos x)/x**2 y la graficamos entre (-4*10**-8,4*10**-8), de esta manera vemos el error que se produce en el grafico   



Resultados
==============

Se define el error relativo como 



Abajo se muestra como va creciendo el error relativo en la medida en que se consideran cada vez mas números. Esto ocurre debido a la perdida de significancia en la operacion suma usada internamente por el algoritmo de `sp.mean`. 

![Results](loss-of-significance.png)


