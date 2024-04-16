"""
Actividad 1 - IMC
Se solicita crear el programa imc.py que permita calcular el IMC de una persona.
1. Al programa se debe ingresar el peso en Kg y la talla (altura) en centímetros.
(1 Puntos)
2. Calcular el IMC ajustando los valores de entrada a las unidades requeridas por la
fórmula. El resultado se debe informar con 2 decimales.
(2 Puntos)
3. Entregar al usuario una salida acorde que permita conocer el valor de su IMC
además de la clasificación dada por la OMS.
(2 Puntos)
A modo de validación se entregan los siguientes valores para revisar su código:
python imc.py 81 178
Su IMC es 25.56
La clasificación OMS es Sobrepeso
"""

import math

peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en centímetros: "))

altura_m = altura / 100 #Convertir la altura a metros
imc = peso / (altura_m ** 2) #Calcular el IMC
imc = round(imc, 2) #Redondear el imc a 2 decimales

if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc < 25:
    clasificacion = "Peso normal"
elif 25 <= imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print(f"Su IMC es {imc}")

print(f"La clasificación IMS es {clasificacion}")
