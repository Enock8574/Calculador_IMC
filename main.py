print("----------#Enoc Carrera ©2021#---------")
print("Este programa le ayudara a conocer su indice de masa corporal")
#Variables para recoger los datos del usuario
altura = float(input("Ingrese su estatura en metros. Ejemplo(1.78) \n"))
peso = float(input("Ingrese su peso en kg(Kilogramos) \n"))
#Variable que resolvera la formula para conocer el IMC
IMC = round(peso/pow(altura,2))
#Condicionales y se determina la condicion del usuario
if IMC < 18.5:
    print(f"su IMC es de {IMC}Usted sufre de peso bajo")
elif IMC < 25:
    print(f"su IMC es de {IMC} Usted tiene un peso normal")
elif IMC < 30:
    print(f"su IMC es de {IMC} Usted tiene un ligero sobrepeso")
else:
    print(f"su IMC es de {IMC} Usted tiene sobrepeso")