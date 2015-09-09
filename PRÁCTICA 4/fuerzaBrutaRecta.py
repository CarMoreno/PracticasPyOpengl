#
"""Nombres: Carlos Andres Moreno
            Daniela Roldan Quiroga
            Viviana Andrea Zuluaga
    Plan: 3743
    Asignatura: Computacion Grafica
    Practica 4
    *************************************************************************************
"""

# 2. Realice una implementacion que permita aplicar el
# algoritmo de fuerza bruta para trazar la linea entre
# dos puntos arbitrarios.
# Muestre en consola los puntos a pintar para los
# siguientes casos:
#1. (-1,3) a (4,4)
#2. (-3,6) a (6,6)
#Ahora a partir de su implementacion, dibuje con la
#ayuda de la libreria de OpenGL las siguientes rectas:
#1. y = x + 0;3 desde x = -0.6 a x = 0.4.
#2. (-0.6; 0;55) a (0;7; 0;9).
#Pista: Apoyese utilizando la directiva GL_POINTS.

from __future__ import division #Esto es para que el operador de division funcione ademas para division en flotantes
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

def inicio():
	glClearColor(0.53, 0.53, 0.53, 0.0)  # Color de fondo
	glMatrixMode(GL_PROJECTION)  #matriz de proyeccion activa

def draw():
	'''Dibuja con ayuda de la libreria OpenGL las rectas'''
	glClear(GL_COLOR_BUFFER_BIT)  # "Limpiamos" el frame buffer con el color de "glClearColor"
	glPointSize(4.0)
	puntoADibujar = fuerzaBruta(-0.6, -0.3, 0.4, 0.7) # y = x + 0;3 desde x = -0.6 a x = 0.4
	glBegin(GL_POINTS) # Dibuja los puntos obtenidos con el algoritmo
	for i in range(0, len(puntoADibujar)-1, 2): 
		glColor3f(0.0, 0.0, 0.0)  # Se especifica el color
		x = puntoADibujar[i]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla
		y = puntoADibujar[i+1]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
		glVertex2f(x, y)      
	glEnd() 

	glBegin(GL_LINES) # Dibuja las linea desde el primer punto hasta el ultimo punto PUEDEN QUEDAR PUNTOS POR FUERA DE LA LINEA
	glColor3f(0.0, 0.0, 0.0)  # Se especifica el color
	#Se obtienen las primeras y ultimas coordenadas x,y del arreglo de las coordenadas obtenidos en fuerzaBruta
	x1 = puntoADibujar[0]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
	y1 = puntoADibujar[1]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
	x2 = puntoADibujar[-2]*0.7 #Se reduce el tamanio del componente un 70% para que quepa en la grilla 
	y2 = puntoADibujar[-1]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
	glVertex2f(x1, y1) #<=====P1 Donde comenzara la linea
	glVertex2f(x2, y2) #<=====P2 Donde terminara la linea	      
	glEnd() 

	glPointSize(4.0) #tamanno del punto
	puntoADibujar = fuerzaBruta(-0.6, -0.55, 0.7, 0.9) # Linea desde (-0.6, -0.55) hasta (0.7, 0.9)
	glBegin(GL_POINTS) # Dibuja los puntos obtenidos con el algoritmo
	for i in range(0, len(puntoADibujar)-1, 2): 
		glColor3f(1.0, 0.0, 0.0)  # Se especifica el color
		x = puntoADibujar[i]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
		y = puntoADibujar[i+1]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
		glVertex2f(x, y)      
	glEnd()

	glBegin(GL_LINES) # Dibuja las linea desde el primer punto hasta el ultimo punto PUEDEN QUEDAR PUNTOS POR FUERA DE LA LINEA
	glColor3f(1.0, 0.0, 0.0)  # Se especifica el color
	x1 = puntoADibujar[0]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
	y1 = puntoADibujar[1]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
	x2 = puntoADibujar[-2]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
	y2 = puntoADibujar[-1]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
	glVertex2f(x1, y1) #<=====P1 Donde comenzara la linea
	glVertex2f(x2, y2) #<=====P2 Donde terminara la linea		      
	glEnd() 
	glFlush()  # Asegura que los comandos anteriores se van a ejecutar


def  fuerzaBruta(x1, y1, x2, y2):
	#Implementacion del algoritmo de fuerza bruta para rectas
	m = (y2 - y1) / (x2 - x1) #Pendiente
	x = x1
	y = y1
	b = y - (m * x) #Punto de corte
	punto = [] #Declaramos un arreglo con el objetivo de ir guardando los puntos que el algoritmo nos va arrojando
	while x <= x2: #Para x desde x1 hasta x2...
		y = round(float(m*x + b)) #Asi se hayan los componentes y
		x = x + 1
		punto.append(x)
		punto.append(y)	
	return punto #retornamos ese arreglo
		
def imprimePuntos(x1,y1,x2,y2):
	puntos = fuerzaBruta(x1,y1,x2,y2)
	print "Para los puntos P1 = (%s, %s) y P2 = (%s, %s)  se pintara los puntos:\n" % (x1, y1, x2, y2)
	for i in range(0, len(puntos)-1, 2):
		# print "(", misPuntos[x], ",", misPuntos[x+1], ")"
		print "(%s, %s)" % (puntos[i], puntos[i+1]) 

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(500, 500)
	glEnable(GL_LIGHT0)
	glutInitWindowPosition(200, 200)
	glutCreateWindow("Fuerza Bruta para rectas")
	inicio()
	glutDisplayFunc(draw)
	# Muestre en consola los puntos a pintar para los
	# siguientes casos:
	#1. (-1,3) a (4,4)
	#2. (-3,6) a (6,6)
	imprimePuntos(1, 3, 4, 4)
	imprimePuntos(-3, 6, 6, 6)
	glutMainLoop()


if __name__ == '__main__':
	main()