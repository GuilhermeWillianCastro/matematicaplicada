import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

d = float(np.format_float_scientific(np.float32(2.81e6), precision=1))
#print(d)

xs, ys, zs = [], [], []
ceil = 2160
def p(frame):
    
    x = d*np.cos(np.linspace(0, ceil, 360)[frame]*(np.pi/180))
    y = d*np.sin(np.linspace(0, ceil, 360)[frame]*(np.pi/180))
    z = np.linspace(0, 720, 360)[frame]
    #print(z)

    xs.append(x);ys.append(y);zs.append(z)

    ax.cla()

    ax.scatter(xs, ys, zs, color='black', s=1)
    ax.plot(xs, ys, zs, color='red', linewidth=0.5, alpha=0.5)

    ax.set_xlabel("X", fontsize=12);ax.set_ylabel("Y", fontsize=12);ax.set_zlabel("Z", fontsize=12)
    ax.set_xlim(-d, d);ax.set_ylim(-d, d);ax.set_zlim(0, 360)

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
fig.suptitle('heli', fontsize=10)

animation = FuncAnimation(fig, p, frames=ceil, interval=5)
plt.show()