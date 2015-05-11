"""Nombres: Carlos Andres Moreno
            Daniela Roldan Quiroga
            Viviana Andrea Zuluaga
    Plan: 3743
    Asignatura: Computacion Grafica
    Practica 4
    *************************************************************************************

    4.1 Realice una implementacion que permita aplicar el algoritmo de punto medio para 
    trazar la linea entre dos puntos arbitrarios."""


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def inicio():
    glClearColor(0.53, 0.53, 0.53, 0.0)  # Color de fondo 
    glMatrixMode(GL_PROJECTION)  # Activamos la matriz de proyeccion


def dibujaPuntos():
    '''Dibuja con ayuda de la libreria OpenGL las rectas'''
    glClear(GL_COLOR_BUFFER_BIT)  # "Limpiamos" el frame buffer con el color de "glClearColor"
    glPointSize(4.0)
    puntoADibujar = puntoMedioLinea(-0.8, -0.71, 0.9, 0.48) # Linea y=0.7x - 0.15 desde x=-0.8 a x=0.9 
    glBegin(GL_POINTS) # Dibuja los puntos obtenidos con el algoritmo
    for i in range(0, len(puntoADibujar)-1, 2): 
        glColor3f(0.0, 0.0, 0.0)  # Se especifica el color
        x = puntoADibujar[i]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla
        y = puntoADibujar[i+1]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
        glVertex2f(x, y)      
    glEnd() 

    glBegin(GL_LINES) # Dibuja las lineas entre los puntos
    for i in range(0, len(puntoADibujar)-1, 2): 
        glColor3f(0.0, 0.0, 0.0)  # Se especifica el color
        x = puntoADibujar[i]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
        y = puntoADibujar[i+1]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
        glVertex2f(x, y)      
    glEnd() 

    glPointSize(4.0)
    puntoADibujar = puntoMedioLinea(-0.6, -0.75, 0.8, 0.69) # Linea desde (-0.6, -0.75) hasta (0.8, 0.69)
    glBegin(GL_POINTS) # Dibuja los puntos obtenidos con el algoritmo
    for i in range(0, len(puntoADibujar)-1, 2): 
        glColor3f(1.0, 0.0, 0.0)  # Se especifica el color
        x = puntoADibujar[i]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
        y = puntoADibujar[i+1]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
        glVertex2f(x, y)      
    glEnd()

    glBegin(GL_LINE_STRIP) # Dibuja las lineas entre los puntos
    for i in range(0, len(puntoADibujar)-1, 2): 
        glColor3f(1.0, 0.0, 0.0)  # Se especifica el color
        x = puntoADibujar[i]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
        y = puntoADibujar[i+1]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
        glVertex2f(x, y)      
    glEnd()
    glFlush()  # Asegura que los comandos anteriores se van a ejecutar


def puntoMedioLinea(x0, y0, x1, y1):
    '''Implementacion algoritmo punto medio para lineas'''
    dy = y1 - y0
    dx = x1 - x0
    d = (2*dy) - dx
    incrE = 2*dy
    incrNE = 2*(dy - dx)
    x = x0
    y = y0
    dibujaPunto= [x, y]
    while (x < x1):
        if d <= 0:
            d = d + incrE
            x = x + 1
            dibujaPunto.append(x)
            dibujaPunto.append(y)
        else:
            d = d + incrNE
            x = x + 1
            y = y + 1
            dibujaPunto.append(x)
            dibujaPunto.append(y)
    return dibujaPunto


def imprimePuntos(x0, y0, x1, y1):
    '''Imprime los puntos a pintar por la consola'''
    misPuntos = puntoMedioLinea(x0, y0, x1, y1)
    print "\n Los puntos a pintar para ", "(" ,x0, y0, ")",  "(" ,x1, y1, ") son: "
    for x in range(0, len(misPuntos)-1, 2):
        print "(", misPuntos[x], ",", misPuntos[x+1], ")"


def main():
    glutInit(sys.argv)  # Primera llamada siempre en OpenGL
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Activamos el buffer simple y colores del tipo RGB
    glutInitWindowSize(500, 500)  # Se define una ventana de medidas ancho x alto
    glutInitWindowPosition(200, 200)  # Posicionamos la esquina superior izquierda de la ventana en el punto definido
    glutCreateWindow("Practica 4: Raster")  # Creamos la ventana y le adjudicamos un nombre
    glutDisplayFunc(dibujaPuntos)
    glutIdleFunc(dibujaPuntos)
    inicio()
    imprimePuntos(-4, -6, 9, 6) # Muestra los puntos a pintar por consola desde (-4, -6) hasta (9, 6)
    imprimePuntos(-9, 2, 8, 6) # Muestra los puntos a pintar por consola desde (-9, 2) hasta (8, 6)
    #imprimePuntos(-0.8, -0.71, 0.9, 0.48)
    #imprimePuntos(-0.6, -0.75, 0.8, 0.69)
    glutMainLoop()


if __name__ == '__main__':
        main()