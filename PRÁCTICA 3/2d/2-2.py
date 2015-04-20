"""Integrantes: Carlos Andres Moreno 1255896
				Viviana Andrea Zuluaga 1255455
    Plan: 3743
    Asignatura: Computacion Grafica
    *************************************************************************************

	2.2 Genere un triangulo con base = 0.7 y h = 0.2. Varie la visualizacion en al menos 
		3 conguraciones distintas.."""

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


def dibujaTriangulo():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    imprimirMatrizModelado()
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0.1)  # Crea un vertice situado en el origen de coordenadas x, y
    glVertex2f(-0.35, -0.1)
    glVertex2f(0.35, 0.1)
    glEnd() 
    glFlush()


def teclaPresionada(*args):  #  Otras configuraciones
    tecla = args[0]
    if tecla == "n" or tecla == "N":
    	glViewport(100, 100, 500, 500) 
    	dibujaTriangulo() 
    if tecla == "r" or tecla == "R":   
    	glViewport(250, 250, 500, 500) 
    	dibujaTriangulo()       
    elif tecla == "g" or tecla == "G":  
        glViewport(0, 250, 250, 500)
        dibujaTriangulo()
    elif tecla == "b" or tecla == "B":  
        glViewport(250, 0, 500, 250)
        dibujaTriangulo()


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(500, 500)
	glEnable(GL_LIGHT0)
	glutInitWindowPosition(200, 200)
	glutCreateWindow("Triangulo de b=0.7 y h=0.2")
	inicio()
	glutDisplayFunc(dibujaTriangulo)
	glutKeyboardFunc(teclaPresionada)
	glutMainLoop()


if __name__ == '__main__':
	main()