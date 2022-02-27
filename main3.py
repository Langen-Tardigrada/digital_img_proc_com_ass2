import pgm

def find_max_min(color):
    max_value = color[0][0]
    min_value = color[0][0]
    try: 
        for i in range(len(color)):
            for j in range(len(color[0])):
                if color[i][j] > max_value:
                    max_value = color[i][j]
                if color[i][j] < min_value:
                    min_value = color[i][j]
    except Exception as e: raise e
    
    return max_value, min_value

def normalize_color(color):
    # normalize between 0 - 255
    list_color = []
    max_color, min_color = find_max_min(color)
    try:
        for i in range(len(color)):
            _list = []
            for j in range(len(color[0])):
                z = (color[i][j]-min_color)/(max_color-min_color) * 255
                _list.append(int(z))
            list_color.extend([_list])
            print(list_color[i])
    except Exception as e: raise e
    
    return list_color

# * detail is list [magic number, [width,height], max_value]
# * gray_color_list is 2D list that keep gray level of each coordinate. row is X, column is Y
detail, red = pgm.read_pgmb('./src/PGM/SanFranPeak_red.pgm')
detail, blue = pgm.read_pgmb('./src/PGM/SanFranPeak_blue.pgm')
detail, green = pgm.read_pgmb('./src/PGM/SanFranPeak_green.pgm')
width = detail[1][0]
height = detail[1][1]

# make gray scale data
all_color_gray = [[]]*height
for i in range(height):
    for j in range(width):
        all_color_gray[i].append(int((red[i][j]+blue[i][j]+green[i][j])/3))
all_normal = normalize_color(all_color_gray)
        
# # excess green 
green_focus = [[]]*height
for i in range(height):
    for j in range(width):
        green_focus[i].append(int(2*green[i][j]-red[i][j]-blue[i][j]))
green_normal = normalize_color(green_focus)

# # focus on red-blue difference
r_b_diff = [[]]*height
for i in range(height):
    for j in range(width):
        r_b_diff[i].append((int(red[i][j]-blue[i][j])))
rb_normal = normalize_color(r_b_diff)

pgm.write_txt_pgma('./src/readPGM/SanFranPeak_red_pgma.txt', red, detail)
pgm.write_txt_pgma('./src/readPGM/SanFranPeak_blue_pgma.txt', blue, detail)
pgm.write_txt_pgma('./src/readPGM/SanFranPeak_green_pgma.txt', green, detail)
pgm.write_txt_pgma('./src/readPGM/SanFranPeak_gray_pgma.txt', all_normal, detail)
pgm.write_txt_pgma('./src/readPGM/SanFranPeak_green_focus.txt', green_normal, detail)
pgm.write_txt_pgma('./src/readPGM/SanFranPeak_red_blue_diff.txt', rb_normal, detail)
pgm.write_pgm('./src/readPGM/SanFranPeak_gray_scale.pgm', all_normal, detail)
pgm.write_pgm('./src/readPGM/SanFranPeak_green_focus.pgm', green_normal, detail)
pgm.write_pgm('./src/readPGM/SanFranPeak_red_blue_diff.pgm', rb_normal, detail)
