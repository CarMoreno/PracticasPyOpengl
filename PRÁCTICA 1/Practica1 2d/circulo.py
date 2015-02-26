from OpenGL.GL import *
from OpenGL.GLUT import *
from random import random
from math import sin
from math import cos
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
#3.								
#Programa que Genera un circulo con radio r = 0,5 de color negro. EL circulo que voy a generar estara centrado
#en el origen, por lo que del origen hacia la izquierda tendra una distancia de 0.25 y hacia la derecha 
#tambien.


def initGL(width, height):
	glClearColor(0.529, 0.529, 0.529, 0.0)
	glMatrixMode(GL_PROJECTION)
	glColor3f(0.0, 0.0, 0.0)
	
def dibujarCirculo():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POLYGON)
	for i in range(400):
		x = 0.25*sin(i) #Cordenadas polares x = r*sin(t) donde r = radio/2 (Circunferencia centrada en el origen)
		y = 0.25*cos(i) #Cordenadas polares y = r*cos(t)
		glVertex2f(x, y)			
	glEnd()
	glFlush()

def keyPressed(*args):
	key = args[0]
	if key == "r" or key =="R":
	#	glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(1.0, 0.0, 0.0)
	elif key == "g" or key == "G":
		glColor3f(0.0, 1.0, 0.0)
	elif key ==	"b" or key == "B":
		glColor3f(0.0, 0.0, 1.0)			

def mouseEvent(botonMouse, estadoMouse, x, y):
	if botonMouse == GLUT_LEFT_BUTTON and estadoMouse == GLUT_DOWN: #Si se clickeo con el boton izquierdo del mouse Y ESTE ESTA PRESIONADO
		glColor3f(random(), random(), random())		

#Funcion que me imprime la matriz actual
def imprimirMatriz():
	matriz = glGetFloatv(GL_PROJECTION_MATRIX)
	print matriz

def main():
	global window
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	
	#creando la ventana
	window = glutCreateWindow("Taller uno")
	
	glutDisplayFunc(dibujarCirculo)
	glutIdleFunc(dibujarCirculo)
	imprimirMatriz()
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseEvent)
	initGL(500,500)
	glutMainLoop()
	
if __name__ == "__main__":
	main()
