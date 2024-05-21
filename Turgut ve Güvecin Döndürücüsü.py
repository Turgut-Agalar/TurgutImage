import math
import threading
import matplotlib.pyplot as mpl
from PIL import Image
import numpy as np

degree_to_rad=math.pi/180
def hipotenus_counter(x:int,y:int):
    return round(math.sqrt(x*x+y*y))
def hipotenus_counter_for_image(original_image):
    return hipotenus_counter(original_image.shape[0],original_image.shape[1])
def center_finder(x,y):
    return round(x//2),round(y//2)
def center_finder_for_image(original_image):
    return center_finder(original_image.shape[0],original_image.shape[1])
def origin_changer_to_middle(x,y,center):
    return x-center[0],center[1]-y
def rotated_index_finder_raw(originated_from_middle_coordinates,constantsin,constantcos):
    return (
        originated_from_middle_coordinates[0] * constantcos - originated_from_middle_coordinates[1] * constantsin,
        originated_from_middle_coordinates[0] * constantsin + originated_from_middle_coordinates[1] * constantcos,
    )
def rotated_index_finder(first_x,first_y,constant_sin,constant_cos,center_original,shape_of_new_image):
    return middle_coordinates_to_real_index(rotated_index_finder_raw(origin_changer_to_middle(first_x,first_y,center_original),constant_sin,constant_cos),shape_of_new_image[0:2])
def middle_coordinates_to_real_index(middle_coordinates,shape_of_new_image):
    return round(shape_of_new_image[0] // 2 + middle_coordinates[0]),round(shape_of_new_image[1] // 2 - middle_coordinates[1])
def tilt_angle_sinus_and_cosinus_finder(angle):
    return math.sin(angle), math.cos(angle)
def RGB_transmitter(from_coordinates,to_coordinates):
    to_coordinates[:]=from_coordinates[:]
def new_frame_for_turned_image(max_lenght):
    return np.zeros(max_lenght*max_lenght*3).reshape(max_lenght,max_lenght,3)
def tilter(original_image,tilt_angle):
    max_lenght=hipotenus_counter_for_image(original_image)
    center = center_finder_for_image(original_image)
    free_array_for_tilting = new_frame_for_turned_image(max_lenght)
    constant_sin_and_cos = tilt_angle_sinus_and_cosinus_finder(tilt_angle)
    for i in range(original_image.shape[0]):
        for j in range(original_image.shape[1]):
            rotated_index = rotated_index_finder(i,j,constant_sin_and_cos[0],constant_sin_and_cos[1],center,free_array_for_tilting.shape)
            RGB_transmitter(original_image[i,j,:],free_array_for_tilting[rotated_index[0],rotated_index[1],:])
    return free_array_for_tilting
if __name__ == "__main__":
    myImage = Image.open("DEFAULTPICTURE.jpg")
    newImage = np.array(myImage) / 255
    mpl.imshow(tilter(newImage,30*degree_to_rad))
    mpl.show()
