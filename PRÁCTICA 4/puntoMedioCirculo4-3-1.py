"""Nombres: Carlos Andres Moreno
            Daniela Roldan Quiroga
            Viviana Andrea Zuluaga
    Plan: 3743
    Asignatura: Computacion Grafica
    Practica 4
    **********************************************************************************************************************

    4.3 Usando la implementacion que realizo en el punto 4.2, dibuje con la ayuda de la 
        libreria de OpenGL las siguientes circulos: Circulo centrado en (0.2, -0,4) con r = 0.3."""


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def inicio():
    glClearColor(0.53, 0.53, 0.53, 0.0)  # Color de fondo 
    glMatrixMode(GL_PROJECTION)  # Activamos la matriz de proyeccion
    glLoadIdentity()


def dibujaPuntosCentroArbitrario1():
    '''Dibuja con ayuda de la libreria OpenGL los circulos con centro arbitrario'''
    glClear(GL_COLOR_BUFFER_BIT)  # "Limpiamos" el frame buffer con el color de "glClearColor"
    glPointSize(4.0)
    puntosADibujar = puntoMedioCirculo(0.3) # Circulo con r = 0.3. Para este radio no se logra obtener un circulo
                                            # bien definido, con un r mayor se puede apreciar mejor la figura
    glTranslatef(0.2, -0.4, 0.0) # Se mueve el sistema de coordenadas
    glBegin(GL_POINTS) # Dibuja los puntos obtenidos con el algoritmo
    for i in range(0, len(puntosADibujar)-1, 2): 
        glColor3f(0.0, 0.0, 0.0)  # Se especifica el color
        x = puntosADibujar[i]*0.1 # Se reduce el tamanio del componente para que quepa en la grilla
        y = puntosADibujar[i+1]*0.1 # Se reduce el tamanio del componente para que quepa en la grilla
        glVertex2f(x, y) # Se dibuja el punto y su reflexion sobre los ejes
        glVertex2f(y, x)
        glVertex2f(y, -x)
        glVertex2f(x, -y)
        glVertex2f(-x, -y)
        glVertex2f(-y, -x)
        glVertex2f(-y, x)
        glVertex2f(-x, y)
    glEnd()    
    glFlush()  # Asegura que los comandos anteriores se van a ejecutar


def puntoMedioCirculo(r):
    '''Implementacion algoritmo punto medio para circulos centrados en el origen'''
    x = 0
    y = r
    d = 1 - r
    puntosCirculo= [x, y] 
    while (y > x):
        if d < 0:
            d = d + 2*x + 3
            x = x + 1
            puntosCirculo.append(x)
            puntosCirculo.append(y)
        else:
            d = d + 2*(x - y) + 5
            x = x + 1
            y = y - 1
            puntosCirculo.append(x)
            puntosCirculo.append(y)
    return puntosCirculo


def imprimePuntos(r):
    '''Imprime los puntos a pintar por la consola'''
    misPuntos = puntoMedioCirculo(r)
    print "\n Los puntos a pintar en un octante para r = ", r,  " son: "
    for x in range(0, len(misPuntos)-1, 2):
        print "(", misPuntos[x], ",", misPuntos[x+1], ")"


def main():
    glutInit(sys.argv)  # Primera llamada siempre en OpenGL
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Activamos el buffer simple y colores del tipo RGB
    glutInitWindowSize(500, 500)  # Se define una ventana de medidas ancho x alto
    glutInitWindowPosition(200, 200)  # Posicionamos la esquina superior izquierda de la ventana en el punto definido
    glutCreateWindow("Practica 4: Raster")  # Creamos la ventana y le adjudicamos un nombre
    glutDisplayFunc(dibujaPuntosCentroArbitrario1)
    inicio()
    imprimePuntos(0.3) # Muestra los puntos que se pintan en un octante cuando r=0.3
    glutMainLoop()


if __name__ == '__main__':
        main()