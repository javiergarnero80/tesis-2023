import csv
from geopy.geocoders import Nominatim

def obtener_latitud_longitud(ciudad, estado):
    geolocator = Nominatim(user_agent="tu_app")
    
    try:
        ubicacion = geolocator.geocode(f"{ciudad}, {estado}")
        
        if ubicacion:
            latitud = ubicacion.latitude
            longitud = ubicacion.longitude
            return latitud, longitud
        else:
            return None, None
    except Exception as e:
        print(f"Error al obtener la ubicación: {str(e)}")
        return None, None

def guardar_resultado(nombre_archivo, nombre, ciudad, estado, latitud, longitud):
    with open(nombre_archivo, 'a', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow([nombre, ciudad, estado, latitud, longitud])

def main():
    archivo_csv = '/home/jlinux/Escritorio/datos.csv'
    archivo_resultados = 'resultados.csv'
    
    with open(archivo_csv, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        
        for fila in lector_csv:
            name = fila[0]
            ciudad = fila[1]
            estado = fila[2]
            
            latitud, longitud = obtener_latitud_longitud(ciudad, estado)
            
            if latitud is not None and longitud is not None:
                print(f"La latitud y longitud de {name}, {ciudad}, {estado} son: {latitud}, {longitud}")
                guardar_resultado(archivo_resultados, name, ciudad, estado, latitud, longitud)
            else:
                print(f"No se encontraron datos para {name}, {ciudad}, {estado}")
                guardar_resultado(archivo_resultados, name, ciudad, estado, "N/A", "N/A")

if __name__ == "__main__":
    main()
