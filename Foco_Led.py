def Foco_Led():
    print("Seleccione el lugar del Foco: ")
    print("1. HABITACION1")
    print("2. HABITACION2")
    print("3. HABITACION3")
    print("4. HABITACION4")
    print("5. HABITACION5")
    print("6. HABITACION6")
    print("7. HABITACION7")
    #Inicializamos en 0 el número de movimentos en el foco.
    aumento = 0;
    #Ingresar por medio de número el lugar del foco que desea encender.
    opcionMe = input("Ingrese la ubicación del Foco LED Inteligente: ")
    #Crea una función que verifica el espacio del foco
    # Si el foco está en la en la habitación se debe ingresar el número 1.