import numpy as np

def read_pgmb(file):
    ############################################################################
    # this function read file pgmb that get path 'file'
    # open file with mode read binary as 'rb'
    # define magic_num, [width,height], max_value to get details of file pgmb
    # in loop get details with read each lines and decode with ascii cause it is text
    # define raster = [] to get gray scale value 
    # make nest loop that get value to put in raster and decode with ord() 
    # return raster and  detail of image pgmb
    ############################################################################
    f = open(file, 'rb')
    # detail file pgmb
    magic_num = 0
    [width, height] = [0,0]
    max_value = 0

    count = 1
    while count<= 3:
        line = f.readline()
        line_dec = line.decode('ascii')
        if not line_dec.find('#'):
            continue
        else:
            line_dec = line_dec.strip('\n')
            if count == 2:
                [w, h] = (line_dec.strip()).split()
                width = int(w)
                height = int(h)
            elif count == 3:
                max_value = int(line_dec)
            else:
                magic_num = line_dec
        count +=1
    detail = [magic_num, [width, height], max_value]
    assert max_value <= 255

    raster = []
    try:
        for y in range(height):
            row = []
            for y in range(width):
                row.append(ord(f.read(1)))
            raster.append(row)
    except Exception as e: raise e
    
    return detail,raster
      
def write_txt_pgma(file,raster,detail):
    ###############################################################################
    # write text file that copy value from .pgm file
    ###############################################################################
    magic_num = detail[0]
    width = detail[1][0]
    height = detail[1][1]
    max_value = detail[2]
    f = open(file,'w')
    f.write(magic_num+'\n')
    f.write(str(width)+' '+str(height)+'\n')
    f.write(str(max_value)+'\n')
    for i in range(height):
        for j in range(width):
            f.write(str(raster[i][j]) + ' ')
        f.write('\n')
    f.close()


def write_pgm(file_name, data, detail):
    ###############################################################################
    # write .pgm file that copy value from .pgm file
    ###############################################################################
    magic_num = detail[0]
    width = detail[1][0]
    height = detail[1][1]
    max_value = detail[2]
    f = open(file_name,'wb')
    # write header file
    f.write(bytes((magic_num+'\n'),'utf-8'))
    f.write(bytes((str(width)+' '+str(height)+'\n'),'utf-8'))
    f.write(bytes((str(max_value)+'\n'),'utf-8'))
    
    #write data file
    data_arr = np.array(data)
    for j in range(height):
        row = list(data_arr[j, : ])
        f.write(bytearray(row))
    f.close()
    
    


