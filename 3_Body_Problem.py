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