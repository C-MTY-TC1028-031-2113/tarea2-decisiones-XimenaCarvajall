import math

def main():
    
    a=int(input("Da el valor de a: "))
    b=int(input("Da el valor de b: "))
    c=int(input("Da el valor de c: "))
    disc = b**2 - 4*a*c
    if a == 0 and b == 0:
        print("No tiene solución")
    elif a == 0 and b != 0:
        x = -c/b
        print(x)
    elif a != 0 and b != 0 and disc > 0:
        x1 = (-b + math.sqrt(b**2 -4*a*c)) / 2*a
        x2 = (-b - math.sqrt(b**2 -4*a*c)) / 2*a
        print(x1)
        print(x2)
    elif a != 0 and b != 0 and disc < 0:
        print("Raíces complejas")
    elif a != 0 and b != 0 and disc == 0:
        d = -b/(2*a)
        print(d)

if __name__ == '__main__':
    main()
