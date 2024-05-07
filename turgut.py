import inspect
import numpy as np
def Bebekfurkan(f):
  getattr(__builtins__, f)(inspect.stack()[0][3])


Bebekfurkan("print") #Fonksiyon ismini printliyoru
def imagegrayscale(image:np.array): #Burası içine koyulan fotoğrafı siyahbeyaz yapai
  img_rescaled = image / 255
  grayscale = np.array([0.2126, 0.7152, 0.0722])
  img_gray = np.matmul(img_rescaled, grayscale)
  return img_gray