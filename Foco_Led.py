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
    if opcionMe == '1':
        #Imprime el menú de estado del foco si está apagado se ingresa 1 y si está encendido se ingresa 2
        print("Seleccione el estado de la Habitación: ")
        print("1. Apagado")
        print("2. Encendido")
        
        #Ingresar el estado de la cafetera por medio de los números indicados
        opcionEstado = input("Inserte el estado del Foco Led Inteligente: ")
        
        if opcionEstado == '1':
            opcionEstado = '2'
            
            
            if opcionEstado == '1':
                print("Foco Apagado")
               
            elif opcionEstado == '2':
                 #Muestra un mensaje diciendo que el foco está encendido
                print("El foco se encuentra Encedido ")
            else:
                print("Ingrese el color:") #Colores a escoger
        print("Seleccione el color: ")
        print("0. Blanco")
        print("1. Azul")
        print("2. Rojo")
        
        opcionColor = input("Inserte el color del Foco Led Inteligente: ")
         
        if opcionColor == '0':
                print("Color Blanco activado")
                aumento +=1 #Costo
                print("El costo actual es: " +str(aumento)) 
        if opcionColor == '1':
                print("Color Azul activado")
                aumento +=1
                print("El costo actual es: " +str(aumento)) 
        elif opcionColor == '2':
                print("Color Rojo activado")
                aumento +=1
                print("El costo actual es: " +str(aumento)) 
        else:
        
            print("---FIN DEL PROCESO---")

    
Foco_Led()