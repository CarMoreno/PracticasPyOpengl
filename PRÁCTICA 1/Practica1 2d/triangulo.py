from OpenGL.GL import *
from OpenGL.GLUT import *
from random import random
#from random import random


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
#2.								
#Programa que Genera un triangulo de color negro con h = 0,5 y L = 0,5. El triangulo que se va a generar
#es un triangulo rectangulo, su base medira 0.5 y su lado 0.5, la hipotenusa se puede hallar con el teorema
#de Pitagoras.

def initGL(width, height):
	glClearColor(0.529, 0.529, 0.529,  0.0)
	glMatrixMode(GL_PROJECTION)
	glColor3f(0,0,0)

def dibujarTriangulo():
	glClear(GL_COLOR_BUFFER_BIT)
	
	glBegin(GL_TRIANGLES)
	glVertex2f(0.0, 0.0)
	glVertex2f(0.0, 0.5)
	glVertex2f(0.5, 0.0)
	glEnd()
	#glutSwapBuffers() hace que se me muestre transparente la pantalla, para solucionar esto usamos el metodo de glFlush()
	glFlush()

def keyPressed(*args):
	key = args[0]
	if key == "r" or key =="R":
		glColor3f(0.8, 0.1, 0.1)
	elif key == "g" or key == "G":
		glColor3f(0.1, 0.7, 0.0)
	elif key ==	"b" or key == "B":
		glColor3f(0.1, 0.3, 0.9)	

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
	glutDisplayFunc(dibujarTriangulo)
	glutIdleFunc(dibujarTriangulo)
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mouseEvent)
	initGL(500,500)
	imprimirMatriz()
	glutMainLoop()
	
if __name__ == "__main__":
	main()
	