import numpy as np

#==================== CONTROL DATA =======================
test = [
    1.784, 2.008, 2.373,2.877,3.167, 3.316, 3.886, 4.456, 4.661, 4.979, 5.502, 6.016, 6.193, 6.361, 6.8, 7.548, 7.959, 8.267, 8.65, 9.005, 9.294, 9.649, 9.799, 10.145, 10.967, 11.144, 11.518, 11.62, 12.172, 12.928, 14.348, 14.498, 14.628, 14.993, 15.404, 15.665, 15.955, 16.207, 16.450, 16.590, 17.150, 17.403, 17.561, 17.832, 18.402, 18.757, 19.112, 19.318, 19.542, 20.233
]
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
test = [0.434, 1.569,2.560, 3.173, 3.861, 4.577, 5.065, 5.279, 6.077, 6.325, 6.634, 7.192, 7.481, 7.901, 8.472, 8.891, 9.360, 9.456, 10.179, 11.335, 12.360 ]
# print(len(test))
print(len(test))
for index, num in enumerate(test):
    test[index] = num + 1
np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/control/controlLongData.npz", controlLongData = test)

# print(len(test))


