`2017-09-18 Monday`
# Mechanics
- Displacement ($m$): $x$ (initial displacement: $x_0$)
- Velocity ($m/s$): $v$ (initial velocity: $v_0$)
- Acceleration ($m/s^2$): $a$ 

## Graphs of motion
For constant acceleration with $v_0$ and $x_0$
![graphs of acceleration, velocity and displacement](graphs-motion.png)

```python
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 5)
a = t * 0 + 1
v = 1 + a * t
s = 1 + (v - 1) * t / 2

_, (a1, a2, a3) = plt.subplots(3, sharex=True)
for ax, y, y0_name, description in zip(
    (a1, a2, a3), 
    (a, v, s), 
    ('$a$', '$v_0$', '$x_0$'), 
    ('acceleration ($m/s^2$)', 'velocity ($m/s$)', 'displacement ($m$)')
):
    ax.plot(t, y)
    ax.grid(True, which='both')
    plt.xlabel('time ($s$)')
    ax.set_ylabel(description)
    plt.xticks(range(10))
    plt.xlim([0, 5])
    ax.set_ylim([0, max(y) + 1])
    ax.set_yticks([1])
    ax.set_yticklabels([y0_name])
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.get_yaxis().set_label_coords(-0.1,0.5)
plt.tight_layout()

```

- $v = \frac{\Delta x}{\Delta t}$ (change in displacement over time)
- $a = \frac{\Delta{v}}{\Delta{t}}$ (change in velocity over time)