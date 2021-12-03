# Roomba: Diana
Para este proyecto hay dos agentes: El robot que limpia el piso y el piso que solamente cambia de estado de sucio a limpio si el robot se encima.
El objetivo del robot es limpiar el suelo en la menor cantidad de pasos posibles.

En este programa el Roomba se mueve de forma random y si encuentra una celda de suelo sucia se mueve hacia ella para limpiarla.

¿Cómo optimizaría el proceso de limpiado?

El robot puede hacer un diccionario checando sus possible_steps guarda como llave la posición y como valor el estado del suelo. Entonces prioriza moverse a las posiciones que estén sucias.
