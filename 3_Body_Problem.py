import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
import time



#referenzgrößen aus  skalierung ->für berechnung der der realten werte 
G = 6.674e-11            # gravitationskonstante in m^3/kg·s^2
M = 1.989e30             # sonnenmasse in kg 
# M = 5.972e24             # erdmasse in kg
L = 1.496e11             # referenzlänge = 1 AE in m 
T = np.sqrt(L**3 / (M * G))   # referenzzeit in s
V = L / T                # referenzgeschwindigkeit in m/s




# anfangsbedingungen  
m1, m2, m3 = 1.0, 2.0, 1.5
 
start_postion_1 = [ 1.0,  0.0,  0.5]
start_postion_2 = [-1.0,  0.0, -0.5]
start_postion_3 = [ 0.0,  1.5,  0.0]

start_geschwindigkeit_1 = [ 0.2,  0.5, -0.3]
start_geschwindigkeit_2 = [-0.2, -0.5,  0.3]
start_geschwindigkeit_3 = [ 0.1,  0.0,  0.2]

# anfangsbedingungen für solve ivp
anfangsbedingungen = np.array([
    start_postion_1, start_postion_2, start_postion_3,
    start_geschwindigkeit_1, start_geschwindigkeit_2, start_geschwindigkeit_3
]).ravel()     #macht aus  2D array eine 1D array, damit solve ivp klappt




def system_odes(t, S, m1, m2, m3): #t ist zeit, S zustand, m1, m2, m3 sind massen der planeten für berechnung der beschleunigung

    #herauslesen von position und geschwindigkeit da ergebniss von solve ivp ein einzelnes array ist 
    x1, x2, x3 = S[0:3], S[3:6], S[6:9] 
    dp1_dt, dp2_dt, dp3_dt = S[9:12], S[12:15], S[15:18] 

# Die Änderung der Position ist einfach die aktuelle Geschwindigkeit.
    f1, f2, f3 = dp1_dt, dp2_dt, dp3_dt

    df1_dt = m3*(x3 - x1)/np.linalg.norm(x3 - x1)**3 + m2*(x2 - x1)/np.linalg.norm(x2 - x1)**3
    df2_dt = m3*(x3 - x2)/np.linalg.norm(x3 - x2)**3 + m1*(x1 - x2)/np.linalg.norm(x1 - x2)**3
    df3_dt = m1*(x1 - x3)/np.linalg.norm(x1 - x3)**3 + m2*(x2 - x3)/np.linalg.norm(x2 - x3)**3

    return np.array([f1, f2, f3, df1_dt, df2_dt, df3_dt]).ravel() #wieder 1D array zurückgeben für solve_ivp



#zeitspanne
time_start , time_end = 0, 10
# zeitpunkte für auswertung 
t_points = np.linspace(time_start, time_end, 2001) 

t1 =time.time()
#numerische lösung
solution= solve_ivp(
    fun=system_odes,                    #die funktion die die differenzialgleichungen definiert
    t_span=(time_start, time_end),      #zeitspanne für die integration
    y0=anfangsbedingungen,              #anfangsbedingungen für die integration
    t_eval=t_points,                #zeitpunktewo Lösung ausgewertet wird oll
    args=(m1, m2, m3)           #zusätzliche argumente für system_odes funktion sodass sie in der funktion verwendet werden können

)

#daten für vektor 
v1x_sol = solution.y[9]
v1y_sol = solution.y[10]
v1z_sol = solution.y[11]

v2x_sol = solution.y[12]
v2y_sol = solution.y[13]
v2z_sol = solution.y[14]

v3x_sol = solution.y[15]
v3y_sol = solution.y[16]
v3z_sol = solution.y[17]


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




# für bildung von 3D grafik
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

 #für die bahnen der planeten
planet1_plt, = ax.plot(p1x_sol, p1y_sol, p1z_sol, 'green', label='Planet 1', linewidth=1)
planet2_plt, = ax.plot(p2x_sol, p2y_sol, p2z_sol, 'red', label='Planet 2', linewidth=1)
planet3_plt, = ax.plot(p3x_sol, p3y_sol, p3z_sol, 'blue', label='Planet 3', linewidth=1)

#für die planeten als punkte um nachzuverfolgen 
planet1_dot, = ax.plot([p1x_sol[-1]], [p1y_sol[-1]], [p1z_sol[-1]], 'o', color='green', markersize=6)
planet2_dot, = ax.plot([p2x_sol[-1]], [p2y_sol[-1]], [p2z_sol[-1]], 'o', color='red', markersize=6)
planet3_dot, = ax.plot([p3x_sol[-1]], [p3y_sol[-1]], [p3z_sol[-1]], 'o', color='blue', markersize=6)

#für vektor pfeile
quiver1 = ax.quiver(p1x_sol[-1], p1y_sol[-1], p1z_sol[-1], v1x_sol[-1], v1y_sol[-1], v1z_sol[-1], color='green', length=2)
quiver2 = ax.quiver(p2x_sol[-1], p2y_sol[-1], p2z_sol[-1], v2x_sol[-1], v2y_sol[-1], v2z_sol[-1], color='red', length=0.3)
quiver3 = ax.quiver(p3x_sol[-1], p3y_sol[-1], p3z_sol[-1], v3x_sol[-1], v3y_sol[-1], v3z_sol[-1], color='blue', length=0.3)



ax.set_title("Das 3-Körper Problem")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.grid()
plt.legend()

#textdarstellung für anzeige der abstände und geschwindigkeiten in der animation
info_text = ax.text2D(
    0.01, 0.97, "",
    transform=fig.transFigure,
    fontsize=8,
    verticalalignment='top',
    fontfamily='monospace',
    bbox=dict(boxstyle='round', facecolor='black', alpha=0.5),
    color='white'
)

#startwerte für standbild 
r12_0 = np.linalg.norm(np.array(start_postion_1) - np.array(start_postion_2))
r13_0 = np.linalg.norm(np.array(start_postion_1) - np.array(start_postion_3))
r23_0 = np.linalg.norm(np.array(start_postion_2) - np.array(start_postion_3))

geschwindigkeit1_0 = np.linalg.norm(start_geschwindigkeit_1)
geschwindigkeit2_0 = np.linalg.norm(start_geschwindigkeit_2)
geschwindigkeit3_0 = np.linalg.norm(start_geschwindigkeit_3)

# text für die infobox zusammenbauen und werte mit hilfe der referenzgrößen zurückskalieren und in AE und km/s umrechen 
info_text.set_text(
    f"Abstände:\n"
    f"  r₁₂ = {r12_0 * L / 1.496e11:.3f} AE\n"
    f"  r₁₃ = {r13_0 * L / 1.496e11:.3f} AE\n"
    f"  r₂₃ = {r23_0 * L / 1.496e11:.3f} AE\n"
    f"\nGeschwindigkeiten:\n"
    f"  |v₁| = {geschwindigkeit1_0 * V / 1000:.2f} km/s\n"
    f"  |v₂| = {geschwindigkeit2_0 * V / 1000:.2f} km/s\n"
    f"  |v₃| = {geschwindigkeit3_0 * V / 1000:.2f} km/s"
)

# plt.show()




#animation

#pause button
ax_button = fig.add_axes([0.45, 0.02, 0.1, 0.05])  #links, unten, breite, höhe
btn_pause = Button(ax_button, 'Pause')

#dafür da um Animation zu stoppen und  starten und varuiablen zu speichern
laeuft = [True]  # Liste, damit sie in toggle_pause geändert werden kann

# funktion steuert das pausieren und fortsetzen per button-klick
def toggle_pause(event):  
    if laeuft[0]:
        animation.pause()
        btn_pause.label.set_text('Play')
    else:
        animation.resume()
        btn_pause.label.set_text('Pause')
    laeuft[0] = not laeuft[0]

def update(frame):

    global quiver1, quiver2, quiver3
    quiver1.remove()
    quiver2.remove()
    quiver3.remove()

    x_current_1 = p1x_sol[0:frame+1]
    y_current_1 = p1y_sol[0:frame+1]
    z_current_1 = p1z_sol[0:frame+1]

    x_current_2 = p2x_sol[0:frame+1]
    y_current_2 = p2y_sol[0:frame+1]
    z_current_2 = p2z_sol[0:frame+1]

    x_current_3 = p3x_sol[0:frame+1]
    y_current_3 = p3y_sol[0:frame+1]
    z_current_3 = p3z_sol[0:frame+1]

    planet1_plt.set_data(x_current_1, y_current_1)  
    planet1_plt.set_3d_properties(z_current_1)
    planet1_dot.set_data([x_current_1[-1]], [y_current_1[-1]])
    planet1_dot.set_3d_properties([z_current_1[-1]])

    planet2_plt.set_data(x_current_2, y_current_2)
    planet2_plt.set_3d_properties(z_current_2)
    planet2_dot.set_data([x_current_2[-1]], [y_current_2[-1]])
    planet2_dot.set_3d_properties([z_current_2[-1]])

    planet3_plt.set_data(x_current_3, y_current_3)
    planet3_plt.set_3d_properties(z_current_3)
    planet3_dot.set_data([x_current_3[-1]], [y_current_3[-1]])
    planet3_dot.set_3d_properties([z_current_3[-1]])

    #vektoren 
    quiver1 = ax.quiver(x_current_1[-1], y_current_1[-1], z_current_1[-1], v1x_sol[frame], v1y_sol[frame], v1z_sol[frame], color='green', length=0.3)
    quiver2 = ax.quiver(x_current_2[-1], y_current_2[-1], z_current_2[-1], v2x_sol[frame], v2y_sol[frame], v2z_sol[frame], color='red', length=0.3)
    quiver3 = ax.quiver(x_current_3[-1], y_current_3[-1], z_current_3[-1], v3x_sol[frame], v3y_sol[frame], v3z_sol[frame], color='blue', length=0.3)

    # abstände und geschwindigkeiten berechnen und rückskalieren
    r12 = np.linalg.norm(np.array([x_current_1[-1], y_current_1[-1], z_current_1[-1]]) -
                         np.array([x_current_2[-1], y_current_2[-1], z_current_2[-1]]))
    r13 = np.linalg.norm(np.array([x_current_1[-1], y_current_1[-1], z_current_1[-1]]) -
                         np.array([x_current_3[-1], y_current_3[-1], z_current_3[-1]]))
    r23 = np.linalg.norm(np.array([x_current_2[-1], y_current_2[-1], z_current_2[-1]]) -
                         np.array([x_current_3[-1], y_current_3[-1], z_current_3[-1]]))

    geschwindigkeit1 = np.linalg.norm([v1x_sol[frame], v1y_sol[frame], v1z_sol[frame]])
    geschwindigkeit2 = np.linalg.norm([v2x_sol[frame], v2y_sol[frame], v2z_sol[frame]])
    geschwindigkeit3 = np.linalg.norm([v3x_sol[frame], v3y_sol[frame], v3z_sol[frame]])

    # infobox-text zur laufzeit mit den skalierten echtzeitwerten updaten
    info_text.set_text(
        f"Abstände:\n"
        f"  r₁₂ = {r12 * L / 1.496e11:.3f} AU\n"
        f"  r₁₃ = {r13 * L / 1.496e11:.3f} AU\n"
        f"  r₂₃ = {r23 * L / 1.496e11:.3f} AU\n"
        f"\nGeschwindigkeiten:\n"
        f"  |v₁| = {geschwindigkeit1 * V / 1000:.2f} km/s\n"
        f"  |v₂| = {geschwindigkeit2 * V / 1000:.2f} km/s\n"
        f"  |v₃| = {geschwindigkeit3 * V / 1000:.2f} km/s"
    )


    return planet1_plt, planet1_dot, planet2_plt, planet2_dot, planet3_plt, planet3_dot, quiver1, quiver2, quiver3
    
animation = FuncAnimation(fig, update, frames=range(0, len(t_points), 2), interval=10, blit=False)
btn_pause.on_clicked(toggle_pause)
plt.show()


