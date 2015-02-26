from PIL import Image #La libreria pil me permite manejar imagenes en python

def main():
	imagen = Image.open("integral_vida.jpg")
	imagen.show()

if __name__ == '__main__':
	main()

