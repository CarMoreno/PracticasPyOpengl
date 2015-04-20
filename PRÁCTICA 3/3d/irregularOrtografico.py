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
# 3 Genere una Figura en 3D irregular, queda a su imaginacion como generarla, 
#debe usar al menos 4 colores diferentes para sus caras.
"""En este archivo haremos el punto 1 y 2 (Paralela Ortografica con sus correspondientes LookAt) para la figura irregular 3d""""


def init(): 
  glClearColor(0.529, 0.529, 0.529, 0.0) #Fondo de la ventana
  #glColor3f(0.8, 0.1, 0.3) #ESTABLECEMOS el color por default
  glViewport(0, 0, 500, 500)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  #glOrtho(-1, 1, -1, 1, 1, -2) # Proyeccion paralela 1
  glOrtho(-0.7, 0.2, -0.6, 0.2, -0.2, 0.9) # Proyeccion paralela 2
  #glOrtho(-0.3, 0.8, -0.4, 0.4, -0.3, 0.9) # Proyeccion paralela 3
  imprimirMatrizProyeccion()

def imprimirMatrizProyeccion():
  m = glGetFloatv(GL_PROJECTION_MATRIX)
  print "La matriz de proyeccion es:\n\n%s" % str(m) + "\n"


def imprimirMatrizModelado():
  mm = glGetFloatv(GL_MODELVIEW_MATRIX)
  print "La matriz de modelado es:\n\n%s" % str(mm) + "\n"

def dibujarIrregular():
  glClear (GL_COLOR_BUFFER_BIT) #Borramos buffer de color
  glMatrixMode(GL_MODELVIEW)# Borramos la matriz (cada vez que se dibuje cargamos la matriz identidad)
  glLoadIdentity()
  gluLookAt(0.3, 0.3, 0.3, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)# Establecemos el punto de vista deseado para la figura  gluLookAt( GLdouble eyex, GLdouble eyey, GLdouble eyez,GLdouble centerx, GLdouble centery, GLdouble centerz,GLdouble upx, GLdouble upy, GLdouble upz ) ALTERA LA MATRIZ MODELVIEW
  #gluLookAt(0.3, 0.3, 0.1, 0.2, 0.0, 0.0, 0.0, 1.0, 0.0)#Segunda prueba del lookat
  #gluLookAt(0.1, 0.1, 0.1, 0.2, 0.0, 0.2, 0.0, 1.0, 0.0)#Tercera prueba del lookat
  imprimirMatrizModelado()
  #glRotatef(40, 1,3,6)#Hacemos una transformacion para apreciar mejor la figura
  #Lado frontal del cubo
  glBegin(GL_POLYGON);
  glVertex3f(  0.45, -0.25, -0.25 ) 
  glVertex3f(  0.45,  0.25, -0.25 )     
  glVertex3f( -0.45,  0.25, -0.25 )     
  glVertex3f( -0.45, -0.25, -0.25 )  
  glEnd()

  glColor3f(0.8, 0.1, 0.3)
  glBegin(GL_POLYGON)
  glVertex3f(0.23, -0.25, 0.25)
  glVertex3f(0.3,  0.5, 0.25)
  glVertex3f(-0.1,  0.5, 0.25)
  glVertex3f(-0.30, -0.25, 0.25)
  glEnd()
 
  glColor3f(0.2, 0.1, 0.3)
  glBegin(GL_POLYGON)
  glVertex3f( 0.25, -0.43, -0.25 )
  glVertex3f( 0.25,  0.43, -0.25 )
  glVertex3f( 0.25,  0.43,  0.25 )
  glVertex3f( 0.25, -0.43,  0.25 )
  glEnd()
 

  glBegin(GL_POLYGON)
  glVertex3f( -0.25, -0.25,  0.21 )
  glVertex3f( -0.25,  0.25,  0.21 )
  glVertex3f( -0.25,  0.25, -0.25 )
  glVertex3f( -0.25, -0.25, -0.25 )
  glEnd()
 
  glColor3f(1.0, 0.4, 0.3)
  glBegin(GL_POLYGON)
  glVertex3f(  0.34,  0.25,  0.25 )
  glVertex3f(  0.34,  0.25, -0.25 )
  glVertex3f( -0.34,  0.25, -0.25 )
  glVertex3f( -0.34,  0.25,  0.25 )
  glEnd()

  glColor3f(0.2, 0.7, 0.3)
  glBegin(GL_POLYGON)
  glVertex3f(  0.12, -0.25, -0.25 )
  glVertex3f(  0.12, -0.25,  0.25 )
  glVertex3f( -0.12, -0.25,  0.25 )
  glVertex3f( -0.25, -0.25, -0.25 )
  glEnd()
   
  glFlush()


  

def main():
  glutInit(sys.argv) #Importante, siempre debe ir
  glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH) #Activar el color, el buffer simple y el bufer de profundidad
  glEnable(GL_DEPTH_TEST)
  glutInitWindowSize (500, 500) # Establecemos ventana de 500x500
  glutInitWindowPosition (100, 100)#la ponemos en posicion (100,100) empezando desde la esquina suerior izquierda del pc
  glutCreateWindow ("Irregular")#Creamos en si la ventana y le damos un nombre
  init ()#Llamamos la funcion init
  glutDisplayFunc(dibujarIrregular)
  glutMainLoop()

if __name__ == '__main__':
    main()