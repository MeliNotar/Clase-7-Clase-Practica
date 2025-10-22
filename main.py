# JUEGO DE ADIVINANZA

import random

numero_secreto = random.randint(1,30)
incorrecta = True

print("Piense un numero entre 1 y 30, tienes 5 intentos para adivinar")


for intento in range (1,6,1) :        

      
     # while incorrecta:
        adivina = int(input(f"Intento {intento} de 5, ingrese un numero entre 1 y 30: ")) 

        if  adivina == numero_secreto:
            print("Felicitaciones! adivinaste el numero")
            break


        elif adivina < numero_secreto:
            print ("El número es mayor")


        else : 
            print ("El número es menor")     


else : print(f"Lo siento, agotaste los 5 intentos. El número secreto era {numero_secreto}.")