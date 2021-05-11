import datetime
import time
import csv

def main():
    print("\nEste algoritmo es un contador que va incrementando su valor cada 2 horas y va a almacenar información, tal como 'conteo actual', 'fecha del conteo', 'hora del conteo' y 'número de día desde que comenzó el conteo.\n")

    contador = 0
    dia = 0
    while (dia < 3):
        # El conteo durará máximo 3 días.
        if contador == 0:
            # Si es la primera iteración añade la cabecera del archivo csv.
            with open("file.csv", mode='x', newline='') as writer:
                # Abre (primero lo crea) el archivo como 'writer'.
                csvWriter = csv.writer(writer, delimiter=',', quotechar='"',
                quoting=csv.QUOTE_ALL)
                # Crea un objeto para escribir el archivo.

                csvWriter.writerow(['dia','fecha','hora','contador (aumenta cada 2 hrs)'])
                # Escribe en el objeto de escritura (escribe nuestro archivo).

        for i in range(24):
            # Por cada vez en un rango de 24 veces.
            time.sleep(7200)
            # Espera 7200 segundos (2 horas)

            with open("file.csv", mode='a', newline='') as writer:
                # Vuelve a abrir el archivo pero en un modo diferente, para
                # añadirle líneas al final del archivo.
                csvWriter = csv.writer(writer, delimiter=',', quotechar='"',
                quoting=csv.QUOTE_ALL)

                today = datetime.datetime.now()
                fecha = f"{ today.day } - { today.month } - { today.year }"
                hora = f"{ today.hour }:{ today.minute }"
                # Agarramos la fecha y hora actual y la almacenamos en
                # variables.

                contador += 1
                # Aumentamos el contador.
                row = [dia, fecha, hora, contador]

                csvWriter.writerow(row)
                # Escribimos todas las variables en una fila en nuestro archivo.
        
        dia += 1
        # Aumentamos el contador de días.

    print(f"\nSe ha finalizado el conteo correctamente.")

if __name__ == '__main__':
    main()
