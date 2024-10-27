import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import pygame
import sys

d = 10

xs, ys, zs = [], [], []
x_inc, y_inc, z_inc = 0, 0, 0

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
fig.suptitle('Coordenadas', fontsize=10)

pygame.init()
pygame.joystick.init()

j = pygame.joystick.Joystick(0)
j.init()

def update_coordinates():
    global x_inc, y_inc, z_inc
    
    if round(j.get_axis(3), 1) == 1:
        z_inc -= 1
    if round(j.get_axis(3), 1) == -1:
        z_inc += 1
    if round(j.get_axis(0), 1) == 1:
        x_inc += 1
    if round(j.get_axis(0), 1) == -1:
        x_inc -= 1
    if round(j.get_axis(1), 1) == 1:
        y_inc -= 1
    if round(j.get_axis(1), 1) == -1:
        y_inc += 1
    

def p(frame):
    global x_inc, y_inc, z_inc
    x, y, z = 5 + x_inc, 5 + y_inc, 5 + z_inc

    xs.append(x), ys.append(y), zs.append(z)

    ax.cla()

    ax.scatter(xs, ys, zs, color='black', s=1)
    ax.plot(xs, ys, zs, color='red', linewidth=0.5, alpha=0.5)

    ax.set_xlim(min(xs), max(xs)), ax.set_ylim(min(ys), max(ys)), ax.set_zlim(min(zs), max(zs))

    ax.set_xlabel("X", fontsize=12), ax.set_ylabel("Y", fontsize=12), ax.set_zlabel("Z", fontsize=12)
    ax.set_xlim(0, d), ax.set_ylim(0, d), ax.set_zlim(0, d)

animation = FuncAnimation(fig, p, interval=1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    update_coordinates()
    
    plt.pause(.001)
