def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    
    if x < y and x < z and y < z:
        print(x)
        print(y)
        print(z)
    if x < y and x < z and y > z:
        print(x)
        print(z)
        print(y)
    if y < x and y < z and x < z:
        print(y)
        print(x)
        print(z)
    if y < x and y < z and z < x:
        print(y)
        print(z)
        print(x)
    if z < x and z < y and x < y:
        print(z)
        print(x)
        print(y)
    if z < x and z < y and y < x:
        print(z)
        print(y)
        print(x)
        
if __name__=='__main__':
    main()
