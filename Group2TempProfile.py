import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

if __name__ == '__main__':
    file = pd.read_excel('Discharge_4c_1.xlsx')
    T2Array = file['T2']
    Time = file['Time']
    plt.plot(Time,T2Array)
    plt.plot(Time,file['BV'])
    plt.show()