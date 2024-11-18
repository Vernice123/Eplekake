import numpy as np
import matplotlib.pyplot as plt

def T(t):
    return 23.3 + 73.3*np.e**(-2.568e-2*t)
    
x_verdier = np.array([0, 5, 10, 15, 20, 25, 30, 35, 45, 55, 65, 75, 85, 95, 115, 135, 200])
y_verdier1 = np.array([96.9, 91.1, 80.3, 74.4, 67.1, 60.1, 54.7, 51.0, 44.2, 39.0, 34.6, 32.5, 30.7, 27.9∑, 26.3, 24.8, 23.6])

t_verdier = np.linspace(0, 200, 40000)
y_verdier = T(t_verdier)

plt.plot(t_verdier, y_verdier, 'r-', label = 'T(t)')
plt.plot(x_verdier, y_verdier1, 'b-', label = 'Eksperimentelle verdier')
plt.title('Plot av temperaturen til den beste eplekaken over tid')
plt.xlabel('Tid(min)')
plt.legend()
plt.ylabel('Temperatur(C)')

plt.show() 