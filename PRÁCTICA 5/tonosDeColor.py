from OpenGL.GL import *
from OpenGL.GLUT import *
from random import random
from math import sin
from math import cos
from math import pi

"""Integrantes: Viviana Andrea Zuluaga
				Carlos Andres Moreno
				Daniela Roldan Quiroga"""

#Ejercicio 2.2 Tonos de color
# Escoja un color diferente al blanco. Dibuje un circulo,
# al darle clic izquierdo con el mouse aumenta el tono
# de color y con clic derecho disminuye. Pista: Lo que
# debe hacer con este evento es que el valor a multiplicar
# por su color varia entre 0 y 1.

"""Se manejara el espacio RGB para el ejercicio
El circulo se pintara de azul inicialmente, pero se podria haber esocgido, rojo o verde"""
r = 0
g = 0
b = 1
aumentoTono = 0 #Variable de control para el tono

def initGL(width, height):#Configuraciones iniciales de la ventana
	glClearColor(0.529, 0.529, 0.529, 0.0)
	glMatrixMode(GL_PROJECTION)
	glColor3f(r, g, b)
	
def dibujarCirculo():#Funcion que nos dibuja un circulo
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POLYGON)
	for i in range(400):
		x = 0.25*sin(i) #Cordenadas polares x = r*sin(t) donde r = radio/2 (Circunferencia centrada en el origen)
		y = 0.25*cos(i) #Cordenadas polares y = r*cos(t)
		glVertex2f(x, y)			
	glEnd()
	glFlush()
			

def getTono(stepTono):
	"""Funcion de cambio de tono"""
	colorInicial = [r, g, b]#Color inicial de nuestro circulo
	colorConTono = []#aca guardaremos el cambio de tono
	for componente in colorInicial:
		componente = componente*stepTono#Cada componente lo multiplicamos por el escalar que debe estar entre 0 y 1
		colorConTono.append(componente)

	glColor3f(colorConTono[0], colorConTono[1], colorConTono[2])#Establecemos el color con un tono distinto


def mouseEvent(botonMouse, estadoMouse, x, y):
	"""Manejador de eventos de raton"""
	global aumentoTono #Para poder usarla en la funcion necesito especificar que es una variable global
	if botonMouse == GLUT_LEFT_BUTTON and estadoMouse == GLUT_DOWN: #Si clickeo con el boton izquierdo del mouse Y ESTE ESTA PRESIONADO
		aumentoTono = aumentoTono + 0.1#Con el click izquierdo aumenta el tono
		getTono(aumentoTono)	
	if botonMouse == GLUT_RIGHT_BUTTON and estadoMouse == GLUT_DOWN: #Si se clickeo con el boton derecho del mouse Y ESTE ESTA PRESIONADO	
		aumentoTono = aumentoTono - 0.1#Con el click derecho disminuye el tono
		getTono(aumentoTono)

def main():
	global window
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	#creando la ventana
	window = glutCreateWindow("Practica 5")
	glutDisplayFunc(dibujarCirculo)
	glutIdleFunc(dibujarCirculo)
	glutMouseFunc(mouseEvent)
	initGL(500,500)
	glutMainLoop()
	
if __name__ == "__main__":
	main()
