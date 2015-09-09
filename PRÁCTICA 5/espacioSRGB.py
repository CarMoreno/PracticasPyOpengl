from OpenGL.GL import *
from OpenGL.GLUT import *
from math import sin
from math import cos
from math import pi

"""Integrantes: Viviana Andrea Zuluaga
				Carlos Andres Moreno
				Daniela Roldan Quiroga"""

# Ejercicio 2.3.1				
# Investigue el espacio de color sRGB. Dibuje un
# circulo de radio 0.5 centrado en el origen en
# openGL y muestre tres colores diferentes que se
# muestran respectivamente al hacer clic izquierdo
# con el mouse.				

"""Espacio de color sRGB

Es un espacio de color RGB creado en cooperacion por Hewlett-Packard y Microsoft Corporation. 
Fue aprobado por el W3C, Exif, Intel, Pantone, Corel y otros muchos actores de la industria.
Es importante indicar que el espacio sRGB esta diseniado para coincidir con el utilizado por 
los monitores CRT. Muchos programas de ordenador, tanto profesionales como domesticos, asumen
que una imagen de 8 bits dispuesta en una pantalla con un buffer de 8 bits por canal se mostrara
correctamente. Por esta razon se puede asumir que cualquier imagen de 8 bits sacada de Internet
esta dentro del espacio de color sRGB.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+ Por ultimo y para que no haya dudas, el espacio sRGB es un sub-espacio de RGB, por lo que este ultimo+
+ lo contiene. 																						   +	
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
"""

contador = 0#variable que cuenta la cantidaad de clicks hechos

def initGL(width, height):
	"""Configuraciones iniciales de la ventana"""
	glClearColor(0.529, 0.529, 0.529, 0.0)#Color de fondo
	glMatrixMode(GL_PROJECTION)#Matriz de proyeccion
	glColor3f(0.0, 0.0, 0.0)#Color inicial del circulo
	
def dibujarCirculo():
	"""Funcion que crea un circulo de radio 0.5 centrado en el origen"""
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POLYGON)
	for i in range(400):
		x = 0.25*sin(i) #Cordenadas polares x = r*sin(t) donde r = radio/2 (Circunferencia centrada en el origen)
		y = 0.25*cos(i) #Cordenadas polares y = r*cos(t)
		glVertex2f(x, y)			
	glEnd()
	glFlush()

def mouseEvent(botonMouse, estadoMouse, x, y):
	"""Manejador de eventos de raton"""
	global contador#Cuenta las veces que se hizo click se supone que se muestran tres colores
	if botonMouse == GLUT_LEFT_BUTTON and estadoMouse == GLUT_DOWN: #Si se clickeo con el boton izquierdo del mouse Y ESTE ESTA PRESIONADO
		if contador == 0:
			glColor3f(0.6400, 0.3300, 0.2126)#Color piel srgb
			contador += 1
		elif contador == 1:
			glColor3f(0.3000, 0.6000, 0.7152)#Color azul claro srgb
			contador += 1
		elif contador == 2:
			glColor3f(0.1500, 0.0600, 0.0722)#Color cafe srgb
			contador = 0
		
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
