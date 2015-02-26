from OpenGL.GL import *
from OpenGL.GLUT import *
from random import random
from math import sin
from math import cos
from math import pi

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
# Taller Numero 2 de Computacion Grafica
#=====================================================================													
#Programa que genera un cuadrado de L = 0.5, centrado en el origen
#Como el cuadro esta centrado en el origen, entonces del origen a la izquierda habra 0.25 y 
#del origen a la derecha habra tambien 0.25, para que la suma nos de 0.5

def initGL(width, height):
	glClearColor(0.529, 0.529, 0.529, 0.0)
	glColor3f(0.0, 0.5, 0.0)
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

def gradosAradianes(grados):
	return (grados*pi)/180


contador = 0	
def keyPressed(*args):
	key = args[0]
	#Debo de guardar la identidad en la pila, puesto que si no se hace, se perdera la identidad al multiplicarla mas abajo, y la necesito mas adelante para trasladar y escalar la figura
	if key == "r" or key =="R":
		#Primero defino mi matriz de rotacion, puesto que esta sera la que se multiplacara con la matriz
		#de proyeccion inicial (la identidad), ahora bien, la matriz definida anteriormente, rotara la
		#figura alrededor del eje x.
		matrizRotacion = [1, 0, 0, 0, 0, cos(gradosAradianes(30)), sin(gradosAradianes(30)), 0, 0, -sin(gradosAradianes(30)), cos(gradosAradianes(30)), 0, 0, 0, 0, 1]
		glMultMatrixf(matrizRotacion)#Esta funcion multiplica la matriz de rotacion por la identidad
		#glRotatef(gradosAradianes(30), 1, 0, 0)
	elif key == "t" or key =="T":
		# Cada vez que se presiona t la figura se traslada 0.1 en
		# direccion x y 0.2 en direccion y. Una vez se ha realizado
		# 3 veces este proceso, esta se devuelve y asi sucesivamente.
		global contador
		matrizTraslacion = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0.1, 0.2, 0, 1]#Matriz de traslacion calculada a mano
		devolverse = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, -0.3, -0.6, 0, 1]#Como me desplaze tres veces en total (0.1 en x * 3 + 0.2 en y * 3), entonces me devulevo al punto de partida con x = -0.3 e y = -0.6, 

		if contador == 0 or contador == 1 or contador == 2:
			glMultMatrixf(matrizTraslacion)
			contador += 1
			#glTranslatef(0.1, 0.2, 0.0)
		else:
			glMultMatrixf(devolverse)
			contador = 0			
			#glTranslatef(-0.3, -0.6, 0.0)
			
	# Cada vez que se presiones s se aplica un shade con shx =0.3. Observe los resultados.		
	elif key == "s" or key == "S":
		matrizShade = [1, 0.3, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]#matriz shade calculada a mano
		glMultMatrixf(matrizShade)	

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
