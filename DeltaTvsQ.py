import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from sklearn.metrics import r2_score


#Import Libraries MatPlotLib, Pandas, and Numpy for data visualization

if __name__ == '__main__':
    file1 = pd.read_excel('Q(0.5)ThroughPlane.xlsx')
    file2 = pd.read_excel('Q(1.0)ThroughPlane.xlsx')
    file3 = pd.read_excel('Q(1.5)ThroughPlane.xlsx')
    file4 = pd.read_excel('Q(2.0)ThroughPlane.xlsx')
    file5 = pd.read_excel('Q(3.0)ThroughPlane.xlsx')
    #An excel file is read into a pandas dataframe --> can now be used for analysis
    deltaT = []
    dt1 = file1['T2-T1']
    dt2 = file2['T2-T1']
    dt3 = file3['T2-T1']
    dt4 = file4['T2-T1']
    dt5 = file5['T2-T1']
    deltaT1=deltaT2=deltaT3=deltaT4=deltaT5=0
    for i in range(len(dt1)):
        if dt1[i]<deltaT1:
            deltaT1 = dt1[i]
    print(deltaT1)
    deltaT.append(deltaT1)
    for i in range(len(dt2)):
        if dt2[i]<deltaT2:
            deltaT2 = dt2[i]
    print(deltaT2)
    deltaT.append(deltaT2)
    for i in range(len(dt3)):
        if dt3[i]<deltaT3:
            deltaT3 = dt3[i]
    print(deltaT3)
    deltaT.append(deltaT3)
    for i in range(len(dt4)):
        if dt4[i]<deltaT4:
            deltaT4 = dt4[i]
    print(deltaT4)
    deltaT.append(deltaT4)
    for i in range(len(dt5)):
        if dt5[i]<deltaT5:
            deltaT5 = dt5[i]
    print(deltaT5)
    deltaT.append(deltaT5)

    Q = [0.5,1,1.5,2,3]

    ΔX = 100/1000
    ΔY = 60/1000
    ΔZ = 12/1000
    SA = (100/1000)*(45/1000)
    #Establishing Dimensions of Battery Cell, Length of X,Y,Z and SA = Area of Heater in meters and square meters
    #Heater was measured to be 100 mm * 45 mm
    #Equation to be modelled: Q/(SA) = -k*(ΔT)/(ΔZ), needed in terms of ΔT in X axis.
    #Reconvert equation to: (-1/k)*Q = (SA/ΔZ)*ΔT

    ThroughPlaneDim = SA/ΔZ
    InPlaneDim = SA/ΔX

    constant = []
    for item in Q:
        constant.append(item/ThroughPlaneDim)

    x = np.array(constant)
    # Converts the excel column for ΔT into a numpy array for the X axis

    y = np.array(deltaT)
    #Converts the array that multiplied ΔT with ΔZ/SA into a numpy array for the Y-Axis

    a,b = np.polyfit(x,y,1)
    #This numpy function creates a linear polynomial best-fit line for the relationship betewen ΔT and Q.

    plt.scatter(x, y, color = 'green')
    #Creates a matplotlib scatterplot with the defined values for the x and y axes

    plt.xlabel("Φ*ΔZ(W/M)") #Labels X axis as Q
    plt.ylabel("ΔTemperature(C)") #Labels Y axis as ΔT

    plt.plot(x, a*x+b,color = 'blue',linestyle = '--', linewidth = 2)
    #Generates a Best-Fit Line on MatPlotLIb for the scatterplot Data

    for i in range(len(x)):
        if (deltaT[i] > (a * x[i] + b)):
            plt.text(x[i], y[i] + 0.3, "ΔT" + str(i + 1) + " Q=" + str(Q[i]), fontsize=12, ha='center', va='bottom')
        else:
            plt.text(x[i], y[i] - 0.4, "ΔT" + str(i + 1) + " Q=" + str(Q[i]), fontsize=12, ha='center', va='bottom')

    k = -1/a
    # Slope A = -1/k, so k (thermal conductivity) = -1/A

    plt.text(2,-4, 'Thermal Conductivity (W/M*K) = ' + '{:.2f}'.format(k), size=12)
    #Prints the slope of the graph at the X and Y coordinates (2,-4),which is the thermal conductivity, k
    r2 = r2_score(y,a*x+b)
    print(r2)
    #Printed R^2 score of 0.998

    plt.show() #Displays Final Graph
