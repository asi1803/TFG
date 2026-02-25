#parentesis opcionales en los tuples
# los tuples son inmutables, lo que significa que no se pueden modificar después de su creación. Esto los hace útiles para almacenar datos que no deben cambiar, como coordenadas, fechas o cualquier tipo de información que deba permanecer constante.
# los tuples pueden contener elementos de diferentes tipos de datos, como números, cadenas, listas e incluso otros tuples. Esto los hace versátiles para almacenar una variedad de información.a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))
# a tiene 10 elementos, pero b tiene solo 4 elementos únicos, por lo que la diferencia es 6.

#After executing this code, will the number 5 be a part of the set b?
b = set(a)
b.add(5)
b.pop()
#Puede que no, ya que el método pop() elimina un elemento aleatorio del conjunto. Si el número 5 es el elemento que se elimina, entonces no formará parte del conjunto b después de la ejecución del código. Sin embargo, si se elimina otro elemento, entonces el número 5 seguirá siendo parte del conjunto b.

#a un set añades con el método add(), y puedes eliminar un elemento con el método pop(). El método pop() elimina un elemento aleatorio del conjunto, por lo que no se puede predecir qué elemento se eliminará. Si deseas eliminar un elemento específico, puedes usar el método remove() en su lugar.
#¡OJO! a un list puedes añadir con el método append(), pero no puedes eliminar un elemento aleatorio con pop() sin especificar un índice, ya que pop() en una lista elimina el último elemento por defecto. Si deseas eliminar un elemento específico de una lista, puedes usar el método remove() o pop() con un índice específico.