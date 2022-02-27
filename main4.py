import pgm
import matplotlib.pyplot as plt
import algorithm as alg

def write_with_tab_elem(file,arr,detail):
    width = detail[1][0]
    height = detail[1][1]
    try: 
        f = open(file, 'w')
        for i in range(height): #header
            if(i==0): 
                f.write('\t')
            f.write(str(i)+'\t')
        f.write('\n')
        
        for i in range(width):
            f.write(str(i)+'\t')
            for j in range(height):
                f.write(str(arr[i][j]) + '\t')
            f.write('\n')
        f.close() 
    except Exception as e: raise e

detail, grid = pgm.read_pgmb('./src/PGM/grid.pgm') # magic number from detail is 'P5\r' must be strip \r out.
width = detail[1][0]
height = detail[1][1]

detail, distgrid = pgm.read_pgmb('./src/PGM/distgrid.pgm')
detail, distlenna = pgm.read_pgmb('./src/PGM/distlenna.pgm')

# coor priority, row, column, color
cut = [[0,15,15,32],[1,15,31,32],[2,15,47,32],[3,15,63,32],[4,15,79,17],[5,16,95,73],[6,17,111,83],[7,18,127,21],[8,18,143,79],[9,17,159,53],[10,16,175,45],[11,15,191,32],[12,15,207,32],[13,15,223,32],[14,15,239,32],
       [15,31,15,32],[16,31,31,32],[17,31,47,32],[18,32,63,107],[19,34,82,88],[20,37,103,59],[21,39,121,67],[22,42,135,28],[23,42,150,86],[24,40,163,43],[25,37,176,31],[26,34,191,30],[27,32,207,36],[28,31,223,32],[29,31,239,32],
       [30,47,15,32],[31,47,31,32],[32,48,51,32],[33,50,72,54],[34,52,94,94],[35,56,112,89],[36,59,127,42],[37,62,141,63],[38,64,154,85],[39,64,165,12],[40,62,177,67],[41,56,191,47],[42,50,206,42],[43,47,223,4],[44,47,239,32],
       [45,63,15,32],[46,63,33,18],[47,63,56,62],[48,64,78,28],[49,67,100,93],[50,71,118,108],[51,76,132,93],[52,79,143,24],[53,83,155,19],[54,84,165,57],[55,83,177,14],[56,79,190,46],[57,]]

detail[0] = detail[0].strip('\r')
pgm.write_txt_pgma('./src/readPGM/grid.txt', grid, detail)
pgm.write_txt_pgma('./src/readPGM/distgrid.txt', distgrid, detail)
write_with_tab_elem('./src/readPGM/grid_tab.txt',grid, detail)
write_with_tab_elem('./src/readPGM/distgrid_tab.txt',distgrid, detail)
