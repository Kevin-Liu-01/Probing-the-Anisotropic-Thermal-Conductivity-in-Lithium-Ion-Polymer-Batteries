import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Import Libraries MatPlotLib, Pandas, and Numpy for data visualization

if __name__ == '__main__':
    file = pd.read_excel('Discharge_4c_1.xlsx')
    x = file['Time']
    y1 = file['T1']
    y2 = file['T2']
    y3 = file['T3']
    y4 = file['T4']
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.plot(x,y3)
    plt.plot(x,y4)
    plt.xlabel("Time[s]")  # Labels X axis as Q
    plt.ylabel("Temperature[C]")  # Labels Y axis as ΔT
    plt.legend(["T1", "T2", "T3", "T4", "BV"], loc="upper left")
    plt.show()