import numpy as np

from PIL import Image
from PIL import ImageDraw

np.set_printoptions(precision=2, suppress=True)



def seprate(data):
    # data.split(' ')
    # print(data.split(' ')[2])
    seprated = []
    for i in range(0,5):
        if i == 4:
            data_splited = data.split(' ')[i]
            data_remove = data_splited.split('\n')[0]
            seprated.append(data_remove)
        else:
            seprated.append(data.split(' ')[i])
    return seprated


# print(img_name)
img = Image.open("./img/000000.png")
draw = ImageDraw.Draw(img)

f_read = open("result_train.txt",'r')
# f_write = open("result_train.txt",'w')

lines = f_read.readlines()
num_prev = 0
for line in lines:
    line_seprated = seprate(line)
    num = int(line_seprated[0])
    x1 = float(line_seprated[1]) - float(line_seprated[3])
    y1 = float(line_seprated[2]) - float(line_seprated[4])
    x2 = float(line_seprated[1]) + float(line_seprated[3])
    y2 = float(line_seprated[2]) + float(line_seprated[4])
    if num > num_prev:
        if num == 0:
            img.save("./output/000000.png")
            img_name = "./img/00000"+ str(num) +".png"
            img = Image.open(img_name)
            draw = ImageDraw.Draw(img)
        else:
            if num < 10:
                save_path = "./output/00000"+ str(num) +".png"
                img.save(save_path)
                img_name = "./img/00000"+ str(num) +".png"
                img = Image.open(img_name)
                draw = ImageDraw.Draw(img)
            elif num < 100:
                save_path = "./output/0000"+ str(num) +".png"
                img.save(save_path)
                img_name = "./img/0000"+ str(num) +".png"
                img = Image.open(img_name)
                draw = ImageDraw.Draw(img)
            elif num < 1000:
                save_path = "./output/000"+ str(num) +".png"
                img.save(save_path)
                img_name = "./img/000"+ str(num) +".png"
                img = Image.open(img_name)
                draw = ImageDraw.Draw(img)
            else:
                save_path = "./output/00"+ str(num) +".png"
                img.save(save_path)
                img_name = "./img/00"+ str(num) +".png"
                img = Image.open(img_name)
                draw = ImageDraw.Draw(img)
        print(num_prev)
        num_prev = num
        draw.rectangle(((x1, y1), (x2, y2)), outline=(0, 0, 255), width=4)

    else:
        draw.rectangle(((x1, y1), (x2, y2)), outline=(0, 0, 255), width=4)
    # if int(line_seprated[0])>= 2000:
    #     break

f_read.close