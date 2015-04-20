"""Integrantes: Carlos Andres Moreno 1255896
				Viviana Andrea Zuluaga 1255455
    Plan: 3743
    Asignatura: Computacion Grafica
    *************************************************************************************

	2.1 Genere un cuadrado con L = 0.5, utilice la sentencia glViewport para variar su visualizacion. 
		Varie la visualizacion en al menos 3 configuraciones distintas.."""

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


def imprimirMatrizProyecccion():
	m = glGetFloatv(GL_PROJECTION_MATRIX)
	print "La matriz de proyeccion es:\n\n%s" % str(m) + "\n"


def imprimirMatrizModelado():
	mm = glGetFloatv(GL_MODELVIEW_MATRIX)
	print "La matriz de modelado es:\n\n%s" % str(mm) + "\n"


def inicio():
	glClearColor(0.53, 0.53, 0.53, 0.0)  # Color de fondo
	glMatrixMode(GL_PROJECTION) # Matriz de proyecccion
	glLoadIdentity()
	imprimirMatrizProyecccion()
	


def dibujarCuadrado():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glMatrixMode (GL_MODELVIEW)
	glLoadIdentity()
	imprimirMatrizModelado()	
	glColor3f(0.0, 1.0, 0.0)
	glBegin(GL_QUADS)
	glVertex2f(-0.25, 0.25)
	glVertex2f(-0.25, -0.25)
	glVertex2f(0.25, -0.25)
	glVertex2f(0.25, 0.25)
	glEnd()
	glFlush()


def teclaPresionada(*args):  #  Otras configuraciones
    tecla = args[0]
    if tecla == "n" or tecla == "N":
    	glViewport(30, 100,500, 500) 
    	dibujarCuadrado() 
    if tecla == "r" or tecla == "R":   
    	glViewport(180, 90,300, 300) 
    	dibujarCuadrado()       
    elif tecla == "g" or tecla == "G":  
        glViewport(-200, 200,500, 500)
        dibujarCuadrado()
    elif tecla == "b" or tecla == "B":  
        glViewport(250, 0, 500, 250)
        dibujarCuadrado()


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(500, 500)
	glEnable(GL_LIGHT0)
	glutInitWindowPosition(200, 200)
	glutCreateWindow("Cuadrado lado L = 0.5")
	inicio()
	glutDisplayFunc(dibujarCuadrado)
	glutKeyboardFunc(teclaPresionada)
	glutMainLoop()


if __name__ == '__main__':
	main()