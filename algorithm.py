import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import math as m

def normalize_2D(normalize, width):
    ################################
    # convert list to 2D list
    ################################
    normalize_2d = []
    list = []
    i = 0
    try:
        while i <= len(normalize):
            if i%width == 0 and i != 0:
                normalize_2d.extend([list])
                list = []
                if i!=len(normalize):
                    list.append(normalize[i])
            else:
                list.append(normalize[i])
            i+=1
    except Exception as e: raise e
    
    return normalize_2d

def find_obj_from_histogram(histo,background):
    #####################################################################
    # find gral level of each object and cut gray level of background out
    #####################################################################
    
    real_gray_level = []
    for i in range(len(histo)):
        if (histo[i] > sum(histo)/(len(histo))) and (i != background):
            real_gray_level.append(i)
    return real_gray_level

def normalize_variant_binary(gray_color, width, height, real):
    ########################################################################
    # initialize normalize 2Dlist size [325][553]
    # normalize keep values 0,1 for each coordinate in list 1D
    # in normalize, cut noise out with detect with real that is list of gray level in each object
    # call normalize_2D function to convert list to list 2D
    # return normalize in 2D list
    ########################################################################
    
    normalize = []
    try:
        for i in range(height):
            for j in range(width):
                if (gray_color[i][j] in real):
                    normalize.append(1)
                else:
                    normalize.append(0)
        
        normalize_2d = normalize_2D(normalize, width)
    except Exception as e: raise e
    
    return normalize_2d

def pq_moment(normalize, gray_pos, obj_gray,pq, width, height):
    ########################################################################
    # this function find pq-moment
    # create moment list that keep pq moment at pq value for each object
    # find each gray level value that same the object gray level value
    # then calculate follow defination of pq moment and put in list_s
    # so list_s keeps all pq-moment for 1 object
    # append list_s to moment and reset to []
    ########################################################################
    moment = []
    for o in range(len(obj_gray)):
        list_s = []
        for k in range(len(pq)):
            summ = 0
            for i in range(height):
                for j in range(width):
                    if (normalize[i][j] == 1) and (gray_pos[i][j] == obj_gray[o]):
                        p = pq[k][0]
                        q = pq[k][1]
                        summ+= (i**p)*(j**q)*normalize[i][j]
            list_s.append(summ)
        moment.extend([list_s])    
    return moment

def position_bar(moment):
    ########################################################################
    # find central of mass for each pq-momen and keep in pos_bar
    ########################################################################
    pos_bar = []
    for i in range(len(moment)):
        x_bar = moment[i][2]/moment[i][0] # m10/m00
        y_bar = moment[i][1]/moment[i][0] # m01/m00
        pos_bar.extend([[x_bar,y_bar]])
    
    return pos_bar

def central_moment(normalize, gray_pos, obj_gray, pq, pos_bar, width, height):
    ########################################################################
    # this function find central moment
    # this algorithm is similar pq-moment algorithm 
    # but change calculate of summ variable
    ########################################################################
    moment = []
    for o in range(len(obj_gray)):
        list_s = []
        for k in range(len(pq)):
            summ = 0
            for i in range(height):
                for j in range(width):
                    if (normalize[i][j] == 1) and (gray_pos[i][j] == obj_gray[o]):
                        p = pq[k][0]
                        q = pq[k][1]
                        summ+= m.pow(i-pos_bar[o][0],p)*m.pow(j-pos_bar[o][1],q)*normalize[i][j]
            list_s.append(round(summ,3))
        # print(list_s)
        moment.extend([list_s])    
    return moment   

def normalize_moment(u_moment,pq):
    
    n_moment = []
    for i in range(len(u_moment)):
        list = []
        p_sum_q = 2
        for j in range(1,len(u_moment[i])):
            p = pq[j-1][0]
            q = pq[j-1][1]
            # print(u_moment[i][j],((p+q)/2)+1)
            nm = u_moment[i][j]/m.pow(u_moment[i][0],((p+q)/2)+1)
            list.append(nm)
        n_moment.extend([list]) 
    return n_moment                  

def histogram(gray_color,width,height):
    histo = [0] * 256
    for i in range(height):
        for j in range(width):
            histo[gray_color[i][j]] += 1 
    return histo

def draw_histogram(data,name):
    ind = []
    ind.extend(range(0,256))
    fig = plt.figure(figsize = (20, 10))
    plt.bar(ind, data, color ='maroon',width = 1)
    plt.xlabel("gray level")
    plt.ylabel("freq")
    plt.title("histogram gray level of"+name)
    plt.show()

def histogram_equalize(pgm_list):
    ################################
    # credit: https://github.com/samsudinng/cv_histogram_equalization/blob/master/demo_notebook/Histogram_Equalization_Grayscale.ipynb
    ################################
    # * convert to numpy array
    pgm_array = np.array(pgm_list)
    # * Calculate normalized histogram and cumulative histogram
    # flatten image array and calculate histogram via binning
    histogram_array = np.bincount(pgm_array.flatten(), minlength=256)

    # normalize
    num_pixels = np.sum(histogram_array)
    histogram_array = histogram_array/num_pixels

    # cumulative histogram
    chistogram_array = np.cumsum(histogram_array)
    
    # * Calculate pixel intensity transformation map
    transform_map = np.floor(255 * chistogram_array).astype(np.uint8)

    # * Equalization by pixel transformation 
    # flatten image array into 1D list
    img_list = list(pgm_array.flatten())

    # transform pixel values to equalize
    eq_img_list = [transform_map[p] for p in img_list]

    # reshape and write back into img_array
    eq_img_array = np.reshape(np.asarray(eq_img_list), pgm_array.shape)

    # Let's plot the histograms

    # histogram and cumulative histogram of original image has been calculated above
    ori_cdf = chistogram_array
    ori_pdf = histogram_array

    # calculate histogram and cumulative histogram of equalized image
    eq_histogram_array = np.bincount(eq_img_array.flatten(), minlength=256)
    num_pixels = np.sum(eq_histogram_array)
    eq_pdf = eq_histogram_array/num_pixels
    eq_cdf = np.cumsum(eq_pdf)

    return eq_img_array, ori_pdf, eq_pdf

def plot_histogram_equal(ori_pdf, eq_pdf, name):
    # * plot histogram graph
    # plot pdf graph
    plt.figure()
    plt.plot(ori_pdf)
    plt.plot(eq_pdf)
    plt.xlabel('Pixel intensity')
    plt.ylabel('Distribution')
    plt.legend(['Original','Equalized'])
    plt.title("histogram gray level of "+name)
    # plt.show() # comment here because want to show 2 graph together
    
    # plot cdf graph
    # plt.figure()
    # plt.plot(ori_cdf)
    # plt.plot(eq_cdf)
    # plt.xlabel('Pixel intensity')
    # plt.ylabel('Distribution')
    # plt.legend(['Original','Equalized'])
    # plt.title("histogram gray level of"+name)
    # plt.show()
    
def create_image(img_arr,file_name):
    eq_img = Image.fromarray(img_arr, mode='L')
    eq_img.save("./src/img/"+file_name+".jpg")
