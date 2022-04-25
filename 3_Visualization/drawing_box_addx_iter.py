import numpy as np
import os

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


# path = "/home/yh/RAISE/3_datasets/KITTI/odom_data/dataset/sequences/00/image_2"
# file_list = os.listdir(path)
# file_list_png = [file for file in file_list if file.endswith(".png")]
# # file_list_png = file_list_png.sort()
# file_name = []
# for file in file_list_png:
#     if file.count(".") == 1:
#         name = file.split(".")[0]
#         file_name.append(name)
#     else:
#         for k in range(len(file) - 1, 0, -1):
#             if file[k] == ".":
#                 file_name.append(file[:k])
#                 break
# # print(file_name)
# # print("file_list_png:{}".format(file_list_png))

# for img_num in file_name:
#     print(int(img_num))
#     img = Image.open(
#         "/home/yh/RAISE/3_datasets/KITTI/odom_data/dataset/sequences/00/image_2/"
#         + str(img_num)
#         + ".png"
#     )
#     draw = ImageDraw.Draw(img)
img_name = (
    "/home/yh/RAISE/3_datasets/KITTI/odom_data/dataset/sequences/00/image_2/000000.png"
)
img = Image.open(img_name)
draw = ImageDraw.Draw(img)
f_read = open("../4_Result/210509/1_result_seg_proj_add_x.txt", "r")
# f_write = open("result_train.txt",'w')

lines = f_read.readlines()
num_prev = 0
for line in lines:
    line_seprated = seprate(line)
    num = int(line_seprated[0])
    x_value = round(float(line_seprated[1]), 2)
    x1 = float(line_seprated[2]) - float(line_seprated[4])
    y1 = float(line_seprated[3]) - float(line_seprated[5])
    x2 = float(line_seprated[2]) + float(line_seprated[4])
    y2 = float(line_seprated[3]) + float(line_seprated[5])
    txt_pos = x1 + 2
    if num > num_prev:
        if num == 0:
            save_path = "./output/00000" + str(num) + ".png"
            img.save("./output/000000.png")
            img_name = (
                "/home/yh/RAISE/3_datasets/KITTI/odom_data/dataset/sequences/00/image_2/00000"
                + str(num)
                + ".png"
            )
            img = Image.open(img_name)
            draw = ImageDraw.Draw(img)
        else:
            if num < 10:
                save_path = "./output/00000" + str(num) + ".png"
                img.save(save_path)
                img_name = (
                    "/home/yh/RAISE/3_datasets/KITTI/odom_data/dataset/sequences/00/image_2/00000"
                    + str(num)
                    + ".png"
                )
                img = Image.open(img_name)
                draw = ImageDraw.Draw(img)
            elif num < 100:
                save_path = "./output/0000" + str(num) + ".png"
                img.save(save_path)
                img_name = (
                    "/home/yh/RAISE/3_datasets/KITTI/odom_data/dataset/sequences/00/image_2/0000"
                    + str(num)
                    + ".png"
                )
                img = Image.open(img_name)
                draw = ImageDraw.Draw(img)
            elif num < 1000:
                save_path = "./output/000" + str(num) + ".png"
                img.save(save_path)
                img_name = (
                    "/home/yh/RAISE/3_datasets/KITTI/odom_data/dataset/sequences/00/image_2/000"
                    + str(num)
                    + ".png"
                )
                img = Image.open(img_name)
                draw = ImageDraw.Draw(img)
            else:
                save_path = "./output/00" + str(num) + ".png"
                img.save(save_path)
                img_name = (
                    "/home/yh/RAISE/3_datasets/KITTI/odom_data/dataset/sequences/00/image_2/00"
                    + str(num)
                    + ".png"
                )
                img = Image.open(img_name)
                draw = ImageDraw.Draw(img)
        print(num_prev)
        num_prev = num
        draw.rectangle(((x1, y1), (x2, y2)), outline=(255, 0, 0), width=5)
        # draw.text((x1, y1 - 10), str(x_value), (255, 255, 255))
        # draw.rectangle((0, 0, 200, 200), outline=(0, 0, 255), width=4)

    else:
        draw.rectangle(((x1, y1), (x2, y2)), outline=(255, 0, 0), width=5)
        # draw.text((x1, y1 - 10), str(x_value), (255, 255, 255))

    # if int(line_seprated[0])>= 2000:
    #     break
print(save_path)
img.save(save_path)


f_read.close
