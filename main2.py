import pgm
import matplotlib.pyplot as plt
import algorithm as alg
from PIL import Image

# * detail is list [magic number, [width,height], max_value]
# * gray_color_list is 2D list that keep gray level of each coordinate. row is X, column is Y
detail, gray_color_list = pgm.read_pgmb('./src/PGM/SEM256_256.pgm')
detail2, gray_color_list2 = pgm.read_pgmb('./src/PGM/Cameraman.pgm')
width = detail[1][0] # width and height for SEM256_256
height = detail[1][1]
width2 = detail2[1][0] # width and height for Cameraman
height2 = detail2[1][1]

img_array, original, equal = alg.histogram_equalize(gray_color_list) # * equalize image
alg.plot_histogram_equal(original, equal, "SEM256")  # * create histrogram graph compare between original and after enhance.
alg.create_image(img_array, "SEM256_equalize") # * create image after enhance

img_array2, original2, equal2 = alg.histogram_equalize(gray_color_list2)
alg.plot_histogram_equal(original2, equal2, "Cameraman")
alg.create_image(img_array2, "cameraman_equalize")

plt.show()

pgm.write_txt_pgma('./src/readPGM/SEM256_256_pgma.txt', gray_color_list, detail)
pgm.write_txt_pgma('./src/readPGM/Cameraman_pgma.txt', gray_color_list2, detail2)