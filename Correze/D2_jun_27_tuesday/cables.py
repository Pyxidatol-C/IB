# %% Experimental
import matplotlib.pyplot as plt
import numpy as np

height = 15.0
xs = np.sqrt(np.arange(11) ** 2 + height ** 2)
mag = [0.0499197812503,
       0.0452709950819,
       0.0391668841284,
       0.0465973932039,
       0.050467915221,
       0.0631260108794,
       0.0561816989157,
       0.0511809844696,
       0.0459644139879,
       0.0487916814552,
       0.0492391733468, ]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x_err = 1 / 2 * ((2 * 0.005 * xs) / (xs ** 2 + height ** 2)) * xs
plt.errorbar(xs, mag, linestyle='-', yerr=0.001, xerr=x_err, capsize=2)
plt.plot(xs, mag, 'x')
plt.xlabel("Distance from cable (m)")
plt.ylabel("Magnetic field strength (µT)")
plt.title("Magnetic flux density with varying distance from cable")

ax.set_xticks(np.arange(15, 18.1, 0.5))
ax.set_xticks(np.arange(15, 18.1, 0.1), minor=True)
ax.set_yticks(np.arange(0.035, 0.065, 0.005))
ax.set_yticks(np.arange(0.035, 0.065, 0.001), minor=True)

ax.grid(which='both')

plt.show()

# %% Theoretical

xs = np.linspace(1, 20, 100)
mag = 1 / xs

plt.plot(xs, mag, '-')
plt.xlabel("Distance from cable (m)")
plt.ylabel("Magnetic field strength (µT)")
plt.yticks([])
plt.title("Theoretical magnetic flux density with varying distance from cable")

plt.show()
