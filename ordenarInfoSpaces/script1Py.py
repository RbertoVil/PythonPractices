
# Este programa va a leer un archivo e imprimir los datos.
# pero reemplazando los espacios por caracteres final de línea.

def main():
    # Función principal.
    file = open("portsInWwwFolder.txt")
    
    auxiliar = ''
    contador = 0

    for linea in file:
        for i in linea:
#            if contador >= 10:
#                break
            if i != " ":
                print(i, end='')
            else:
                print()
#            contador += 1

main()
