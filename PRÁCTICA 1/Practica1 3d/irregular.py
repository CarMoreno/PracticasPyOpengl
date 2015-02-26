from OpenGL.GL import *
from OpenGL.GLUT import *
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
#Programa que genera Genere una esfera con radio r = 0;5 de color azul.

def initGL(width, height):
	glClearColor(0.529, 0.529, 0.529, 0.0) #Fondo de la ventana
	glMatrixMode(GL_PROJECTION) #DEFINIMOS matriz de proyeccion
	glColor3f(0.2, 0.5, 0.5) #ESTABLECEMOS el color por default
def dibujarIrregular():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #Booramos buffer de color y profundidad
	
	glLoadIdentity ()# Borramos la matriz (cada vez que se dibuje cargamos la matriz identidad)

          # -----Transformaciones de vista, aca vamos a empezar a darle un poco de estilo a nuestra escena----

	gluLookAt(0.5,0.2,0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)# Establecemos el punto de vista deseado para la figura  gluLookAt( GLdouble eyex, GLdouble eyey, GLdouble eyez,GLdouble centerx, GLdouble centery, GLdouble centerz,GLdouble upx, GLdouble upy, GLdouble upz );
	glScalef (0.5, 0.5, 0.5) #glScalef(anchoIzquierda, Alto, AnchoDerecha), me define el aspecto de la figura irregular
	glutWireIcosahedron() #Me genera una figura irregular de "Alambre"
	glFlush()
	
def keyPressed(*args):
	key = args[0]
	if key == "r" or key =="R":
		glColor3f(0.5, 0.0, 0.0)
	elif key == "g" or key == "G":
		glColor3f(0.0, 0.5, 0.0)
	elif key ==	"b" or key == "B":
		glColor3f(0.0, 0.0, 0.5)	

def mouseEvent(botonMouse, estadoMouse, x, y):
	if botonMouse == GLUT_LEFT_BUTTON and estadoMouse == GLUT_DOWN: #Si se clickeo con el boton izquierdo del mouse Y ESTE ESTA PRESIONADO
		glColor3f(random(), random(), random())	

#Funcion que me imprime la matriz actual
def imprimirMatriz():
	matriz = glGetFloatv(GL_PROJECTION_MATRIX)
	print matriz

def main():
	global window #Variable global para la ventana
	glutInit(sys.argv) #Importante, siempre debe ir
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH) #Mostramos buffr simple, de color y profundidad
	glutInitWindowSize(500,500) #Establecemos tamano de ventana
	glutInitWindowPosition(200,200) #ESTABLECEMOS posicion de la ventana con respecto a la pantala del pc
	glEnable(GL_DEPTH_BUFFER) 
	#creando la ventana
	window = glutCreateWindow("Taller uno") #Creamos ventana y le damos un nombre
	glutKeyboardFunc(keyPressed) #Evento tecla
	glutMouseFunc(mouseEvent) #Evento raton
	glutDisplayFunc(dibujarIrregular)
	glutIdleFunc(dibujarIrregular)
	imprimirMatriz()
	initGL(500,500) #Llamamos a Init
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #Borramos el bufer de profuncididad e inicial
	glutMainLoop() #Ciclo para que la ventana no desaparezca
	
if __name__ == "__main__":
	main()
