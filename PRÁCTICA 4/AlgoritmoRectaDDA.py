"""Nombres: Carlos Andres Moreno
            Daniela Roldan Quiroga
            Viviana Andrea Zuluaga
    Plan: 3743
    Asignatura: Computacion Grafica
    Practica 4
    *************************************************************************************
"""

#3. Realice una implementacion que permita aplicar el
# algoritmo DDA para trazar la linea entre dos puntos
# arbitrarios.
# Muestre los puntos a pintar en consola para los
# siguientes casos:
# 1. (-5, -8) a (7,3)
# 2. (-6, 7) a (5, 10).
# Ahora a partir de su implementacion, dibuje con la
# ayuda de la libreria de OpenGL las siguientes rectas:
# 1. y = 0.9x -0.3 desde x = -0.7 a x = 0,8.
# 2. (-0.65,-0.45) a (0.7, 0.6).
from __future__ import division #Para dividir correctamente en flotantes
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
	puntoADibujar = DDA(-0.7, -0.93, 0.8, 0.42) # y = 0.9x - 0;3 desde x = -0.7 a x = 0.8
	glBegin(GL_POINTS) # Dibuja los puntos obtenidos con el algoritmo
	for i in range(0, len(puntoADibujar)-1, 2): 
		glColor3f(0.0, 0.0, 0.0)  # Se especifica el color
		x = puntoADibujar[i]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla
		y = puntoADibujar[i+1]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
		glVertex2f(x, y)      
	glEnd() 

	glBegin(GL_LINES) # Dibuja las linea desde el primer punto hasta el ultimo punto PUEDEN QUEDAR PUNTOS POR FUERA DE LA LINEA
	glColor3f(0.0, 0.0, 0.0)  # Se especifica el color
	#Se obtienen las primeras y ultimas coordenadas x,y del arreglo de las coordenadas obtenidos en DDA
	x1 = puntoADibujar[0]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
	y1 = puntoADibujar[1]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
	x2 = puntoADibujar[-2]*0.7 #Se reduce el tamanio del componente un 70% para que quepa en la grilla 
	y2 = puntoADibujar[-1]*0.7 # Se reduce el tamanio del componente un 70% para que quepa en la grilla 
	glVertex2f(x1, y1) #<=====P1 Donde comenzara la linea
	glVertex2f(x2, y2) #<=====P2 Donde terminara la linea	      
	glEnd() 

	glPointSize(4.0) #tamanno del punto
	puntoADibujar = DDA(-0.65, -0.45, 0.7, 0.6) # Linea desde (-0.65, -0.45) hasta (0.7, 0.6)
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


def DDA(x1, y1, x2, y2):
	m = (y2 - y1) / (x2 - x1) #Pendiente
	#print "Pendiente: ",m
	x = x1
	y = y1
	punto = []#Declaramos un arreglo con el objetivo de ir guardando los puntos que el algoritmo nos va arrojando
	while x <= x2:
		y = round(y + m) #Asi hallamos la nueva coordenada Y en cada iteracion
		punto.append(x)
		punto.append(y)
		x = x + 1
	return punto
		
def imprimePuntos(x1,y1,x2,y2):
	puntos = DDA(x1,y1,x2,y2)
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
	glutCreateWindow("Algoritmo DDA para rectas")
	inicio()
	glutDisplayFunc(draw)
	# Muestre los puntos a pintar en consola para los
	# siguientes casos:
	# 1. (-5, -8) a (7,3)
	# 2. (-6, 7) a (5, 10).
	#imprimePuntos(-5, -8, 7, 3)
	imprimePuntos(-6, 7, 5, 10)
	glutMainLoop()


if __name__ == '__main__':
	main()