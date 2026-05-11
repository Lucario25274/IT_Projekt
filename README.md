# Das Drei-Körper-Problem

> **Projektbeschreibung:** Numerische Simulation der Bahnen dreier Körper unter gegenseitiger Gravitationswechselwirkung.

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Annahmen und Vereinfachungen](#2-annahmen-und-vereinfachungen)
3. [Mathematische Aspekte](#3-mathematische-aspekte)
4. [Skalierung für Python](#4-skalierung-für-python)
5. [Umskalierung der Gleichungen](#5-umskalierung-der-gleichungen)

---

## 1. Einführung

Das Drei-Körper-Problem besteht darin, den Bahnverlauf dreier Körper unter dem Einfluss ihrer gegenseitigen Gravitationskraft vorherzusagen. Ziel dieses Projekts ist es, die Positionen und Geschwindigkeiten der drei Körper näherungsweise zu bestimmen.

---

## 2. Annahmen und Vereinfachungen

| Annahme | Beschreibung |
|---|---|
| Isoliertes System | Keine externen Kräfte auf die betroffenen Körper |
| Massenpunkte | Körper werden als punktförmige Massen dargestellt |
| Gravitationsgesetz | Anziehungskräfte werden mit dem Newtonschen Gravitationsgesetz beschrieben |

---

## 3. Mathematische Aspekte

### 3.1 Einfaches Modell: Zwei Körper

<img width="1552" height="711" alt="Image (3)" src="https://github.com/user-attachments/assets/838324a3-e390-4a4a-bf91-1053fe964668" />

Die Stärke der Gravitationskraft zwischen zwei Körpern ist laut Newtonschen Gravitationsgesetz proportional zum Produkt der wirkenden Massen und umgekehrt proportional zum Quadrat ihres Abstandes:

$$F = G \frac{m_1 m_2}{r^2}$$

Da man Vektoren benötigt, um sich sowohl im zwei- als auch im dreidimensionalen Raum zu bewegen, erweitert man die Formel in die vektorielle Form Für die auf Massenpunkt 1 wirkende Kraft $\vec{F}_1$ gilt:

$$\vec{F}_1 = G \frac{m_1 m_2}{|\vec{r}_2 - \vec{r}_1|^3}(\vec{r}_2 - \vec{r}_1)$$

wobei $\vec{r}_1$ und $\vec{r}_2$ die Positionen (Ortsvektoren) der beiden Massenpunkte sind. Der Verbindungsvektor von Massenpunkt 1 zu Massenpunkt 2 ist definiert als:

$$\vec{r}_{12} := \vec{r}_2 - \vec{r}_1 \qquad \text{mit Betrag } r = |\vec{r}_{12}|$$

---

> [!TIP]
> **Warum steht da ein Hoch 3 statt Hoch 2?**
>
> Das skalare Gravitationsgesetz enthält $r^2$ im Nenner. Um die **Richtung** der Kraft zu berücksichtigen, multipliziert man mit dem Einheitsvektor $\vec{e}_{12}$, der von Körper 1 zu Körper 2 zeigt:
>
> $$\vec{e}_{12} := \frac{\vec{r}_{12}}{r} = \frac{\vec{r}_{12}}{|\vec{r}_{12}|}$$
>
> Setzt man diesen ein, ergibt sich:
>
> $$\vec{F}_1 = \underbrace{G \frac{m_1 m_2}{|\vec{r}_2 - \vec{r}_1|^2}}_{\text{Stärke}} \cdot \underbrace{\frac{(\vec{r}_2 - \vec{r}_1)}{|\vec{r}_2 - \vec{r}_1|}}_{\text{Richtung}} = G \frac{m_1 m_2}{|\vec{r}_2 - \vec{r}_1|^3}(\vec{r}_2 - \vec{r}_1)$$
>
> Das r³ kommt daher, dass man das r² aus dem Gravitationsgesetz und das r aus dem Richtungsvektor zusammenmultipliziert. Das ergibt dasselbe wie wenn man einen extra Einheitsvektor hinschreibt. Es ist bloß kürzer

---

Verallgemeinert man die Formel für beliebige Massenpunkte $x_i$ und $x_j$, ergibt sich:

$$\vec{F}_{x_i \leftarrow x_j} = G \frac{m_i \, m_j}{|\vec{x}_j - \vec{x}_i|^3} (\vec{x}_j - \vec{x}_i)$$

---

### 3.2 Verbindung zu Newtons zweitem Gesetz

Wirken mehrere Kräfte auf einen Körper, werden alle aufaddiert. Die Summe ergibt die Gesamtbeschleunigung:

$$\sum \vec{F}_{ij} = m \cdot \vec{a} = m \frac{d\vec{v}}{dt} = m \frac{d^2\vec{x}}{dt^2}$$

| Symbol | Bedeutung |
|---|---|
| $\vec{a}$ | Beschleunigung |
| $\frac{d\vec{v}}{dt}$ | Änderung der Geschwindigkeit mit der Zeit |
| $\frac{d^2\vec{x}}{dt^2}$ | Zweite Ableitung der Position |

Für den allgemeinen Fall (Körper $i$ im Drei-Körper-Problem) schreibt man kompakt:

$$\boxed{\sum \vec{F}_{ij} = m_i \frac{d^2\vec{x}_i}{dt^2}}$$

> [!IMPORTANT]
> Das ist die Gleichung, die numerisch gelöst werden muss. Sie beschreibt, wie sich die Position von Körper $i$ im Laufe der Zeit verändert — abhängig von Position und Masse der anderen Körper.

---

### 3.3 Erweiterung auf drei Körper

<img width="1923" height="914" alt="Image (2)" src="https://github.com/user-attachments/assets/a9c792e4-ee06-41af-8239-5fa0ec1641a9" />

Ein Planet wird als Massenpunkt mit Position $\vec{x} = [x, y, z]$ dargestellt. Wendet man Newtons zweites Gesetz auf jeden Planeten einzeln an, ergibt sich für **Planet 1** ($\vec{x}_1$):

$$m_1 \frac{d^2\vec{x}_1}{dt^2} = G \left( \frac{m_3 \, m_1}{|\vec{x}_3 - \vec{x}_1|^3}(\vec{x}_3 - \vec{x}_1) + \frac{m_2 \, m_1}{|\vec{x}_2 - \vec{x}_1|^3}(\vec{x}_2 - \vec{x}_1) \right)$$

Nach dem Kürzen von $m_1$:

$$\frac{d^2\vec{x}_1}{dt^2} = Gm_3 \frac{\vec{x}_3 - \vec{x}_1}{|\vec{x}_3 - \vec{x}_1|^3} + Gm_2 \frac{\vec{x}_2 - \vec{x}_1}{|\vec{x}_2 - \vec{x}_1|^3}$$

Wiederholt man dies für alle drei Planeten, erhält man das vollständige Differentialgleichungssystem (ODE-System):

```math
\begin{aligned}
    \frac{d^2\vec{x}_1}{dt^2} &= Gm_3 \frac{\vec{x}_3 - \vec{x}_1}{|\vec{x}_3 - \vec{x}_1|^3}
                               + Gm_2 \frac{\vec{x}_2 - \vec{x}_1}{|\vec{x}_2 - \vec{x}_1|^3} \\[20pt]
    \frac{d^2\vec{x}_2}{dt^2} &= Gm_3 \frac{\vec{x}_3 - \vec{x}_2}{|\vec{x}_3 - \vec{x}_2|^3}
                               + Gm_1 \frac{\vec{x}_1 - \vec{x}_2}{|\vec{x}_1 - \vec{x}_2|^3} \\[20pt]
    \frac{d^2\vec{x}_3}{dt^2} &= Gm_1 \frac{\vec{x}_1 - \vec{x}_3}{|\vec{x}_1 - \vec{x}_3|^3}
                               + Gm_2 \frac{\vec{x}_2 - \vec{x}_3}{|\vec{x}_2 - \vec{x}_3|^3}
\end{aligned}
```

> [!WARNING]
> Dieses Gleichungssystem besitzt keine analytische Lösung. Es muss numerisch gelöst werden.

---

## 4. Skalierung für Python

<img width="1608" height="862" alt="Image (1)" src="https://github.com/user-attachments/assets/e44dabfe-76e0-4163-93e5-adf211721a2a" />


Um die numerische Berechnung stabiler zu machen, werden alle Größen dimensionslos umskaliert. Dazu definiert man Referenzgrößen $M$ (Masse), $L$ (Länge) und $T$ (Zeit) und drückt alle Variablen relativ zu diesen aus.

---

### 4.1 Masse $m'$

$$\boxed{m' = \frac{m}{M}}$$

$M$ ist die Referenzmasse.

**Beispiel:** Wählt man $M = m_\oplus = 5{,}972 \times 10^{24}\,\text{kg}$ (Erdmasse), so gilt:

$$m'_e = \frac{m_e}{M} = 1 \qquad m'_s = \frac{m_s}{M} \approx 330\,000$$

---

### 4.2 Position $\vec{x}\,'$

$$\boxed{\vec{x}\,' = \frac{\vec{x}}{L}}$$

$L$ ist die Referenzlänge (z. B. 1 AE = astronomische Einheit).

---

### 4.3 Zeit $t'$

Die Referenzzeit $T$ wird so gewählt, dass sie dimensionslos Logisch mit $G$, $M$ und $L$ ist:

**Herleitung:**

$$[G] = \frac{\text{m}^3}{\text{kg} \cdot \text{s}^2}
\quad\Rightarrow\quad
[s^2] = \frac{[\text{m}^3]}{[\text{kg}] \cdot G}
\quad\Rightarrow\quad
T^2 = \frac{L^3}{M \cdot G}
\quad\Rightarrow\quad
T = \sqrt{\frac{L^3}{M \cdot G}}$$

Damit ergibt sich:

$$\boxed{t' = \frac{t}{T} = t \cdot \sqrt{\frac{M \cdot G}{L^3}}}$$

**Dimensionsprobe:**

$$\left[\frac{t}{T}\right] = \frac{[\text{s}]}{\sqrt{\dfrac{\text{m}^3}{\text{kg} \cdot \frac{\text{m}^3}{\text{kg} \cdot \text{s}^2}}}} = \frac{[\text{s}]}{[\text{s}]} = 1 \checkmark$$

---

## 5. Umskalierung der Gleichungen

### 5.1 Einsetzen der skalierten Variablen

Setzt man die skalierten Variablen

$$\vec{x}\,' = \frac{\vec{x}}{L}, \qquad m' = \frac{m}{M}, \qquad t' = t\sqrt{\frac{GM}{L^3}}$$

in die Bewegungsgleichung ein, erhält man zunächst:

$$\frac{d^2(L\vec{x}\,'_1)}{d\\left(\sqrt{\frac{L^3}{GM}}\,t'\right)^2} = Gm_3 \frac{L(\vec{x}\,'_3 - \vec{x}\,'_1)}{|L(\vec{x}\,'_3 - \vec{x}\,'_1)|^3} + Gm_2 \frac{L(\vec{x}\,'_2 - \vec{x}\,'_1)}{|L(\vec{x}\,'_2 - \vec{x}\,'_1)|^3}$$

Nach dem Vereinfachen und Kürzen ergibt sich die skalierte Bewegungsgleichung:

$$\boxed{\frac{d^2\vec{x}\,'_1}{dt'^2} = m'_3 \frac{\vec{x}\,'_3 - \vec{x}\,'_1}{|\vec{x}\,'_3 - \vec{x}\,'_1|^3} + m'_2 \frac{\vec{x}\,'_2 - \vec{x}\,'_1}{|\vec{x}\,'_2 - \vec{x}\,'_1|^3}}$$

Das vollständige skalierte ODE-System für alle drei Körper lautet:

```math
\begin{aligned}
    \frac{d^2\vec{x}\,'_1}{dt'^2} &= m'_3 \frac{\vec{x}\,'_3 - \vec{x}\,'_1}{|\vec{x}\,'_3 - \vec{x}\,'_1|^3}
                                   + m'_2 \frac{\vec{x}\,'_2 - \vec{x}\,'_1}{|\vec{x}\,'_2 - \vec{x}\,'_1|^3} \\[8pt]
    \frac{d^2\vec{x}\,'_2}{dt'^2} &= m'_3 \frac{\vec{x}\,'_3 - \vec{x}\,'_2}{|\vec{x}\,'_3 - \vec{x}\,'_2|^3}
                                   + m'_1 \frac{\vec{x}\,'_1 - \vec{x}\,'_2}{|\vec{x}\,'_1 - \vec{x}\,'_2|^3} \\[8pt]
    \frac{d^2\vec{x}\,'_3}{dt'^2} &= m'_1 \frac{\vec{x}\,'_1 - \vec{x}\,'_3}{|\vec{x}\,'_1 - \vec{x}\,'_3|^3}
                                   + m'_2 \frac{\vec{x}\,'_2 - \vec{x}\,'_3}{|\vec{x}\,'_2 - \vec{x}\,'_3|^3}
\end{aligned}
```

---

### 5.2 Umwandlung in ein System erster Ordnung

> [!IMPORTANT]
> Das Programm kann nur Differentialgleichungen erster Ordnung (nur $\frac{d}{dt}$, kein $\frac{d^2}{dt^2}$) direkt lösen. Deshalb führt man Hilfsfunktionen für die Geschwindigkeiten ein.

Man definiert die Geschwindigkeiten als neue Variablen:

$$\vec{f}_1 = \frac{d\vec{x}\,'_1}{dt'}, \qquad \vec{f}_2 = \frac{d\vec{x}\,'_2}{dt'}, \qquad \vec{f}_3 = \frac{d\vec{x}\,'_3}{dt'}$$

Damit erhält man das vollständige System erster Ordnung:

```math
\boxed{
\begin{aligned}
    \frac{d\vec{x}\,'_1}{dt'} &= \vec{f}_1 \\[6pt]
    \frac{d\vec{x}\,'_2}{dt'} &= \vec{f}_2 \\[6pt]
    \frac{d\vec{x}\,'_3}{dt'} &= \vec{f}_3 \\[10pt]
    \frac{d\vec{f}_1}{dt'} &= m'_3 \frac{\vec{x}\,'_3 - \vec{x}\,'_1}{|\vec{x}\,'_3 - \vec{x}\,'_1|^3}
                            + m'_2 \frac{\vec{x}\,'_2 - \vec{x}\,'_1}{|\vec{x}\,'_2 - \vec{x}\,'_1|^3} \\[6pt]
    \frac{d\vec{f}_2}{dt'} &= m'_3 \frac{\vec{x}\,'_3 - \vec{x}\,'_2}{|\vec{x}\,'_3 - \vec{x}\,'_2|^3}
                            + m'_1 \frac{\vec{x}\,'_1 - \vec{x}\,'_2}{|\vec{x}\,'_1 - \vec{x}\,'_2|^3} \\[6pt]
    \frac{d\vec{f}_3}{dt'} &= m'_1 \frac{\vec{x}\,'_1 - \vec{x}\,'_3}{|\vec{x}\,'_1 - \vec{x}\,'_3|^3}
                            + m'_2 \frac{\vec{x}\,'_2 - \vec{x}\,'_3}{|\vec{x}\,'_2 - \vec{x}\,'_3|^3}
\end{aligned}
}
```

---

### 5.3 Anfangsbedingungen

Gesucht sind die Punkte $\vec{x}\,'_1(t')$, $\vec{x}\,'_2(t')$ und $\vec{x}\,'_3(t')$. Zum Zeitpunkt $t' = 0$ müssen folgende Anfangswerte bekannt sein:

$$
\begin{aligned}
\vec{x}\,'_{i,0} &= [x'_0,\, y'_0,\, z'_0] && \text{Anfangsposition von Körper } i \\
\vec{v}\,'_{i,0} &= [v'_{x_0},\, v'_{y_0},\, v'_{z_0}] && \text{Anfangsgeschwindigkeit von Körper } i
\end{aligned}
$$

für $i = 1, 2, 3$. (Körper)
---

