# %%
import numpy as np
import matplotlib.pyplot as plt

delta_hs = [-12,
            -18,
            -10,
            -15,
            -9,
            -10,
            -12,
            -12,
            -12,
            -9,
            -10,
            -12,
            -13,
            -15,
            -12,
            -10,
            -11,
            -13,
            -10,
            -13,
            -11,
            -11,
            -12,
            -10,
            -10,
            -10,
            -11,
            -13,
            -9,
            -8,
            -18,
            -11,
            -9,
            -8,
            -8,
            -16,
            -10,
            -16,
            -15,
            -10,
            -15,
            -15,
            -12,
            -17,
            -8,
            -15,
            -9,
            -12,
            -10,
            -9,
            -8,
            -11,
            -8,
            -11,
            -11,
            -14,
            -10,
            -12,
            -8,
            -10,
            -8,
            -7,
            -10,
            -2,
            -7,
            -9,
            -3,
            -7,
            -8,
            0]
xs = np.concatenate(([0], np.arange(1, 69 + 1), [81.6]))

# %%
hs = [0]
for d_h in delta_hs:
    hs.append(hs[-1] + d_h)
hs = np.array(hs) / 100  # convert from cm to m

# %%
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.plot(xs, hs, '-x')

plt.xlabel("Distance away from starting point (m)")
plt.ylabel("Height relative to starting point (m)")
plt.title("Landscape of Field")

ax.set_xticks(np.arange(min(xs), max(xs) + 1, 5))
ax.set_xticks(np.arange(min(xs), max(xs) + 1, 1), minor=True)
ax.set_yticks(np.arange(min(hs), max(hs) + .1, .5))
ax.set_yticks(np.arange(min(hs), max(hs) + .1, .1), minor=True)
ax.grid(which='both')

plt.xlim([min(xs), max(xs)])
plt.ylim([min(hs), max(hs)])

plt.show()
