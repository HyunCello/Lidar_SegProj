import numpy as np
import time

np.set_printoptions(precision=2, suppress=True)
import pandas as pd

pd.options.display.float_format = "{:.f}".format


def projection(data):
    Tr_velo_to_cam = np.array(
        [
            [
                7.533745000000e-03,
                -9.999714000000e-01,
                -6.166020000000e-04,
                -4.069766000000e-03,
            ],
            [
                1.480249000000e-02,
                7.280733000000e-04,
                -9.998902000000e-01,
                -7.631618000000e-02,
            ],
            [
                9.998621000000e-01,
                7.523790000000e-03,
                1.480755000000e-02,
                -2.717806000000e-01,
            ],
            [
                0.000000000000e00,
                0.000000000000e00,
                0.000000000000e00,
                1.000000000000e00,
            ],
        ]
    )

    R0_rect = np.array(
        [
            [
                9.999239000000e-01,
                9.837760000000e-03,
                -7.445048000000e-03,
                0.000000000000e00,
            ],
            [
                -9.869795000000e-03,
                9.999421000000e-01,
                -4.278459000000e-03,
                0.000000000000e00,
            ],
            [
                7.402527000000e-03,
                4.351614000000e-03,
                9.999631000000e-01,
                0.000000000000e00,
            ],
            [
                0.000000000000e00,
                0.000000000000e00,
                0.000000000000e00,
                1.000000000000e00,
            ],
        ]
    )

    P2_rect = np.array(
        [
            [
                7.215377000000e02,
                0.000000000000e00,
                6.095593000000e02,
                4.485728000000e01,
            ],
            [
                0.000000000000e00,
                7.215377000000e02,
                1.728540000000e02,
                2.163791000000e-01,
            ],
            [
                0.000000000000e00,
                0.000000000000e00,
                1.000000000000e00,
                2.745884000000e-03,
            ],
        ]
    )

    Homogeneous_Matrix = P2_rect @ R0_rect @ Tr_velo_to_cam

    output = []
    for i in range(0, 4):
        input_ = [data[i][0], data[i][1], data[i][2]]
        input_matrix = np.array([[input_[0]], [input_[1]], [input_[2]], [1]])
        result = Homogeneous_Matrix @ input_matrix
        scale_mat = np.array([[result[2]], [result[2]], [result[2]]])
        result = result / scale_mat
        result = result[0]
        output.append(result.tolist())
        # print(result.tolist())

    if (
        (np.float_(output[0][0][0]) <= 0)
        or (np.float_(output[1][0][0]) <= 0)
        or (np.float_(output[2][0][0]) <= 0)
        or (np.float_(output[3][0][0]) <= 0)
    ):
        return 0

    else:

        x_min = min(
            np.float_(output[0][0][0]),
            np.float_(output[1][0][0]),
            np.float_(output[2][0][0]),
            np.float_(output[3][0][0]),
        )
        x_max = max(
            np.float_(output[0][0][0]),
            np.float_(output[1][0][0]),
            np.float_(output[2][0][0]),
            np.float_(output[3][0][0]),
        )
        y_min = min(
            np.float_(output[0][1][0]),
            np.float_(output[1][1][0]),
            np.float_(output[2][1][0]),
            np.float_(output[3][1][0]),
        )
        y_max = max(
            np.float_(output[0][1][0]),
            np.float_(output[1][1][0]),
            np.float_(output[2][1][0]),
            np.float_(output[3][1][0]),
        )

        # print(str(x_min) + " " + str(x_max) + " " + str(y_min) + " " + str(y_max))

        # x_middle = (x_min + x_max) / 2 + 621
        x_middle = (x_min + x_max) / 2
        y_middle = (y_min + y_max) / 2
        # if (x_min < 0) and (x_max > 0):
        #     width = abs(x_max - x_min)
        # elif (x_min < 0) and (x_max < 0):
        #     width = abs(x_max + x_min)

        width = abs(x_max - x_min) / 2
        height = abs(y_max - y_min) / 2
        if width < 500 and height < 310:
            result_ = (
                str(x_middle)
                + " "
                + str(y_middle)
                + " "
                + str(width)
                + " "
                + str(height)
                + "\n"
            )
            # print(str(x_middle) + " " + str(y_middle) )
            return result_
        else:
            return 0

    # Image = 1242 x 375 -> -621 to 621, 375/2
    # x1,y1     x2,y2
    # x3,y3     x4,y4


def seprate(data):
    # data.split(' ')
    # print(data.split(' ')[2])
    seprated = []
    for i in range(0, 7):
        if i == 6:
            data_splited = data.split(" ")[i]
            data_remove = data_splited.split("\n")[0]
            seprated.append(data_remove)
        else:
            seprated.append(data.split(" ")[i])
    return seprated


def modify(data):
    # data -> [num, x, y, z, x_length, y_length, z_length]
    x = float(data[1])
    y = float(data[2])
    z = float(data[3])
    x_length = float(data[4])
    y_length = float(data[5])
    z_length = float(data[6])
    if x_length * y_length * z_length < 30:

        x_min = x - x_length / 2
        x_max = x + x_length / 2
        y_min = y - y_length / 2
        y_max = y + y_length / 2
        z_min = z - z_length / 2
        z_max = z + z_length / 2

        # y축은 x축 기준 왼쪽
        # z축은 x축 기준 아래쪽

        x1 = x
        y1 = y_max
        z1 = z_min

        x2 = x
        y2 = y_min
        z2 = z_min

        x3 = x
        y3 = y_max
        z3 = z_max

        x4 = x
        y4 = y_min
        z4 = z_max

        modified = [[x1, y1, z1], [x2, y2, z2], [x3, y3, z3], [x4, y4, z4]]
        # print(modified)
        return modified
    else:
        return 0


f_read = open("../4_Result/211024/0_seg.txt", "r")
f_write = open("../4_Result/211024/1_seg_proj.txt", "w")
f_write_time = open("../4_Result/211024/1_time_proj.txt", "w")
num_prev = 0

lines = f_read.readlines()
start = time.time()
for line in lines:

    line_seprated = seprate(line)

    line_modified = modify(line_seprated)
    if line_modified != 0:
        result = projection(line_modified)
        print(line_seprated[0])
    else:
        continue
    if result != 0:
        # f_write.write(
        #     str(line_seprated[0]) + " " + str(line_seprated[1]) + " " + result
        # )

        f_write.write(str(line_seprated[0]) + " " + result)
        if num_prev < int(line_seprated[0]):
            # print(line_seprated[0])
            # print(time.time() - start)
            f_write_time.write(
                str(line_seprated[0]) + " " + str(time.time() - start) + "\n"
            )

        start = time.time()
        num_prev = int(line_seprated[0])

f_read.close
f_write.close
