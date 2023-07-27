import matplotlib.pyplot as plt
import pandas as pd

# Import Libraries MatPlotLib, Pandas, and Numpy for data visualization

if __name__ == '__main__':
    file = pd.read_excel('Discharge_4c_1.xlsx')
    x = file['Time']
    y5 = file['BV']
    plt.plot(x,y5)
    plt.xlabel("Time[s]")  # Labels X axis as Q
    plt.ylabel("BatteryVoltage(BV)")  # Labels Y axis as ΔT
    plt.legend(["BV"], loc="upper left")
    plt.show()