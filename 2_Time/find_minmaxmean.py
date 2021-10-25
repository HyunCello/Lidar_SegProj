import numpy as np

np.set_printoptions(precision=2, suppress=True)

# f_read = open("./0509/result_merge_time.txt", "r")
f_read = open("../4_Result/211024/2_time.txt", "r")

lines = f_read.readlines()

values = np.array([])

for line in lines:
    # print(line)
    line = line.split(" ")[1]
    line = line.split("\n")[0]
    # print(float(line))
    # print(line)
    values = np.append(values, float(line))

print(np.max(values))
print(np.min(values))
print(np.mean(values))
