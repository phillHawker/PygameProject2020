import pygame #Importamos el módulo pygame para el proyecto.


def main(): #Declaramos la funcion principal del programa.
    pygame.init() #Inicializamos todos los módulos de pygame. (opcional: se pueden inicializar individualmente)
    pantalla = pygame.display.set_mode([1280,480]) #Fijamos el tamaño de la ventana del programa.
    pygame.display.set_caption("MainProject") #Le damos un nombre a la ventana.
    salir = False #Creamos una variable booleana para tener control del Bucle PRINCIPAL.
    reloj1 = pygame.time.Clock() #reloj para regular la actualización de pantalla.
    blanco = (255,255,255) #Tupla con los datos RGB del color blanco.

    while salir!= True: #(Bucle PRINCIPAL) para evitar que la ventana se cierre.
        for event in pygame.event.get(): #Recorre todos los eventos que se produzcan (periféricos en acción).
            if event.type == pygame.QUIT: #Preguntamos si ocurrió el evento "cerrar ventana".
                salir = True
        reloj1.tick(20) #establecemos el refresco de pantalla a 20FPS.
        pantalla.fill(blanco) #Cambiamos de color el fondo, a blanco.
        pygame.display.update() # SIN parámetros Actualiza TODA la pantalla en cada ciclo del WHILE. #OPCIONAL: Se puede usar pygame.display.flip() tambien, para hacer lo mismo.


    pygame.quit() #cuando el programa llega a ésta linea, se cierra la ventana, porque salió del Bucle PRINCIPAL.

main() #invocamos a la funcion principal para que se ejecute.
