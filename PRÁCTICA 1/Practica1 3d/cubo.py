import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from random import random #Necesaria para generar numeros pseudoaleatorios

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
# Taller Numero 1 de Computacion Grafica
#=====================================================================						
#1.								
#Programa que genera un cubo con l = 0;5 de color cyan.

def init(): 
   glClearColor(0.529, 0.529, 0.529, 0.0)#Definimos color de ventana
   glColor3f(0.0, 1.0, 1.0)#Definimos color inicial para el cubo

def dibujarCubo():
   glClear (GL_COLOR_BUFFER_BIT) #Borramos buffer de color
   glLoadIdentity ()             # Borramos la matriz (cada vez que se dibuje cargamos la matriz identidad)
   
   # -----Transformaciones de vista, aca vamos a empezar a darle un poco de estilo a nuestra escena----

   gluLookAt(3.0, 3.0, 6.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)# Establecemos el punto de vista deseado para la figura  gluLookAt( GLdouble eyex, GLdouble eyey, GLdouble eyez,GLdouble centerx, GLdouble centery, GLdouble centerz,GLdouble upx, GLdouble upy, GLdouble upz );
   glScalef(2.0, 2.0, 2.0)#glScalef(anchoIzquierda, Alto, AnchoDerecha), me define el aspecto del cubo
   glutSolidCube(0.5)#Me genera un cubo de lado 0.5 solido
   glFlush()

def reshape (w, h): #Esta funcion se escarga de reescalar la ventana
   glViewport (0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity ()
   glFrustum (-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
   glMatrixMode (GL_MODELVIEW)

def keyPressed(*args):
  key = args[0]
  if key == "r" or key =="R":
    glColor3f(0.5, 0.0, 0.0)
  elif key == "g" or key == "G":
    glColor3f(0.0, 0.5, 0.0)
  elif key == "b" or key == "B":
    glColor3f(0.0, 0.0, 0.5)  

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
  glutReshapeFunc(reshape)
  imprimirMatriz()
  glutMainLoop()

if __name__ == '__main__':
    main()  