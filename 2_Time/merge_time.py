import numpy as np

np.set_printoptions(precision=2, suppress=True)


def merge_float(data):
    # data.split(' ')
    # print(data.split(' ')[2])
    data = data.split(" ")[0]
    # print("MUNSNDAS"+data)
    merged = merge_data + float(data)

    return merged


def seprate(data):
    # data.split(' ')
    # print(data.split(' ')[2])
    seprated = []
    for i in range(0, 2):
        if i == 1:
            data_splited = data.split(" ")[i]
            data_remove = data_splited.split("\n")[0]
            seprated.append(data_remove)
        else:
            seprated.append(data.split(" ")[i])
    return seprated


f_read_excution = open("result_execution_time(0.3).txt", "r")
f_read_projection = open("result_projection_time.txt", "r")

f_write = open("result_merge_time.txt", "w")

lines_excution = f_read_excution.readlines()
lines_projection = f_read_projection.readlines()

seq = 0
merge_data = 0.0
proper_data = 0

for line_excution in lines_excution:
    excution_seprate = seprate(line_excution)
    for line_projection in lines_projection:
        projection_seprate = seprate(line_projection)

        if excution_seprate[0] == projection_seprate[0]:
            proper_data = projection_seprate[1]
    write_data = float(proper_data) / 4 + (float(excution_seprate[1]) / 1000000)
    print(write_data)
    f_write.write(excution_seprate[0] + " " + str(write_data) + "\n")
    proper_data = 0
f_read_excution.close
f_read_projection.close
f_write.close
