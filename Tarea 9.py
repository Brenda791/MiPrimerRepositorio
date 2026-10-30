# Ingresar operaciones a realizar
Suma =("num1","num2") 
Resta =("num1","num2")
Multiplicación =("num1","num2")
División =("num1","num2")
print ("Ingrersar dos numeros")
num1=int(input("Numero 1"))
num2=int(input("Numero 2"))
opcion =input("Selecciona lo que quieres hacer con estos dos numerso\n\
=Suma\n\
=Resta\n\
=Multiplicación\n\
=División")
opcion =opcion.lower()
resultado=0
if opcion=="Suma":
 print("resultado:",suma=(num1+num2))
if opcion=="Resta":
 print("resultado:",Resta=(num1-num2))
if opcion=="Multiplicacion":
 print("resultado:",Multiplicación=(num1*num2))  
if opcion=="Division":
 print("resultado:",División=(num1/num2))
else:
    print("la eleccion es icorrecta")
    print(f"el resultado es:{resultado}")