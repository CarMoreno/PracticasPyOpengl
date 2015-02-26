from OpenGL.GL import *
from OpenGL.GLUT import *
from random import random

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
#Programa que genera un cuadrado de L = 0.5, centrado en el origen
#Como el cuadro esta centrado en el origen, entonces del origen a la izquierda habra 0.25 y 
#del origen a la derecha habra tambien 0.25, para que la suma nos de 0.5

def initGL(width, height):
	glClearColor(0.529, 0.529, 0.529, 0.0)
	glMatrixMode(GL_PROJECTION)
	glColor3f(0,0,0)

def dibujarCuadrado():
	glClear(GL_COLOR_BUFFER_BIT)
	
	glBegin(GL_QUADS)
	glVertex2f(-0.25, 0.25)
	glVertex2f(0.25, 0.25)
	glVertex2f(0.25, -0.25)
	glVertex2f(-0.25, -0.25)
	glEnd()
	glFlush()
	#glutSwapBuffers();	
	
def keyPressed(*args):
	key = args[0]
	if key == "r" or key =="R":
		glColor3f(1.0, 0.0, 0.0)
	elif key == "g" or key == "G":
		glColor3f(0.0, 1.0, 0.0)
	elif key ==	"b" or key == "B":
		glColor3f(0.0, 0.0, 1.0)	

#Funcion que me imprime la matriz actual
def imprimirMatriz():
	matriz = glGetFloatv(GL_PROJECTION_MATRIX)
	print matriz

def mouseEvent(botonMouse, estadoMouse, x, y):
	if botonMouse == GLUT_LEFT_BUTTON and estadoMouse == GLUT_DOWN: #Si se clickeo con el boton izquierdo del mouse Y ESTE ESTA PRESIONADO
		glColor3f(random(), random(), random())		

def main():
	global window
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	
	#creando la ventana
	window = glutCreateWindow("Taller uno")
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseEvent)
	glutDisplayFunc(dibujarCuadrado)
	glutIdleFunc(dibujarCuadrado)
	imprimirMatriz()
	initGL(500,500)
	glutMainLoop()
	
if __name__ == "__main__":
	main()
