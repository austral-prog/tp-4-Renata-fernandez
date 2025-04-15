def line():
    A = float(input("Ingrese coeficiente A: "))
    B = float(input("Ingrese coeficiente B: "))
    X1 = float(input("Ingrese coeficiente X1: "))
    X2 = float(input("Ingrese coeficiente X2: "))
    
    print(f"El coeficiente A de su ecuación de la recta es: {A}")
    print(f"El coeficiente B de su ecuación de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")
    
    print()
    print("Para la siguiente ecuación:")
    print(f"\ty = {A}x + {B}")
    print()
    
    Y1 = (A * X1) + B
    Y2 = (A * X2) + B
    P1 = f"({X1},{Y1})"
    P2 = f"({X2},{Y2})"
    
    print("Dados los siguientes puntos:")
    print(f"\tP1 {P1}")
    print(f"\tP2 {P2}")
    print()
    
    Distancia = (((X1 - X2) ** 2) + ((Y1 - Y2) ** 2)) ** 0.5
    print(f"La distancia entre ellos es: {Distancia}")
