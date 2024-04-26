import pyedflib
print("Hello")
#crear un objeto EdfReader y cargar el archivo.
edfRreader = pyedflib.EdfReader("chb01_01.edf")
#obtener la informacion general del archivo
num_canales = edfRreader.signals_in_file
print("Numero de canales:", num_canales)
frecuenciaMuestreo = edfRreader.getSampleFrequencies()
print("Frecuencia de muestreo del primer canal:", frecuenciaMuestreo)
duracion = edfRreader.getFileDuration()
print("Duracion del archivo (segundos):", duracion)

#Leer las senales de todos los canales
senales = []
for i in range(num_canales):
    senal = edfRreader.readSignal(i)
    senales.append(senal)

print(senales)