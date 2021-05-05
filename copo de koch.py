#LIBRERIAS

#Importamos las librerias necesarias, que son la de turtle para poder dibujar y random para los numeros aleatorios
import random, time					
from turtle import Screen, Turtle

PROFUND  = 5
SIZE     = 7
RELACION = 1.3


DISTANCE    = 150
ANGLE_ALPHA = 24
ANGLE_BETHA = 24








#CONDICIONES INICIALES

pen = Turtle()		      #Le ponemos nombre a nuestra tortuga
screen = Screen()		  #Esta condicion es necesaria para la grama cromatica en las hojas
random.seed()			  #Inicializamos el generador de numeros aleatorios



#Posicion inicial 
pen.penup()
pen.goto(-300,200)
pen.pendown()
pen.speed(10)


pen.pencolor(0,0,0)





def fun(DEPHT, DISTANCE):

	if DEPHT > 0:
		fun(DEPHT - 1, DISTANCE/3)
		pen.left(60)
		fun(DEPHT - 1, DISTANCE/3)
		pen.right(120)
		fun(DEPHT - 1, DISTANCE/3)
		pen.left(60)
		fun(DEPHT - 1, DISTANCE/3)
	else:
		pen.forward(DISTANCE)


	
DEPHT = 4
for _ in range(3):
	fun(DEPHT, 500)
	pen.right(120)

time.sleep(5)