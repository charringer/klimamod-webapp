import numpy as np
import matplotlib.pyplot as plt

def euler(f, x0, h, time):
    steps = [x0]
    x = x0
    for i in range(time):
        x = x + h * f(x)
        steps.append(x)
    return steps

def plot_euler(f, iv, time):
    fig, ax = plt.subplots()

    numsteps = 5*24*60*60
    numstepspertime = 365//5

    x = np.linspace(0, time, time*numstepspertime+1)
    y = euler(f, iv, numsteps, time*numstepspertime)
    ax.plot(x, y, 'r-')

    ax.set_ylim(200,320)
    ax.set_title("dynamics in time")
    ax.set_xlabel("time / 1 year")
    ax.set_ylabel("temperature / 1 K")
    ax.grid()
    return fig
