import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
import time

# anfangsbedingungen und konstanten 

m1, m2, m3 = 1.0, 1.0, 1.0
 
start_postion_1 = [1.0, 0.0, 1.0]
start_postion_2 = [1.0, 1.0, 0.0]
start_postion_3 = [0.0, 1.0, 1.0]

start_geschwindigkeit_1 = [0.0, 0.0, -1.0]
start_geschwindigkeit_2 = [0.0, 0.0, 1.0]
start_geschwindigkeit_3 = [0.0, 0.0, -0.6]

# anfangsbedingungen für solve ivp
anfangsbedingungen = np.array([
    start_postion_1, start_postion_2, start_postion_3,
    start_geschwindigkeit_1, start_geschwindigkeit_2, start_geschwindigkeit_3
]).ravel()     #macht aus  2D array eine 1D array, damit solve ivp klappt

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


time_start , time_end = 0, 10
t_points = np.linspace(time_start, time_end, 2001) 

t1 =time.time()
solution= solve_ivp(
    fun=system_odes,                    #die funktion die die differenzialgleichungen definiert
    t_span=(time_start, time_end),      #zeitspanne für die integration
    y0=anfangsbedingungen,              #anfangsbedingungen für die integration
    t_eval=t_points,                #zeitpunktewo Lösung ausgewertet wird oll
    args=(m1, m2, m3)           #zusätzliche argumente für system_odes funktion sodass sie in der funktion verwendet werden können

)


t_sol = solution.t
#positionen der planeten durch berechnung 
p1x_sol = solution.y[0]
p1y_sol = solution.y[1]
p1z_sol = solution.y[2]

p2x_sol = solution.y[3]
p2y_sol = solution.y[4]
p2z_sol = solution.y[5]

p3x_sol = solution.y[6]
p3y_sol = solution.y[7]
p3z_sol = solution.y[8]
# print(p1x_sol)

solution.y.shape

# für bildung von 3D grafik
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

 #für die bahnen der planeten
planet1_plt, = ax.plot(p1x_sol, p1y_sol, p1z_sol, 'green', label='Planet 1', linewidth=1)
planet2_plt, = ax.plot(p2x_sol, p2y_sol, p2z_sol, 'red', label='Planet 2', linewidth=1)
planet3_plt, = ax.plot(p3x_sol, p3y_sol, p3z_sol, 'blue',label='Planet 3', linewidth=1)

#für die planeten als punkte um nachzuverfolgen 
planet1_dot, = ax.plot([p1x_sol[-1]], [p1y_sol[-1]], [p1z_sol[-1]], 'o', color='green', markersize=6)
planet2_dot, = ax.plot([p2x_sol[-1]], [p2y_sol[-1]], [p2z_sol[-1]], 'o', color='red', markersize=6)
planet3_dot, = ax.plot([p3x_sol[-1]], [p3y_sol[-1]], [p3z_sol[-1]], 'o', color='blue', markersize=6)


ax.set_title("The 3-Body Problem")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.grid()
plt.legend()




#animation

def update(frame):

    x_current = p1x_sol[0:frame+1]
    y_current = p1y_sol[0:frame+1]
    z_current = p1z_sol[0:frame+1]

    planet1_plt.set_data(x_current, y_current)  
    planet1_plt.set_3d_properties(z_current)

    planet1_dot.set_data([x_current[-1]], [y_current[-1]])
    planet1_dot.set_3d_properties([z_current[-1]])

    return planet1_plt, planet1_dot 

    
animation = FuncAnimation(fig, update, frames=range(0, len(t_points), 2), interval=10, blit=True)
plt.show()


