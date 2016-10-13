#!/usr/bin/env python
import numpy as np

pi=3.141592653

dest = "../"

xarray = np.linspace(0,3*pi,200)
yarraysum = np.zeros((200,))

Amplitude = [1, 0.6, 0.3, 0.3, 0.1, 0.1]
for n in range(0,5):
    currentAmplitude = Amplitude[n]
    yarray = currentAmplitude*np.sin(n*xarray*np.pi)
    yarraysum += yarray

    savearray = np.array([xarray, yarray]).T

    np.savetxt(dest + "sinus" + str(n)  + ".dat", savearray)


savearray = np.array([xarray, yarraysum]).T
np.savetxt(dest + "sinussumme.dat",savearray)

Amplitude = [1, 0.6, 0.3, 0.3, 0.1, 0.1]
for n in range(0,5):
    currentAmplitude = Amplitude[n]
    yarray = currentAmplitude*np.cos(n*xarray*np.pi)
    yarraysum += yarray

    savearray = np.array([xarray, yarray]).T

    np.savetxt(dest + "cosinus" + str(n)  + ".dat", savearray)


savearray = np.array([xarray, yarraysum]).T
np.savetxt(dest + "schwingungsumme.dat",savearray)



xarray = np.linspace(0,2*pi,50)
yarraysum = np.zeros((50,))
Amplitude = [1]
n=1
currentAmplitude = Amplitude[0]
yarray = currentAmplitude*np.sin(n*xarray)
yarraysum += yarray

savearray = np.array([xarray, yarray]).T
np.savetxt(dest + "puresinus" + str(n)  + ".dat", savearray)

