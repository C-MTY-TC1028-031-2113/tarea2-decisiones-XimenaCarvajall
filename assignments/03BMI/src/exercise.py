def main():
    peso = float(input("Dame tu peso en kilogramos: "))
    altura = float(input("Dame tu altura en metros: "))
    if altura <=0 or peso <=0:
        print("Revisa tus datos, alguno de ellos es incorrecto")
    else:
        indicemasa = peso / altura**2
        if indicemasa < 20:
            print(str("PESO BAJO"))
        elif 20 <= indicemasa < 25:
            print(str("PESO NORMAL"))
        elif 25 <= indicemasa < 30:
            print(str("SOBREPESO"))
        elif 30 <= indicemasa < 40:
            print(str("OBESIDAD"))
        else:
            print(str("OBESIDAD MORBIDA"))
            
if __name__=='__main__':
    main()