import numpy as np
import matplotlib.pyplot as plt

loaded_data = np.load("/Users/wpgoh/Documents/fyp-teleprompter/results/Short/Experiment4.4/data.npz")

loadedControlData = np.load("/Users/wpgoh/Documents/fyp-teleprompter/control/controlShortData.npz")
controlData = loadedControlData["controlShortData"]
xRAWArray = loaded_data["xRAWArray"]
yRAWArray = loaded_data["yRAWArray"]
wordCountTimings = loaded_data["wordCountTimings"]
periodCountTimings = loaded_data["periodCountTimings"]

plt.plot(xRAWArray, yRAWArray)
print(len(wordCountTimings), len(periodCountTimings))
for timings in wordCountTimings:
    plt.axvline(x=timings, color='r', linestyle='--')
for timings in periodCountTimings:
    plt.axvline(x=timings, color='g', linestyle='--')
for timings in controlData:
    plt.plot(timings, 0, marker = "o", color= "pink", markersize=4)
    
plt.xlabel("Time")
plt.ylabel("RMS")

plt.show()

