import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from random import random #Necesaria para generar numeros pseudoaleatorios
from math import sin
from math import cos
from math import pi

# ====================================================================
#Para el color de fondo de ventana realize una regla de 3 simple:  
#Si 255 ---> 1 entonces
#   135 ---> x
# x = 135/255
# x = 0.529 (aproximadamente)
# ====================================================================
# 								DATOS
# Nombre : Carlos Andres Moreno
# Codigo : 1255896
# Plan: Ingenieria de Sistemas
# Profesor: Carlos Andres Delgado
# Taller Numero 2 de Computacion Grafica
#=====================================================================														
#Programa que genera un cubo con l = 0;5 de color cyan.

def init(): 
  glMatrixMode (GL_PROJECTION)
  glClearColor(0.529, 0.529, 0.529, 0.0)#Definimos color de ventana
  glColor3f(0.0, 1.0, 1.0)#Definimos color inicial para el cubo

def dibujarCubo():
  glClear (GL_COLOR_BUFFER_BIT)
  glutSolidCube(0.5)
  glFlush ()

def gradosAradianes(grados):
  return (grados*pi)/180

# operaciones sobre la figura
def keyPressed(*args):
  key = args[0]
  if key == "r" or key =="R":
    #Primero defino mi matriz de rotacion, puesto que esta sera la que se multiplacara con la matriz
    #de proyeccion inicial (la identidad), ahora bien, la matriz definida anteriormente, rotara la
    #figura alrededor del eje x.
    glLoadIdentity()
    matrizRotacion = [1, 0, 0, 0, 0, cos(gradosAradianes(30)), sin(gradosAradianes(30)), 0, 0, -sin(gradosAradianes(30)), cos(gradosAradianes(30)), 0, 0, 0, 0, 1]
    glMultMatrixf(matrizRotacion)#Esta funcion multiplica la matriz de rotacion por la identidad
  
  elif key == "s" or key == "s":
    glLoadIdentity()
    #El cubo rotara 35 grados con respecto a el vector (1,3,5)
    glRotatef(gradosAradianes(35), 1, 3, 5)

  elif key == "b" or key == "B":
    # Cada vez que se presiona b se aplica una transformacion
    # compuesta de rotar 30 grados con respecto a z, trasladar
    # 0.1 con respecto a y y escalar con respecto a y en 0.95. En
    # este punto no es necesario insertar una matriz y realizar
    # el proceso.
    glLoadIdentity()
    glRotatef(gradosAradianes(30), 0, 0, 1)
    glTranslatef(0.0, 0.1, 0.0)
    glScale(0.5, 0.95, 0.3)


def mouseEvent(botonMouse, estadoMouse, x, y):
    if botonMouse == GLUT_LEFT_BUTTON and estadoMouse == GLUT_DOWN: #Si se clickeo con el boton izquierdo del mouse Y ESTE ESTA PRESIONADO
        glColor3f(random(), random(), random())  

#Funcion que me imprime la matriz actual
def imprimirMatriz():
  matriz = glGetFloatv(GL_PROJECTION_MATRIX)
  print matriz

def main():
  glutInit(sys.argv) #Importante, siempre debe ir
  glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB) #Activar el color y el buffer simple
  glutInitWindowSize (500, 500) # Establecemos ventana de 500x500
  glutInitWindowPosition (100, 100)#la ponemos en posicion (100,100) empezando desde la esquina suerior izquierda del pc
  glutCreateWindow ("Taller Uno")#Creamos en si la ventana y le damos un nombre
  init ()#Llamamos la funcion init
  glutDisplayFunc(dibujarCubo)
  glutIdleFunc(dibujarCubo)
  glutKeyboardFunc(keyPressed)#Evento de tecla
  glutMouseFunc(mouseEvent)#Evento de raton
  imprimirMatriz()
  glutMainLoop()

if __name__ == '__main__':
    main()  