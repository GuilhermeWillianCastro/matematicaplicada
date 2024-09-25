import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

d = 10

xs, ys, zs = [], [], []
x_inc, y_inc, z_inc = 0,0,0

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
fig.suptitle('coordenadas', fontsize=10)

def p(frame):
    global x_inc, y_inc, z_inc
    x, y, z = 5 + x_inc, 5 + y_inc, 5 + z_inc

    xs.append(x);ys.append(y);zs.append(z)

    ax.cla()

    ax.scatter(xs, ys, zs, color='black', s=1)
    ax.plot(xs, ys, zs, color='red', linewidth=0.5, alpha=0.5)

    ax.set_xlabel("X", fontsize=12);ax.set_ylabel("Y", fontsize=12);ax.set_zlabel("Z", fontsize=12)
    ax.set_xlim(0, d),ax.set_ylim(0, d),ax.set_zlim(0, d)
    #ax.view_init(elev=45, azim=-45)

def on_key(event):
    global x_inc, y_inc, z_inc
    if event.key == 'up': y_inc += 1
    if event.key == 'down': y_inc -= 1  
    if event.key == 'left': x_inc -= 1  
    if event.key == 'right': x_inc += 1  
    if event.key == 'a': z_inc += 1  
    if event.key == 'z': z_inc -= 1

fig.canvas.mpl_connect('key_press_event', on_key)

animation = FuncAnimation(fig, p, interval=1)
plt.show()