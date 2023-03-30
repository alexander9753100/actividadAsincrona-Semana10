#mensaje de vien benida
print("\nbien venido al programa\n")

# sele pide al usuario que ingrese el moto a pagar por su compra
compra = float(input("dijite el moto a pagar por su compra: "))

#si el monto a pagar por su compra es negativo osea menor que 0 lo redijira a que ingrese el monto a pagar ya que al ser menor que 0 es una cantidad no valida
while compra <0:
    print("error -> deveria ser un numero positivo")
    compra = float(input("\ndijite el moto a pagar por su compra: "))
    
#si la compra es menor a 500 no sele ara ningun descuento   
if compra <500:
    print("\nel total apaga es de:", compra)
    
 #pero si la compra es igual o mayor que 500 dolares sele hara un descuento del 5%  
elif 500 <= compra <= 500:
    compra -= (compra * 0.05)
    print("\nel total a pagar, con su respectivo des cuento del 5%, es:", compra)
    
# si la compra es igual o mayor que 1000 dolares sele hara un des cuento del 10%  
elif 1000 <= compra <= 1000:
    compra -= (compra * 0.10)
    print("\nel total a pagar, con su respectivo des cuento del 10%, es:", compra)
    
    # mensaje que in dica el fin del programa 
print("\nfin del programa feliz dia\n")