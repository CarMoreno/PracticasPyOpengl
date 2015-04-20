import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

# ====================================================================
#Para el color de fondo de ventana realize una regla de 3 simple:  
#Si 255 ---> 1 entonces
#   135 ---> x
# x = 135/255
# x = 0.529 (aproximadamente)
# ====================================================================
# 								DATOS
# Nombres : Viviana Andrea Zuluaga    1255455
#			Carlos Andres Moreno      1255896				
# Plan: Ingenieria de Sistemas
# Profesor: Carlos Andres Delgado
# Taller Numero 3 de Computacion Grafica
#=====================================================================						
# 3. Vistas en 3D
# 3.1. Figuras a generar
# 1. Genere un cubo de color con colores diferentes en cada
# uno de sus lados y lado L = 05 centrado en el origen.
# 3.2.1 Aplique una proyeccion paralela con el comando glOrtho
# 3.2.2 Para el caso anterior aplique con glLookAt el movimiento
# de la camara.
"""En este archivo haremos el punto 1 y 2 (Paralela Ortografica con sus correspondientes LookAt) para El cubo 3d""""

def init(): 
  glClearColor(0.529, 0.529, 0.529, 0.0) #Fondo de la ventana
  glColor3f(0.2, 0.5, 0.5) #ESTABLECEMOS el color por default
  glViewport(0, 0, 500, 500) # Matriz de mapeo - se ajusta la vista a las dimensiones de la ventana
  glMatrixMode(GL_PROJECTION) # Matriz de proyecccion
  glLoadIdentity()
  glOrtho(-1, 1, -1, 1, 1, -2) # Proyeccion paralela 1
  #glOrtho(-1, 1, -0.5, 1, 1, -1) # Proyeccion paralela 2
  #glOrtho(-0.5, 0.4, -0.5, 1, -0.5, 0.9) # Proyeccion paralela 3
  imprimirMatrizProyecccion()


def imprimirMatrizProyecccion():
  m = glGetFloatv(GL_PROJECTION_MATRIX)
  print "La matriz de proyeccion es:\n\n%s" % str(m) + "\n"


def imprimirMatrizModelado():
  mm = glGetFloatv(GL_MODELVIEW_MATRIX)
  print "La matriz de modelado es:\n\n%s" % str(mm) + "\n"


def dibujarCubo():
  glClear (GL_COLOR_BUFFER_BIT) #Borramos buffer de color
  glMatrixMode (GL_MODELVIEW) # Matriz de modelado
  glLoadIdentity()
  #gluLookAt(0.1, 0.1, 0.5, 0.2, 0.1, 0.1, 0, 0.1, 0) # Posicion de la camara, altera a la matriz MODELVIEW
  gluLookAt(-0.3, 0.2, -0.1, 0.2, 0.4, 0.4, 0.1, 0.1, 0)
  #gluLookAt(0.1, 0.1, 0.5, 0.2, 0.1, 0.1, 0, 0.2, 0)
  #glRotatef(70, 1,3,6)#Hacemos una transformacion para apreciar mejor la figura
  imprimirMatrizModelado()

  #Lado frontal del cubo
  glBegin(GL_POLYGON);
  glVertex3f(  0.25, -0.25, -0.25 ) 
  glVertex3f(  0.25,  0.25, -0.25 )     
  glVertex3f( -0.25,  0.25, -0.25 )     
  glVertex3f( -0.25, -0.25, -0.25 )  
  glEnd()

  #LADO TRASERO: lado blanco
  glBegin(GL_POLYGON)
  glColor3f(1.0,  1.0, 1.0)
  glVertex3f(0.25, -0.25, 0.25)
  glVertex3f(0.25,  0.25, 0.25)
  glVertex3f(-0.25,  0.25, 0.25)
  glVertex3f(-0.25, -0.25, 0.25)
  glEnd()
 
  # LADO DERECHO: lado morado
  glBegin(GL_POLYGON)
  glColor3f(  0.5,  0.0,  0.5 )
  glVertex3f( 0.25, -0.25, -0.25 )
  glVertex3f( 0.25,  0.25, -0.25 )
  glVertex3f( 0.25,  0.25,  0.25 )
  glVertex3f( 0.25, -0.25,  0.25 )
  glEnd()
 
  # LADO IZQUIERDO: lado verde
  glBegin(GL_POLYGON)
  glColor3f(   0.0,  0.5,  0.0 )
  glVertex3f( -0.25, -0.25,  0.25 )
  glVertex3f( -0.25,  0.25,  0.25 )
  glVertex3f( -0.25,  0.25, -0.25 )
  glVertex3f( -0.25, -0.25, -0.25 )
  glEnd()
 
  # LADO SUPERIOR: lado azul
  glBegin(GL_POLYGON)
  glColor3f(   0.0,  0.0,  0.5 )
  glVertex3f(  0.25,  0.25,  0.25 )
  glVertex3f(  0.25,  0.25, -0.25 )
  glVertex3f( -0.25,  0.25, -0.25 )
  glVertex3f( -0.25,  0.25,  0.25 )
  glEnd()
  # LADO INFERIOR: lado rojo
  glBegin(GL_POLYGON)
  glColor3f(   0.5,  0.0,  0.0 )
  glVertex3f(  0.25, -0.25, -0.25 )
  glVertex3f(  0.25, -0.25,  0.25 )
  glVertex3f( -0.25, -0.25,  0.25 )
  glVertex3f( -0.25, -0.25, -0.25 )
  glEnd() 
  glFlush()

 
def main():
  glutInit(sys.argv) #Importante, siempre debe ir
  glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH) #Activar el color, el buffer simple y el bufer de profundidad
  glEnable(GL_DEPTH_TEST)
  glutInitWindowSize (500, 500) # Establecemos ventana de 500x500
  glutInitWindowPosition (100, 100)#la ponemos en posicion (100, 100) empezando desde la esquina superior izquierda del pc
  glutCreateWindow ("Cubo")#Creamos en si la ventana y le damos un nombre
  init ()#Llamamos la funcion init
  glutDisplayFunc(dibujarCubo)
  glutMainLoop()

if __name__ == '__main__':
    main()  