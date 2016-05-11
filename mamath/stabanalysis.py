import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize, vectorize

def sys(f, x):
    return np.array([ f(x[0], x[1]), 0 * x[1] ])

def plot_stability(f):
    fig, ax = plt.subplots()

    x = np.linspace(0.96,1.30,20)
    y = np.linspace(200,320,20)

    partplot_quiver(ax, f, x, y)
    partplot_root(ax, f, x, y, 'g-')
    ax.grid()

    return fig

def plot_comparison(functions):
    fig, ax = plt.subplots()

    x = np.linspace(0.96,1.30,20)
    y = np.linspace(200,320,20)

    styles = ['g-', 'b-', 'm-', 'r-', 'y-']
    for (f, label), style in zip(functions, styles):
        partplot_root(ax, f, x, y, 'g-', label=label)

    return fig

def partplot_quiver(ax, f, x, y):
    X1 , Y1  = np.meshgrid(x, y)
    DX1 = 0*X1
    DY1 = f(Y1, X1)
    M = np.hypot(DX1, DY1)

    ax.quiver(X1, Y1, DX1, DY1, M, pivot='mid')

def partplot_root(ax, f, x, y, *plot_args, **plot_kwargs):
    root_y_begin = max(y[ 0], optimize.newton(lambda T: f(T, x[ 0]), 100) + 1E-9)
    root_y_end   = min(y[-1], optimize.newton(lambda T: f(T, x[-1]), 100) - 1E-9)
    root_y = np.linspace(root_y_begin, root_y_end, 800) 
    root_x = vectorize(lambda T: optimize.brentq(lambda Qf: f(T, Qf), x[0], x[-1]))(root_y)

    ax.plot(root_x, root_y, *plot_args, **plot_kwargs)
