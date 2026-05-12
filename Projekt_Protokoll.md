# 27.02.26

- **Physikalische Grundlagen:**
    
    - Recherche zum Newtonschen Gravitationsgesetz als theoretische Basis: $F = G \frac{m_1 m_2}{r^2}$.
        
    - Erarbeitung der **vektoriellen Form** für Berechnungen im dreidimensionalen Raum: $\vec{F}_1 = G \frac{m_1 m_2}{|\vec{r}_2 - \vec{r}_1|^3}(\vec{r}_2 - \vec{r}_1)$.
        
        
- **Problem & Lösung:**
    
    - **Frage:** Warum steht in der vektoriellen Formel plötzlich ein $r^3$ im Nenner statt $r^2$?.
        
    - **Lösung:** Um die Richtung der Kraft korrekt darzustellen, nutzt man den Differenzvektor. Da dieser aber selbst die Länge $r$ hat, würde er den Betrag der Kraft verfälschen. Man muss ihn durch seine eigene Länge teilen, um einen Einheitsvektor zu erhalten. Mathematisch wird das $r$ aus der Normierung mit dem $r^2$ aus dem Gesetz zu $r^3$ kombiniert.
---
# 06.03.26

- **Physikalische Grundlagen:**
    
    - Erweiterung des Modells auf ein Drei-Körper-System.
        
    - Erarbeitung des Superpositionsprinzips: Die Gesamtkraft auf einen Körper ergibt sich aus der vektoriellen Summe der Gravitationskräfte aller anderen Massen im System.
        
    - Verknüpfung mit dem zweiten Newtonschen Gesetz ($\sum \vec{F} = m \cdot \vec{a}$), um die Beschleunigung $\frac{d^2\vec{x}}{dt^2}$ für jeden Körper einzeln zu berechnen.
        
    - Feststellung, dass sich die Eigenmasse des beschleunigten Körpers aus der Gleichung kürzt, die Beschleunigung also nur von den Massen und Abständen der _anderen_ Körper abhängt.
        
- **Programmteile:**
    
    - Aufstellung des vollständigen Systems aus gekoppelten Differentialgleichungen (ODE-System) für die drei Planeten als mathematisches Gerüst für den Code.
        
- **Problem & Lösung:**
    
    - **Problem:** Recherche ergab, dass dieses System keine analytische Lösung besitzt.
        
    - **Lösung:** Das Problem muss numerisch gelöst werden, was bedeutet, dass der Computer die Positionen in winzigen Zeitschritten immer wieder neu berechnet.
        
---
# 13.03.26

- **Physikalische Grundlagen:**
    
    -  Auseinandersetzung mit der **dimensionslosen Umskalierung**.
        
    - Herleitung der Referenzzeit $T = \sqrt{\frac{L^3}{M \cdot G}}$ durch Dimensionsanalyse der Gravitationskonstante $G$.
        
    - Ziel dieser Herleitung ist es, dass $G$ in den skalierten Gleichungen den Wert 1 annimmt und somit als störende Konstante aus der Berechnung verschwindet.
        
- **Programmteile:**
    
    - Festlegung von Referenzwerten für Masse ($M$) und Länge ($L$), um alle Werte (z. B. $m' = \frac{m}{M}$) für sichere Berechnung mit Python.
        
    - Erstellung der skalierten Bewegungsgleichung, die deutlich kompakter ist als die ursprüngliche Newton-Formel.
        
- **Problem & Lösung:**
    
    - **Problem:** Große Schwierigkeiten bei der korrekten Skalierung der Zeit ($t'$), da die Einheiten konsistent bleiben müssen.
        
    - **Lösung:** Schrittweise Herleitung mithilfe von Online-Recherche und KI-Unterstützung, um sicherzustellen, dass die Einheitenprobe $[\frac{t}{T}] = 1$ ergibt.
---
# 20.03.26

- **Physikalische Grundlagen:**
    
    - Theoretische Umwandlung der Differentialgleichungen zweiter Ordnung in ein System **erster Ordnung**.
        
    - Einführung der Geschwindigkeit $\vec{f}$ als eigenständige Hilfsvariable, sodass die Beschleunigung nun als erste Ableitung der Geschwindigkeit betrachtet wird.
        
- **Programmteile:**
    
    - Auswahl der Libraries: NumPy und SciPy für die numerischen Integrationen sowie Matplotlib für die spätere grafische Ausgabe der Planetenbahnen.
        
    - Konzeption des "Zustandsvektors", der alle Positionen und Geschwindigkeiten der drei Massen in einer Liste zusammenfasst, damit der Solver sie gleichzeitig verarbeiten kann.
        
- **Problem & Lösung:**
    
    - **Problem:** Python-Solver wie `solve_ivp` können mathematisch bedingt nur Gleichungen erster Ordnung lösen ($\frac{d}{dt}$), unser Modell nutzt aber die zweite Ableitung ($\frac{d^2}{dt^2}$).
        
    - **Lösung:** Durch die Aufsplittung jeder Bewegungsgleichung in zwei Teilschritte ($\frac{d\vec{x}}{dt} = \vec{f}$ und $\frac{d\vec{f}}{dt} = \vec{a}$) wurde das Problem für den Computer lösbar gemacht.
---
# 21.03.26

- **Physikalische Grundlagen:** 
	- Erstellung eines detaillierten Physik-Konzeptblatts, um die theoretischen Herleitungen (Gravitationsgesetz, ODE-System, Skalierung) ordentlich zu strukturieren und für die Dokumentation festzuhalten.
    
- **Programmteile:** 
	- Strukturierung der mathematischen Logik als Vorbereitung für die Implementierung in Python.
    
---
# 27.03.26 & 17.04.26

- Keine Fortschritte im IT-Unterricht weil ich Krank war und mich vor und nach der Zeit aufs Abi vorbereit habe.
    
---
# 28.04.26

- **Programmteile:** 
	- Einrichtung eines Repositories auf GitHub.
    
    - Dokumentation des Physik-Konzeptblatts im Repository zur Versionskontrolle.
        
---
# 07.05.26

- **Programmteile:**
    
    - Import der benötigten Bibliotheken.
        
    - Festlegung der Anfangsbedingungen (Positionen und Geschwindigkeiten) sowie der Massen für die drei Körper .
        
    - Implementierung des Differentialgleichungssystems (ODE) erster Ordnung in einer Python-Funktion.
        
    - Durchführung der numerischen Integration mittels der Funktion scipy.integrate.solve_ivp.
        
- **Physikalische Grundlagen:** 
	- Da die Variablen dimensionslos umskaliert wurden, gab es bei der Bestimmung der Konstanten und Anfangswerte keine Einheitenprobleme mehr.
    
- **Problem & Lösung:**
    
    - **Problem:** Schwierigkeiten beim Auslesen und Strukturieren der Ergebnisse aus dem Solver-Objekt.
        
    - **Lösung:** Nutzung von NumPy-Arrays, um die Datenpunkte kompakt zu speichern und gezielt für die einzelnen Koordinaten ($x, y, z$) der Planeten auszulesen. Zur Einarbeitung in scipy wurden Youtube genutzt.
    - https://www.youtube.com/watch?v=BgVJj556fjY
    - https://www.youtube.com/watch?v=rfQZGhT6bfQ
        
---
# 08.05.26

- **Programmteile:**
    
    - Entwicklung der grafischen Darstellung mithilfe von Matplotlib.
        
    - Erstellung eines 3D-Plots, um die berechneten Bahnen der drei Körper zu visualisieren.
        
- **Problem & Lösung:** 
	- 3D-Visualisierung in Matplotlib wurde durch  YouTube-Tutorial  gelöst.
	
---
# 10.05.26

- **Programmteile:**
    
    - Erstellung einer Animation der Planetenbewegung, um den zeitlichen Verlauf der Bahnen sichtbar zu machen.
        
    - Erstellung von **Geschwindigkeitsvektoren** (Pfeile), die sich während der Simulation mit den Körpern mit bewegen (Zusatzaufgabe).
        
- **Physikalische Grundlagen:** 
	- Die Vektoren visualisieren die momentane Änderung der Position ($\vec{f} = \frac{d\vec{x}}{dt}$) direkt im Plot.
    
- **Problem & Lösung:** 
	- Die korrekte Skalierung und Ausrichtung der Vektorpfeile in der Animation erforderte zusätzliche Recherche zur `FuncAnimation`-Schnittstelle und Vektordarstellung in Matplotlib.
	- Animation mit YouTube beigebracht https://www.youtube.com/watch?v=nT16-yQrnFk
	- Vektoren müssen ständig aktualisiert werden und somit nach jeden Frame gelöscht und erstellt werden 
---
# 11.05.26

- **Programmteile:** 
	- Reparatur des Physik-Konzeptblatts und Hinzufügung von Bildern.
	- Hinzufügung des Projektprotokolls auf Github
    
- **Problem & Lösung:**
    
    - **Problem:** Die mathematischen Formeln wurden im Dokument nicht sauber untereinander aufgelistet.
        
    - **Lösung:** Verwendung von Code-Blöcken mit ` ```math ` anstatt mit Dolarsymbolen, um die Formeln korrekt zu formatieren.

--- 
