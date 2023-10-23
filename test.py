import numpy as np

#==================== CONTROL DATA =======================
# test = [
#     1.784, 2.008, 2.373,2.877,3.167, 3.316, 3.886, 4.456, 4.661, 4.979, 5.502, 6.016, 6.193, 6.361, 6.8, 7.548, 7.959, 8.267, 8.65, 9.005, 9.294, 9.649, 9.799, 10.145, 10.967, 11.144, 11.518, 11.62, 12.172, 12.928, 14.348, 14.498, 14.628, 14.993, 15.404, 15.665, 15.955, 16.207, 16.450, 16.590, 17.150, 17.403, 17.561, 17.832, 18.402, 18.757, 19.112, 19.318, 19.542, 20.233
# ]
# testDict = {
    # "in": 1.784,
    # "a": 2.008, 
    # "cozy": 2.373,
    # "cottage": 2.877, "in": 3.167, "the": 3.316, "forest": 3.886,"a": 4.456,"cat": 4.661, "named": 4.979,"whiskers": 5.502,"sat": 6.016,"by": 6.193, "the": 6.361,"window": 6.8,"the": 7.548,"aroma": 7.959,"of": 8.267,"freshly": 8.650,"baked": 9.005,"bread": 9.294,"filled": 9.649,"the": 9.799,"room": 10.145,"creating": 10.967,
#     "a": 11.144,
#     "warm": 11.518,
#     "and": 11.620,
#     "inviting": 12.172,
#     "atmostphere": 12.928,
#     "it": 14.348,
#     "was": 14.498,
#     "a": 14.628,
#     "perfect": 14.993,
#     "moment": 15.404,
#     "to": 15.665,
#     "curl": 15.955,
#     "up":16.207,
#     "by":16.450,
#     "the": 16.590,
#     "fireplace": 17.150,
#     "with": 17.403,
#     "a": 17.561,
#     "book": 17.832,
#     "and": 18.402,
#     "forget": 18.757,
#     "about": 19.112,
#     "the": 19.318,
#     "world": 19.542,
#     "outside": 20.233
# }



# print(len(test))
# for index, num in enumerate(test):
#     test[index] = num + 1


# np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/control/controlData.npz", controlData = test)

# ======================= SHORT CONTROL ======================
# test = [0.819, 1.126, 1.495, 1.751, 1.813, 2.048, 3.134, 3.594, 3.799, 4.035, 4.270, 5.325, 5.622, 5.807, 6.155, 7.220, 7.445, 8.039 ]
# # print(len(test))
# print(len(test))
# for index, num in enumerate(test):
#     test[index] = num + 1
# np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/control/controlShortData.npz", controlShortData = test)

# ======================= LONG CONTROL ======================
# test = [0.434, 1.569,2.560, 3.173, 3.861, 4.577, 5.065, 5.279, 6.077, 6.325, 6.634, 7.192, 7.481, 7.901, 8.472, 8.891, 9.360, 9.456, 10.179, 11.335, 12.360 ]
# # print(len(test))
# print(len(test))
# for index, num in enumerate(test):
#     test[index] = num + 1
# np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/control/controlLongData.npz", controlLongData = test)

# print(len(test))




shengJieControl = [3.052,3.227,3.550,3.896, 3.939, 3.986, 4.510, 4.811, 4.970,5.200, 5.669, 5.836, 5.941, 6.042, 6.449, 7.080, 7.323, 7.498, 7.819 ,7.981, 8.625, 8.891, 9.048, 9.335, 9.715, 9.791, 9.971, 10.154, 10.454, 10.962, 11.615, 11.769, 11.867, 12.155, 12.510, 12.593, 12.807, 12.903, 12.995, 13.072, 13.615, 13.727, 13.847, 13.947, 14.260, 14.550, 14.799, 14.932, 15.077, 15.379]
# print(len(shengJieControl))
shengJieShort = [0.930, 1.148, 1.345, 1.412, 1.471, 1.720, 2.395, 2.561, 2.624, 2.928, 3.117, 3.465, 3.714, 3.825, 4.089, 4.610, 4.748, 5.028]
shengJieLong = [0.883, 1.472, 1.854, 2.363, 2.722, 3.250, 3.513, 3.772, 3.923, 4.014, 4.267, 4.720, 4.859, 5.108, 5.460, 5.742, 5.899, 6.031, 6.542, 7.091, 7.799]
print(len(shengJieControl), len(shengJieLong), len(shengJieShort))

for index, num in enumerate(shengJieControl):
    shengJieControl[index] = num + 1
for index, num in enumerate(shengJieShort):
    shengJieShort[index] = num + 1
for index, num in enumerate(shengJieLong):
    shengJieLong[index] = num + 1
# np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Sheng Jie/controlData", controlDataSJ = shengJieControl)
# np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Sheng Jie/controlData", controlShortDataSJ = shengJieShort)
# np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Sheng Jie/controlData", controlLongDataSJ = shengJieLong)
np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Sheng Jie/controlDataSJ", controlDataSJ = shengJieControl)
np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Sheng Jie/controlDataShortSJ", controlShortDataSJ = shengJieShort)
np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Sheng Jie/controlDataLongSJ", controlLongDataSJ = shengJieLong)


shihuaControl = [
    0.973,  1.045, 1.508, 2.134, 2.255, 2.423, 2.93, 3.477, 3.732, 4.129,  4.754, 4.91, 5.206, 5.344, 5.761, 6.450, 7.018, 7.293, 7.655, 7.875, 8.277, 8.625, 8.917, 9.253, 10.177, 10.37, 10.633, 10.773, 11.395, 11.945, 12.881, 13.066, 13.135, 13.601, 14.189, 14.314, 14.679, 14.774, 15.072, 15.208, 15.938, 16.259, 16.363, 16.607, 17.249, 17.591, 17.852, 18.164, 18.373, 18.842
]
shihuaShort = [0.944, 1.281, 1.656, 1.926, 2.155, 2.525, 3.072, 3.44, 3.612, 3.89, 4.126, 4.897, 5.265, 5.399, 5.797, 6.496, 6.743, 7.129]

shihuaLong = [
    1.531, 2.463, 3.25, 3.865, 4.472, 5.336, 5.738, 6.140, 6.79, 6.884, 7.175, 7.688, 7.85, 8.38, 8.936, 9.338, 9.757, 9.834, 10.604, 11.271, 12.331
]
# print(len(shihuaControl) , len(shihuaShort), len(shihuaLong))
for index, num in enumerate(shihuaControl):
    shihuaControl[index] = num + 1
for index, num in enumerate(shihuaShort):
    shihuaShort[index] = num + 1
for index, num in enumerate(shihuaLong):
    shihuaLong[index] = num + 1
# np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Shihua/controlData", controlDataSH = shihuaControl)
# np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Shihua/controlData", controlShortDataSH = shihuaShort)
# np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Shihua/controlData", controlLongDataSH = shihuaLong)
np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Shihua/controlDataSH", controlDataSH = shihuaControl)
np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Shihua/controlDataShortSH", controlShortDataSH = shihuaShort)
np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Shihua/controlDataLongSH", controlLongDataSH = shihuaLong)

ziguangControl = [
    0.960, 1.111, 1.363,1.906, 2.115, 2.299, 2.857, 3.186, 3.448, 3.841, 4.486, 4.738, 5.063, 5.199, 5.640, 6.586, 7.188, 7.537, 7.891, 8.201, 8.511, 8.870, 9.108, 9.477, 10.477, 10.626, 10.985, 11.164, 11.722, 12.508, 13.410, 13.584, 13.638, 14.021, 14.501, 14.651, 14.957, 15.088, 15.418, 15.495, 16.218, 16.402, 16.470, 16.713, 17.144, 17.523, 17.818, 18.003, 18.221, 18.779
]
ziguangShort = [
    1.151, 1.396, 1.742, 1.952, 2.087, 2.332, 2.923, 3.168, 3.283, 3.459, 3.739, 4.685, 4.970, 5.1, 5.425, 5.956, 6.151, 6.602
]
ziguangLong = [
    1.167, 2.167, 2.911, 3.569, 4.186, 4.776, 5.226, 5.709, 6.594, 6.701, 7.023, 7.640, 7.822, 8.439, 9.089, 9.566, 9.861, 9.982, 10.813, 11.437, 12.537
]
# print(len(ziguangControl), len(ziguangShort), len(ziguangLong))
for index, num in enumerate(ziguangControl):
    ziguangControl[index] = num + 1
for index, num in enumerate(ziguangShort):
    ziguangShort[index] = num + 1
for index, num in enumerate(ziguangLong):
    ziguangLong[index] = num + 1

np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Zi Guang/controlDataZG", controlDataZG = ziguangControl)
np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Zi Guang/controlDataShortZG", controlShortDataZG = ziguangShort)
np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Zi Guang/controlDataLongZG", controlLongDataZG = ziguangLong)

kaibinControl = [
    1.702, 1.792, 2.192, 2.692, 2.763, 2.84, 3.238, 3.508, 3.747, 4.146, 4.555, 4.85, 5.116, 5.23, 5.580, 6.318, 6.786, 6.886, 7.380, 7.543, 7.867, 8.203, 8.332, 8.524, 9.328, 9.479, 9.862, 10.003, 10.401, 11.024, 11.880, 12.002, 12.087, 12.43, 12.872, 12.968, 13.252, 13.355, 13.584, 13.680, 14.325, 14.440, 14.48, 14.705, 15.037, 15.388, 15.675, 15.815, 16.07, 16.575
]
kaibinShort = [
    1.327, 1.539, 1.857, 2.086, 2.209, 2.390, 3.38, 3.653, 3.735, 3.893, 4.187, 4.801, 5.095, 5.266, 5.478, 6.263, 6.47, 6.767
]
kaibinLong = [
    1.618, 2.562, 3.188, 3.694, 4.143, 4.826, 5.184, 5.315, 5.922, 6.14, 6.532, 7.063, 7.154, 7.561, 8.131, 8.556, 8.899, 8.975, 9.546, 10.371, 10.878
]
# print(len(kaibinControl), len(kaibinShort), len(kaibinLong))
for index, num in enumerate(kaibinControl):
    kaibinControl[index] = num + 1
for index, num in enumerate(kaibinShort):
    kaibinShort[index] = num + 1
for index, num in enumerate(kaibinLong):
    kaibinLong[index] = num + 1

np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Kai Bin/controlDataKB", controlDataKB = kaibinControl)
np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Kai Bin/controlDataShortKB", controlShortDataKB = kaibinShort)
np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Kai Bin/controlDataLongKB", controlLongDataKB = kaibinLong)

lerkControl = [
    1.946, 2.078, 2.614, 3.111, 3.296, 3.376, 3.873, 4.455, 4.718, 5.099, 5.754, 6.203, 6.336, 6.451, 6.813, 7.475, 7.972, 8.145, 8.791, 8.899, 9.610, 9.948, 10.100, 10.358, 11.318, 11.459, 11.680, 11.843, 12.434, 13.014, 13.712, 13.865, 13.968, 14.384, 14.652, 14.748, 14.996, 15.157,15.340, 15.430, 16.008, 16.255, 16.348, 16.501, 17.147, 17.499, 17.640, 17.774, 18.008, 18.306]
lerkShort = [
    1.314, 1.515, 1.877, 2.073, 2.162, 2.366, 3.167, 3.490, 3.647,3.828, 4.152, 5.074, 5.364, 5.599, 5.762, 6.708, 6.823, 7.185]
lerkLong = [0.927, 2.103, 3.266, 3.715, 4.421, 5.255, 5.547, 5.781, 6.440, 6.495, 6.922, 7.286, 7.435, 8.007, 8.519, 8.863, 9.144, 9.212, 9.783, 10.995,11.623]
# print(len(lerkControl), len(lerkShort), len(lerkLong))

for index, num in enumerate(lerkControl):
    lerkControl[index] = num + 1
for index, num in enumerate(lerkShort):
    lerkShort[index] = num + 1
for index, num in enumerate(lerkLong):
    lerkLong[index] = num + 1
np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Jialerk/controlDataJL", controlDataJL = lerkControl)
np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Jialerk/controlDataShortJL", controlShortDataJL = lerkShort)
np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/User Studies/Jialerk/controlDataLongJL", controlLongDataJL = lerkLong)




