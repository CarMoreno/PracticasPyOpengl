from __future__ import division
from OpenGL.GL import *
from OpenGL.GLUT import *
from math import floor

"""Integrantes: Viviana Andrea Zuluaga
				Carlos Andres Moreno
				Daniela Roldan Quiroga"""

#Ejercicio 2.3.2 
#Implemente un metodo para transformar HSV a
#RGB. Dibuje un cuadrado centrado en el origen
# con lado 0.5, muestre tres colores de su preferencia
# especificados en el formato HSV y transforme a
# RGB para pintarlos en OpenGL.				

"""Configuraciones iniciales de la ventana"""
def initGL(width, height):
	glClearColor(0.529, 0.529, 0.529, 0.0)
	#Vamos a definir los 3 colores en formato hsv a continuacion:
	"""Descomentar los otros para ver el resultado"""
	azulFormatoHSV = hsv2rgb(203, 100, 72)#El azul en formato HSV es (203 grad., 100%, 72%)
	rojoFormatoHSV = hsv2rgb(350, 100, 90)#El rojo en formato HSV es (350 grad., 100%, 90%)
	verdeFormatoHSV = hsv2rgb(153, 100, 57)#El verde en formato HSV es (153 grad., 100%, 57%)

	#Ponemos a pintar las componentes que ya estan convetidas a rgb
	glColor3f(azulFormatoHSV[0], azulFormatoHSV[1], azulFormatoHSV[2])
	"""Dscomentar la linea de abajo y comentar la linea de arriba para ver otros colores"""
	# glColor3f(rojoFormatoHSV[0], rojoFormatoHSV[1], rojoFormatoHSV[2])
	# glColor3f(verdeFormatoHSV[0], verdeFormatoHSV[1], verdeFormatoHSV[2])
	glMatrixMode(GL_PROJECTION)

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

def hsv2rgb(h, s, v):
	"""Ëlgoritmo que convierte a rgb un color dado en hsv"""
	colorRgb = []
	hi = floor(h / 60) % 6
	f = ((h / 60) % 6) - hi

	p = v*(1 - s)
	q = v*(1- f*s)
	t = v*(1 - ((1 - f)*s))
	print f,p,q,t

	if hi == 0:
		r = v
		g = t
		b = p
	elif hi == 1:
		r = q
		g = v
		b = p
	elif hi == 2:
		r = p
		g = v
		b = t
	elif hi == 3:
		r = p
		g = q
		b = v
	elif hi == 4:
		r = t
		g = p
		b = v
	else:
		r = v
		g = p
		b = q					

	colorRgb.append(r)
	colorRgb.append(g)
	colorRgb.append(b)
	return colorRgb
	
def main():
	global window
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	
	#creando la ventana
	window = glutCreateWindow("Practica 5")
	#glutKeyboardFunc(keyPressed)
	#glutMouseFunc(mouseEvent)
	glutDisplayFunc(dibujarCuadrado)
	glutIdleFunc(dibujarCuadrado)
	initGL(500,500)
	glutMainLoop()
	
if __name__ == "__main__":
	main()
