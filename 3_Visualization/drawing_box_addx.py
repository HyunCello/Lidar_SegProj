import numpy as np

from PIL import Image
from PIL import ImageDraw

np.set_printoptions(precision=2, suppress=True)


def seprate(data):
    # data.split(' ')
    # print(data.split(' ')[2])
    seprated = []
    for i in range(0, 6):
        if i == 5:
            data_splited = data.split(" ")[i]
            data_remove = data_splited.split("\n")[0]
            seprated.append(data_remove)
        else:
            seprated.append(data.split(" ")[i])
    return seprated


# print(img_name)
img = Image.open("./img/001313.png")
draw = ImageDraw.Draw(img)

f_read = open("../4_Result/210509/1_result_seg_proj_add_x_1313.txt", "r")
# f_write = open("result_train.txt",'w')

lines = f_read.readlines()
num_prev = 0
for line in lines:
    line_seprated = seprate(line)
    num = int(line_seprated[0])
    x_value = round(float(line_seprated[1]), 2)
    x1 = float(line_seprated[2]) - float(line_seprated[4]) - 10
    y1 = float(line_seprated[3]) - float(line_seprated[5]) - 10
    x2 = float(line_seprated[2]) + float(line_seprated[4]) - 10
    y2 = float(line_seprated[3]) + float(line_seprated[5])
    txt_pos = x1 + 2
    if num > num_prev:
        if num == 0:
            img.save("./output/000000.png")
            img_name = "./img/00000" + str(num) + ".png"
            img = Image.open(img_name)
            draw = ImageDraw.Draw(img)
        else:
            if num < 10:
                save_path = "./output/00000" + str(num) + ".png"
                img.save(save_path)
                img_name = "./img/00000" + str(num) + ".png"
                img = Image.open(img_name)
                draw = ImageDraw.Draw(img)
            elif num < 100:
                save_path = "./output/0000" + str(num) + ".png"
                img.save(save_path)
                img_name = "./img/0000" + str(num) + ".png"
                img = Image.open(img_name)
                draw = ImageDraw.Draw(img)
                print("HI")
            elif num < 1000:
                save_path = "./output/000" + str(num) + ".png"
                img.save(save_path)
                img_name = "./img/000" + str(num) + ".png"
                img = Image.open(img_name)
                draw = ImageDraw.Draw(img)
            else:
                save_path = "./output/00" + str(num) + ".png"
                img.save(save_path)
                img_name = "./img/00" + str(num) + ".png"
                img = Image.open(img_name)
                draw = ImageDraw.Draw(img)
        print(num_prev)
        num_prev = num
        draw.rectangle(((x1, y1), (x2, y2)), outline=(255, 0, 0), width=5)
        draw.text((x1, y1 - 10), str(x_value), (255, 255, 255))
        # draw.rectangle((0, 0, 200, 200), outline=(0, 0, 255), width=4)

    else:
        draw.rectangle(((x1, y1), (x2, y2)), outline=(255, 0, 0), width=5)
        draw.text((x1, y1 - 10), str(x_value), (255, 255, 255))

    # if int(line_seprated[0])>= 2000:
    #     break
print(save_path)
img.save(save_path)


f_read.close
