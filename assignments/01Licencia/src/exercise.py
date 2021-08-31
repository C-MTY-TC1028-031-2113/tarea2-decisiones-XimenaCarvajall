
def main():
    edad = int(input("Ingresa tu edad: "))
    if edad>= 18:
       identificacion = input("¿Tienes identificación? ")
       if identificacion == "si":
          print("Trámite de licencia concedido")
       elif identificacion == "no":
           print("No cumples con los requisitos")
       else:
           print("Respuesta incorrecta")

    else:
        print("No cumples con los requisitos")
if __name__ == '__main__':
    main()
