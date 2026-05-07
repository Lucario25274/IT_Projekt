import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
import time

# anfangsbedingungen und konstanten 

m1, m2, m3 = 1.0, 1.0, 1.0

#postionen 
start_postion_1 = [1.0, 0.0, 1.0]
start_postion_2 = [1.0, 1.0, 0.0]
start_postion_3 = [0.0, 1.0, 1.0]

#geschwindigkeiten
start_geschwindigkeit_1 = [0.0, 0.0, -1.0]
start_geschwindigkeit_2 = [0.0, 0.0, 1.0]
start_geschwindigkeit_3 = [0.0, 0.0, -0.6]

# anfangsbedingungen für solve ivp
anfangsbedingungen = np.array([
    start_postion_1, start_postion_2, start_postion_3,
    start_geschwindigkeit_1, start_geschwindigkeit_2, start_geschwindigkeit_3
]).ravel()     #macht aus  2D array eine 1D array, damit solveivp klappt

def system_odes(t, S, m1, m2, m3): #t ist zeit, S zustand, m1, m2, m3 sind massen der planeten für berechnung der beschleunigung

    #Print(S) 
    #herauslesen von position und geschwindigkeit da ergebniss von solve ivp ein einzelnes array ist 
    p1, p2, p3 = S[0:3], S[3:6], S[6:9] 
    dp1_dt, dp2_dt, dp3_dt = S[9:12], S[12:15], S[15:18] 

#berechnung beschleunigung von planet zu planet 
    f1, f2, f3 = dp1_dt, dp2_dt, dp3_dt

    df1_dt = m3*(p3 - p1)/np.linalg.norm(p3 - p1)**3 + m2*(p2 - p1)/np.linalg.norm(p2 - p1)**3
    df2_dt = m3*(p3 - p2)/np.linalg.norm(p3 - p2)**3 + m1*(p1 - p2)/np.linalg.norm(p1 - p2)**3
    df3_dt = m1*(p1 - p3)/np.linalg.norm(p1 - p3)**3 + m2*(p2 - p3)/np.linalg.norm(p2 - p3)**3

    return np.array([f1, f2, f3, df1_dt, df2_dt, df3_dt]).ravel() #wieder 1D array zurückgeben für solve_ivp


