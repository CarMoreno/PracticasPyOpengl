import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

# ====================================================================
#Para el color de fondo de ventana realize una regla de 3 simple:  
#Si 255 ---> 1 entonces
#   135 ---> x
# x = 135/255
# x = 0.2529 (aproximadamente)
# ====================================================================
# 								DATOS
# Nombres : Viviana Andrea Zuluaga    1255
#			Carlos Andres Moreno      1255896				
# Plan: Ingenieria de Sistemas
# Profesor: Carlos Andres Delgado
# Taller Numero 3 de Computacion Grafica
#=====================================================================						
# 3. Vistas en 3D
# 3.1 Figuras a generar
#2 Genere una piramide de tamano, forma y color libre. Preferiblemente
# un color diferente en cada cara.
"""En este archivo haremos el punto 3 y 4 (Paralela Perspectiva con sus correspondientes LookAt) para la Piramide 3d""""

def init(): 
  glClearColor(0.529, 0.529, 0.529, 0.0) #Fondo de la ventana
  glColor3f(0.6, 0.1, 0.4) #ESTABLECEMOS el color por default
  glViewport(0, 0, 500, 500) # Matriz de mapeo - se ajusta la vista a las dimensiones de la ventana
  glMatrixMode(GL_PROJECTION) # Matriz de proyecccion
  glLoadIdentity()
  glFrustum(-0.2, 0.7, -0.7, 0.6, 0.3, 0.8) # Proyeccion paralela 1
  #glFrustum(-0.6, 0.7, -0.7, 0.1, 0.1, 1) # Proyeccion paralela 2
  #glFrustum(-0.3, 0.3, -2, 0.1, 0.2, 0.8) # Proyeccion paralela 3
  imprimirMatrizProyecccion()

def imprimirMatrizProyecccion():
  m = glGetFloatv(GL_PROJECTION_MATRIX)
  print "La matriz de proyeccion es:\n\n%s" % str(m) + "\n"


def imprimirMatrizModelado():
  mm = glGetFloatv(GL_MODELVIEW_MATRIX)
  print "La matriz de modelado es:\n\n%s" % str(mm) + "\n"

def dibujarPiramide():
  glClear(GL_COLOR_BUFFER_BIT) #Borramos buffer de color y de profundidad
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity ()# Borramos la matriz (cada vez que se dibuje cargamos la matriz identidad)
  
  # Establecemos el punto de vista deseado para la figura  gluLookAt( GLdouble eyex, GLdouble eyey, GLdouble eyez,GLdouble centerx, GLdouble centery, GLdouble centerz,GLdouble upx, GLdouble upy, GLdouble upz )
  gluLookAt(0.6, 0.1, 0.6, 0.2, 0.1, 0.1, 0, 0.1, 0) # Posicion de la camara, altera a la matriz MODELVIEW
  #gluLookAt(0.0, 0.2, 0.5, 0.2, 0.1, 0.1, 0, 0.1, 0) #Segunda prueba del lookat
  #gluLookAt(-0.4, 0.2, 0.5, 0.3, 0.1, 0.1, 0, 0.1, 0) #Tercera prueba del lookat
  #glRotatef(90, 1,0,1)
  imprimirMatrizModelado()        
  glutWireCone (0.4,0.4, 3, 4)#Me define una piramide de "Alabre"
  glFlush()

 
def main():
  glutInit(sys.argv) #Importante, siempre debe ir
  glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH) #Activar el color, el buffer simple y el bufer de profundidad
  glEnable(GL_DEPTH_TEST)
  glutInitWindowSize (500, 500) # Establecemos ventana de 500x500
  glutInitWindowPosition (100, 100)#la ponemos en posicion (100,100) empezando desde la esquina suerior izquierda del pc
  glutCreateWindow ("Taller Uno")#Creamos en si la ventana y le damos un nombre
  init ()#Llamamos la funcion init
  glutDisplayFunc(dibujarPiramide)
  glutMainLoop()

if __name__ == '__main__':
    main()