import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Import Libraries MatPlotLib, Pandas, and Numpy for data visualization

if __name__ == '__main__':
    file = pd.read_excel('Q(3.0)InPlane.xlsx')
    # An excel file is read into a pandas dataframe --> can now be used for analysis
    Q_Array = file['Q']
    Q_Val = Q_Array[0]
    for i in range(0,len(Q_Array)):
        if Q_Array[i]>Q_Val:
            Q_Val = Q_Array[i]
    print(Q_Val)

    x = np.array(file['Time'])
    # Converts the excel column for ΔT into a numpy array for the X axis

    y1 = np.array(file['T1'])
    # Converts the array that multiplied ΔT with ΔZ/SA into a numpy array for the Y-Axis
    y2 = np.array(file['T2'])

    a = file['Q']
    b = file['Time']
    i= 0
    while a[i] == 0:
        i+=1
    S0 = b[i]
    print("S0",S0)
    while a[i] ==Q_Val:
        i+=1
    S1 = b[i]
    print("S1",S1)

    maxT = y1[0]
    index = 0
    for i in range(len(y1)):
        if y1[i]>maxT:
            maxT = y1[i]
            index = i
    minT = y1[0]
    ind = 0
    for i in range(len(y1)):
        if y1[i]<minT:
            minT = y1[i]
            ind = i

    plt.plot(x, y1, color='green')
    plt.plot(x, y2, color='red')
    plt.plot(S0, color='purple', linestyle='--')  # Add label for T0 to the legend
    plt.plot(S1, color='blue', linestyle='--')   # Add label for T1 to the legend
    plt.plot(maxT, color = 'orange', linestyle ='--')
    plt.plot(minT, color='pink', linestyle='--')

    # Creates a matplotlib scatterplot with the defined values for the x and y axes

    # Adding dashed vertical lines at x = T0 and x = T1
    plt.axvline(S0, color='purple', linestyle='--', label='T0')
    plt.axvline(S1, color='blue', linestyle='--', label='T1')
    plt.axhline(maxT,color = 'orange', linestyle = '--')
    plt.axhline(minT,color = 'pink', linestyle = '--')

    plt.xlabel("Time[s]")  # Labels X axis as Q
    plt.ylabel("Temperature[C]")  # Labels Y axis as ΔT
    plt.ylim([21, 30])
    Final_Time = file['Time'][len(file['Time'])-1]
    plt.xlim([0.5, Final_Time+50])
    plt.legend(["T1","T2","S0","S1"],loc="upper left")

    # Display values of S0 and S1 below the x-axis
    plt.text(S0, 30.5, f"S0={S0}", color='purple', ha='center')
    plt.text(S1, 30.5, f"S1={S1}", color='blue', ha='center')
    plt.text(Final_Time+150, maxT, f"Q ={Q_Val}",color = 'orange', ha = 'center' )
    plt.text(Final_Time+150, minT, f"Q ={0}", color='pink', ha='center')

    plt.show()  # Displays Final Graph
