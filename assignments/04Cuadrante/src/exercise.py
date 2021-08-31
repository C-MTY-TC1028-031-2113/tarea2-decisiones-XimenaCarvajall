def main():
    grados = int(input("Dame los grados: "))
    if grados > 0 and grados < 90:
        print("Cuadrante 1")
    elif grados > 90 and grados < 180:
            print("Cuadrante 2")
    elif grados > 180 and grados < 270:
        print("Cuadrante 3")
    elif grados > 270 and grados < 360:
        print("Cuadrante 4")
    elif grados == 0 or grados == 360 or grados == 90 or grados == 180 or grados == 270:
        print("Eje")
    elif grados < 0 or grados > 360:
        print("Los grados exceden")
if __name__ == '__main__':
    main()
