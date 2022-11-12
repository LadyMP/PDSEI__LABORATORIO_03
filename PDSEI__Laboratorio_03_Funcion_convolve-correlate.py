# UNIVERSIDAD NACIONAL DE TRUJILLO
# INGENIERIA MECATRONICA
# PROCESAMIENTO DE SEÑALES E IMAGENES

# GRUPO 01
# ELABORADO POR:
    # FERREL ALFARO KEYAR RAUL
    # MENDOZA PASCUAL LADY ALEXANDRA
    # RODRIGUEZ VENTURA CLEVEX MAILZO

#------------------------------------------------------------------------------

import numpy as np                      # Manejar arrays
import matplotlib.pyplot as plt         # Realizar graficos
import sounddevice as sd                # Reproducir audios wav
import soundfile as sf                  # Leer audios wav
plt.style.use(['dark_background'])      # Graficas con temas oscuros

#------------------------------------------------------------------------------

audio = 'AUDIO_LAB_03.wav'      # Nombre del audio
data,fs = sf.read(audio)       # Leer la señal del audio

#------------------------------------------------------------------------------

t = np.arange(0,len(data)/fs,1/fs)
n = len(t)                                  # Numero de muestras en T
señal = np.zeros(len(data))                 
for i in range(len(data)):                  # Convertir stereo a mono
    señal[i]=data[i][0]                     # Señal obtenida del audio

#CREACIÓN DEL KERNEL
kernel = np.exp(-np.linspace(-2,2,31)**2)   #Kernel gaussiano
kernel = kernel/sum(kernel)
# kernel = np.sin(np.linspace(-np.pi,np.pi,31)) #Kernel funcion seno
Nkernel=len(kernel) #Numero de muestras del Kernel (31)
print(f'Numero de muestras del Kernel: {Nkernel}')

#APLICACIÓN DE LA CONVOLUCIÓN
Nconvolucion = n+Nkernel-1
resultado1 = np.convolve(señal, kernel, 'same')
resultado2 = np.correlate(señal, kernel, 'same')

#REPROCUCCION DE AUDIOS
print("Audio Original ...")
sd.play(señal,fs) #audio original
status = sd.wait()
print("Audio Modificado 1 (np.convolve) ...")
sd.play(resultado1,fs) #audio modificado usando convolve
status1 = sd.wait()
print("Audio Modificado 2 (np.correlate) ...")
sd.play(resultado2,fs) #audio modificado usando correlate
status2 = sd.wait()

#GRAFICAR SEÑALES
plt.figure(figsize=(15,6))
   
#Graficar la señal original
plt.subplot(311)
plt.plot(t,señal,'g-',label=('Audio Original') ,linewidth=1)
#plt.xlim([0,n-1])
plt.title('Señal de audio')
plt.grid()
plt.legend(loc='upper left')

#Graficar el kernel
plt.subplot(312)
plt.plot(kernel,'bo-',label=('Kernel'),linewidth=1)
#plt.xlim([0,Nkernel-1])
plt.title('Kernel')
plt.grid()
plt.legend(loc='upper left')

#Graficar Resultados
plt.subplot(313)
plt.plot(t,resultado2,'y-',label=('Audio Modificado - correlate'),linewidth=1)
#plt.xlim([0,Nconvolucion])
plt.title('Resultado de la Convolución')
plt.grid()
plt.legend(loc='upper left')
plt.show()

#GRAFICA DE COMPARACIÓN
plt.figure(figsize=(15,4))
plt.plot(t,resultado1,'r-',label=('Audio Modificado - convolve'),linewidth=1)
plt.plot(t,resultado2,'y-',label=('Audio Modificado - correlate'),linewidth=1)
plt.title('Comparación: Audio modificado usando convolve vs Audio modificado usando correlate')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()
plt.show()