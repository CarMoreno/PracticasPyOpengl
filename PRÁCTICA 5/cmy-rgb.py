from OpenGL.GL import *
from OpenGL.GLUT import *
"""Integrantes: Viviana Andrea Zuluaga
				Carlos Andres Moreno
				Daniela Roldan Quiroga"""

# 2.3.3 Implemente un metodo para transformar CMY a
# RGB. Dibuje un triangulo centrado en el origen
# con lado 0.5 y base 0.5, muestre tres colores de
# su preferencia especificados en el formato CMY y
# transforme a RGB para pintarlos en OpenGL.


def initGL(width, height):
	"""Configuraciones iniciales de la ventana"""
	#Definimos 3 colores y los pasamos a rgb
	blancoFormatoCMY = cmy2rgb(0, 0, 0)#El blanco en formato CMY es (0,0,0)
	negroFormatoCMY = cmy2rgb(1, 1, 1)#El negro en formato CMY es (1,1,1) o bien (255,255,255)
	otroColorCMY = cmy2rgb(0.4, 0.3, 1)#Un verde oliva en formato CMY

	glClearColor(0.529, 0.529, 0.529,  0.0)
	glMatrixMode(GL_PROJECTION)
	glColor3f(0,0,0)
	#Se pintan los colores con sus compoentes ya convertidas a formato rgb
	glColor3f(blancoFormatoCMY[0], blancoFormatoCMY[1], blancoFormatoCMY[2])

	"""Descomentar la linea de abajo y comentar la linea de arriba para ver otros colores"""
	# glColor3f(negroFormatoCMY[0], negroFormatoCMY[1], negroFormatoCMY[2])
	# glColor3f(otroColorCMY[0], otroColorCMY[1], otroColorCMY[2])

def dibujarTriangulo():
	"""Funcion que me dibuja un tirangulo de lado 0.5 y base 0.5 centrado en el origen"""
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_TRIANGLES)
	glVertex2f(0.0, 0.0)
	glVertex2f(0.0, 0.5)
	glVertex2f(0.5, 0.0)
	glEnd()
	#glutSwapBuffers() hace que se me muestre transparente la pantalla, para solucionar esto usamos el metodo de glFlush()
	glFlush()

def cmy2rgb(c, m, y):
	"""Funcion que convierte un color de CMY a RGB"""
	r = 1 - c
	g = 1 - m
	b = 1 - y
	colorRgb = [r, g, b]
	return colorRgb
	
def main():
	global window
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(200,200)
	
	#creando la ventana
	window = glutCreateWindow("Practica 5")
	glutDisplayFunc(dibujarTriangulo)
	glutIdleFunc(dibujarTriangulo)
	initGL(500,500)
	glutMainLoop()
	
if __name__ == "__main__":
	main()
	