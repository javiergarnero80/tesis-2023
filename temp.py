import matplotlib.pyplot as plt

ruta_archivo = '/home/jlinux/Escritorio/tempdep.txt'  # Reemplaza con el nombre y la ruta de tu archivo de texto

x_vals = []
y_vals = []
ciudades = []  # Lista para almacenar los nombres de las ciudades

with open(ruta_archivo, 'r', encoding='utf-8', errors='replace') as archivo:
    for line in archivo:
        line_parts = line.split()
        if len(line_parts) >= 3:  # Asumiendo que el nombre de la ciudad está en la tercera posición
            try:
                ciudad = line_parts[2]  # Extraer el nombre de la ciudad
                temperatura = float(line_parts[1])  # Obtener la temperatura
                x_vals.append(len(x_vals) + 1)
                y_vals.append(temperatura)
                ciudades.append(ciudad)  # Agregar el nombre de la ciudad a la lista
            except ValueError:
                print(f"Se encontró una línea no válida en el archivo: {line}")
        else:
            print(f"Se encontró una línea no válida en el archivo: {line}")

plt.bar(x_vals, y_vals)  # Gráfico de barras
plt.xlabel('Ciudades')
plt.ylabel('Temperaturas')
plt.title('Gráfico de Temperaturas por ciudades')
plt.xticks(x_vals, ciudades)  # Establecer los nombres de las ciudades en el eje x
plt.grid(True)
plt.show()

indice_max_temperatura = y_vals.index(max(y_vals))
ciudad_max_temperatura = ciudades[indice_max_temperatura]

indice_min_temperatura = y_vals.index(min(y_vals))
ciudad_min_temperatura = ciudades[indice_min_temperatura]

print(f"La ciudad con la temperatura más alta es: {ciudad_max_temperatura}")
print(f"La ciudad con la temperatura más baja es: {ciudad_min_temperatura}")
