import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Import Libraries MatPlotLib, Pandas, and Numpy for data visualization

if __name__ == '__main__':
    file = pd.read_excel('Discharge_4c_1.xlsx')
    T2 = file['T2']
    BV = file['BV']
    Time = file['Time']
    plt.plot(Time,T2, color = 'blue')
    plt.plot(Time,BV, color = 'red')
    plt.show()