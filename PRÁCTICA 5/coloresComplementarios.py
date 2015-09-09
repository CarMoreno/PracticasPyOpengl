from OpenGL.GL import *
from OpenGL.GLUT import *
from random import random
from math import sin
from math import cos
from math import pi

"""Integrantes: Viviana Andrea Zuluaga
				Carlos Andres Moreno
				Daniela Roldan Quiroga"""

#Ejercicio 2.1 Colores Complementarios
#Dibuje un circulo, escoja el color con que lo va pintar.
# Cada vez que presiona la tecla s se cambia el color por
# su complementario, al presionar la tecla a se cambia el
# color por uno aleatorio. No defina un conjunto colores
# a mostrar si no las funciones necesarias para especificar
# el color y su inverso.	

"""Se manejara el espacio RGB para el ejercicio
El circulo se pintara de rojo inicialmente, pero se podria haber esocgido, verde o azul"""
r = 1
g = 0
b = 0

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


def colorComplemento(r, g, b):
	"""Funcion para definar el color complementario dado un color inicial"""
	colorRgb = [r, g, b]
	for componente in colorRgb:
		if r == 1:#Si se pinta inicialmente el circulo de rojo hallamos su complemento
			colorRgb = [0, 1, 1]
		elif g == 1:#Si se pinta inicialmente el circulo de verde hallamos su complemento
			colorRgb = [1, 0, 1]
		elif b == 1:#Si se pinta inicialmente el circulo de azul hallamos su complemento
			colorRgb = [1, 1, 0]
		else: 
			colorRgb = [0, 0, 0]#Se pinta de negro el circulo cuando el color inicial no es primario	
	glColor3f(colorRgb[0], colorRgb[1], colorRgb[2])#Se establece el color				


def keyPressed(*args):
	"""Funcion que maneja los eventos de tecla"""
	key = args[0]#Obtengo la tecla presionada
	
	if key == "a":
		glColor3f(random(), random(), random())#Cuando se presione 'a' se pinta el circulo con un color al azar		
	elif key == "s":
		colorComplemento(r, g, b)#Obtengo el color complento del color inicial de mi circulo (en nuestro caso el rojo)

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
	glutKeyboardFunc(keyPressed)
	# glutMouseFunc(mouseEvent)
	initGL(500,500)
	glutMainLoop()
	
if __name__ == "__main__":
	main()
			