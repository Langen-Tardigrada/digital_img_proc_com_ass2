# this program solve problems of Histogram and Object Moment 
# in Digital image processing class.

import pgm
import algorithm as alg

# * detail is list [magic number, [width,height], max_value]
# * gray_color_list is 2D list that keep gray level of each coordinate. row is X, column is Y
detail, gray_color_list = pgm.read_pgmb('./src/PGM/scaled_shapes.pgm')
width = detail[1][0]
height = detail[1][1]

# * for compute histrogram, histo is list that index indicate gray level and value indicate number of that gray level
histo = [0] * 256
for i in range(height):
    for j in range(width):
        histo[gray_color_list[i][j]] += 1 

# * obj is list that contain gray level of each object
# * amount
obj = alg.find_obj_from_histogram(histo, 255)

# * convert gray level of each object to 1 and background to 0, use normalize_variant_binary function
normalize = alg.normalize_variant_binary(gray_color_list, width, height, obj)

# * find D or area of each object
D = []
for i in range(len(obj)):
    D.append(histo[obj[i]])

# * the pq-moment
pq = [[0,0],[0,1],[1,0]]
moment = alg.pq_moment(normalize, gray_color_list, obj, pq, width, height)

# * the central moment as u at pq
# * use pq as same as the pq-moment
pos_bar = alg.position_bar(moment)
u_moment = alg.central_moment(normalize, gray_color_list, obj, pq, pos_bar, width, height) 

# * normalized moment 
pq_n = [[0,2],[2,0]]
n_moment = alg.normalize_moment(u_moment, pq_n)

# * quantity
free = []
for i in range(len(n_moment)):
    free.append(sum(n_moment[i]))
    print("Quantity of object that have gray level at {} is {}".format(obj[i],sum(n_moment[i])))

pgm.write_txt_pgma('./src/readPGM/scaled_shapes_pgma_normalize.txt', normalize, detail)
pgm.write_txt_pgma('./src/readPGM/scaled_shapes_pgma.txt', gray_color_list, detail)
