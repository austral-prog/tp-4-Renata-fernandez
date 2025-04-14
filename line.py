def line():
    A= float(input("Ingrese coeficiente A: "))
    B= float(input("Ingrese coeficiente B: "))
    X1= float(input("Ingrese coeficiente X1: "))
    X2= float (input("Ingrese coeficiente X2: "))

    print(f"El coeficiente A de su ecuacion de la recta es: {A}")
    print(f"El coeficiente B de su ecuacion de la recta es: {B}")
    print(f"El coeficiente X1 su ecuacion de la recta es: {X1}")
    print(f"El coeficiente X2 su ecuacion de la recta es: {X2}")

    print(f"\n Para la siguiente ecuacion:")
    print(f"\t Y= {A}X + {B}"  )

    Y1 = A*X1+B
    Y2 = A*X2+B

    print(f"\n Dados los siguiente puntos:") 
    print(f"\t P1 ({X1},{Y1} )")
    print(f"\t P1 ({X2},{Y2} )")
    
    Distancia= ((X1-X2)**2 + (Y1-Y2)**2)**(1/2)
    
    print(f"La distancia entre ellos es: {Distancia}")
