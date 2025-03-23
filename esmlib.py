import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi # importa Scipy per le immagini
import skimage.io as io # importa il modulo Input/Output di SK-Image

def vediJPEG(filename):
	x = io.imread(filename)
	plt.figure()
	plt.imshow(x, clim=[0,255], cmap="gray")

def vediRAW(filename, shape, typ):
	pass