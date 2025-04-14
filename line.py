def line():
    A = float(input("Ingrese coeficiente A: "))
    B = float(input("Ingrese coeficiente B: "))
    X1 = float(input("Ingrese coeficiente X1: "))
    X2 = float (input("Ingrese coeficiente X2: "))
    print(f"El coeficiente A de su ecuacion de la recta es: {A}")
    print(f"El coeficiente B de su ecuacion de la recta es: {B}")
    print(f"El coeficiente X1 su ecuacion de la recta es: {X1}")
    print(f"El coeficiente X2 su ecuacion de la recta es: {X2}")
    
    print("\n Para la siguiente ecuacion:")
    print(f"\tY= {A}X + {B}")
    
    Y1 = (A*X1)+B
    Y2 = (A*X2)+B
    P1 = f"({X1},{Y1})"
    P2 = f"({X2},{Y2})"

    print(f"\n Dados los siguiente puntos:") 
    print(f"\tP1 {P1}")
    print(f"\tP2 {P2}")
    Distancia= ((X1-X2)**2) + ((Y1-Y2)**2))**(1/2) 
    print(f"\nLa distancia entre ellos es: {Distancia}")
  
