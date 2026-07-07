# Ejercicio 1

### Ejecucion
- revisar que tenga las depdencias instaladas
- ejecutar ne consola el comando: python task_processor.py

### Explicacion

En el Ejercicio 1 Se implemento un isstema de procesamiento de tareas distribuido usando hilos y usando procesos, en este ejercicios de generan 4 tareas con una dificultad aleatoria entre 1 y 5, al mometo de ejecutar este ejercico la salida en consola fue la siguiente:


Tareas generadas:
Tarea 1: dificultad 2
Tarea 2: dificultad 1
Tarea 3: dificultad 5
Tarea 4: dificultad 4

Ejecutando con hilos
Tarea 2 dificultad 1 completada en 0.559s  checksum=185
Tarea 1 dificultad 2 completada en 1.969s  checksum=433
Tarea 4 dificultad 4 completada en 3.983s  checksum=35
Tarea 3 dificultad 5 completada en 4.336s  checksum=258
Tareas completadas hilos: 4

Ejecutando con procesos
Tarea 2 dificultad 1 completada en 0.232s  checksum=185
Tarea 1 dificultad 2 completada en 0.473s  checksum=433
Tarea 4 dificultad 4 completada en 1.007s  checksum=35
Tarea 3 dificultad 5 completada en 1.332s  checksum=258
Tareas completadas procesos: 4

En esta salida podemos determinar que los procesos fueron mas rpidos al momento d ejecutar estas tareas por que si comapramos los tiempos los tiempos de los procesos son mas bajos que los de los hilos, cada uno de estos tiene un uso diferente en el cual es mas eficiente, los procesos son mejores para tareas de calculo intenso y los hilos son mejores para tareas de red, de disco o de espera


# Ejercicio 3

### Ejecucion
- revisar que tenga las depdencias instaladas
- ejecutar ne consola el comando: python load_balance.py

### Explicacion

En el Ejercicio 3 se utilozo dos algoritmos de balanceo de carga uno que es round robin que lo que hace es que distribuye la carga en partes iguales, si tenemos dos servidores manda 1 peticion a una y otra  ala otra y asi continuamente, el otro algoritmo usado es least connection el cual manda las nuevs peticiones a el servidor con menos carga, en la ejecucuon d emi ejercicio este fue el resultado

Simulacion de 50 peticiones concurrentes

Round-robin:
  Servidor-1: 25
  Servidor-2: 25
  Tiempo total: 0.675s

Least connections:
  Servidor-1: 24
  Servidor-2: 26
  Tiempo total: 0.675s

En esta salida lo que se puede interpetear es que round robin es mas eficiente ya que balanceo de manera pareja y que least connection es un poco menos equilibrado y en cuanto a tiempo total para el balanceo ambos estuviron iguales asi que si mayor diferencia es la distribucion de peticiones 


