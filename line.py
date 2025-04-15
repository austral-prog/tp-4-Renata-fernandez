def line():
    A = float(input("Ingrese coeficiente A: "))
    B = float(input("Ingrese coeficiente B: "))
    X1 = float(input("Ingrese coeficiente X1: "))
    X2 = float (input("Ingrese coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {A}")
    print(f"El coeficiente B de su ecuación de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")
    
    print("\nPara la siguiente ecuación:")
    print(f"\tY = {A}X + {B}")
    
    Y1 = (A*X1)+B
    Y2 = (A*X2)+B
    P1 = f"({X1}, {Y1})"
    P2 = f"({X2}, {Y2})"

    print(f"\nDados los siguientes puntos:") 
    print(f"\tP1 {P1}")
    print(f"\tP2 {P2}")
    distancia = (((X1-X2)**2) + ((Y1-Y2)**2))**(1/2) 
    print(f"\nLa distancia entre ellos es: {distancia}")
