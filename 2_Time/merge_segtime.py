import numpy as np

np.set_printoptions(precision=2, suppress=True)


def merge_float(data):
    # data.split(' ')
    # print(data.split(' ')[2])
    data = data.split(" ")[0]
    # print("MUNSNDAS"+data)
    merged = merge_data + float(data)

    return merged


f_read = open("../4_Result/210509/0_time_seg.txt", "r")
f_write = open("../4_Result/210509/0_time_seg_merged.txt", "w")

lines = f_read.readlines()
n = 1
seq = 0
merge_data = 0.0
for line in lines:
    print(line)
    if n == 5:
        merge_data = merge_float(line)
        f_write.write(str(seq) + " " + str(merge_data / 1000000) + "\n")
        seq = seq + 1
        n = 1
        merge_data = 0.0
    else:
        merge_data = merge_float(line)
        n = n + 1
f_read.close
f_write.close
