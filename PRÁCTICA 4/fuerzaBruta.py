# Realice una implementacion que permita aplicar el
# algoritmo de fuerza bruta para trazar la linea entre
# dos puntos arbitrarios.
# Muestre en consola los puntos a pintar para los
# siguientes casos:
#1. (-1,3) a (4,4)
#2. (-3,6) a (6,6)

"""Integrantes: Carlos Andres Moreno 1255896
				Viviana Andrea Zuluaga 1255455
    Plan: 3743
    Asignatura: Computacion Grafica
    *************************************************************************************

	2.1 Genere un cuadrado con L = 0.5, utilice la sentencia glViewport para variar su visualizacion. 
		Varie la visualizacion en al menos 3 configuraciones distintas.."""

from __future__ import division #Esto es para que el operador de division funcione ademas para division en flotantes
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

def inicio():
	glClearColor(0.53, 0.53, 0.53, 0.0)  # Color de fondo
	glMatrixMode(GL_PROJECTION)  #matriz de proyeccion activa

def dibujar_pixel(x, y):
	#print "Vengo de fuerza bruta = ",x,',',y
	x = x * 0.15 # Se reduce el tamano del componente en un 15% para que pueda ser visualizado en la grilla
	y = y * 0.15 # Se reduce el tamano del componente en un 15% para que pueda ser visualizado en la grilla
	#print "Vengo de fuerza bruta reducido = ",x,',',y
	glPointSize(10)#Grosor de los puntos
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()

def  fuerzaBruta(x1, y1, x2, y2):
	#Implementacion del algoritmo de fuerza bruta para rectas
	m = (y2 - y1) / (x2 - x1) #Pendiente
	x = x1
	y = y1
	b = y - (m * x) #Punto de corte
	#punto = [x, y] #Hacemos un arreglo con las coordenadas que se van a ir obteniendo
	while x <= x2: #Para x desde x1 hasta x2...
		y = float(m*x + b) #Asi se hayan los componentes y
		dibujar_pixel(x, round(y))
		x = x + 1
		#punto.append(x)
		#punto.append(y)	
		#imprimePuntos(x1,y1,x2,y2,x,y)
		#print "Para la recta que va desde los puntos P1 = (",x1,",",y1,") hasta p2 = (",x2,",",y2,")"		
	#return punto #retirnamos ese arreglo


def dibujarFuerzaBruta():
	glClear(GL_COLOR_BUFFER_BIT) #Se limpia el buffer de color, (le da un color gris a la ventana)
	fuerzaBruta(-1,3,4,4)
	fuerzaBruta(-3,6,6,6)
		
# def imprimePuntos(x1,y1,x2,y2,x,y):
# 	#print "Para los puntos P1 = (%s, %s) y P2 = (%s, %s)  se pintara el punto: (%s, %s)" % (x1, y1, x2, y2, x, y)
# 	print " "

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(500, 500)
	glEnable(GL_LIGHT0)
	glutInitWindowPosition(200, 200)
	glutCreateWindow("Fuerza Bruta para rectas")
	inicio()
	glutDisplayFunc(dibujarFuerzaBruta)
	glutMainLoop()


if __name__ == '__main__':
	main()