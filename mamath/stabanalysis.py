import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize, vectorize

def plot_stability(f):
    fig, ax = plt.subplots()

    x = np.linspace(0.96,1.30,20)
    y = np.linspace(200,320,20)

    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(y[0], y[-1])

    partplot_quiver(ax, f, x, y)
    partplot_root(ax, f, x, y, 'm-')
    ax.grid()

    return fig

def plot_comparison(models):
    fig, ax = plt.subplots()

    x = np.linspace(0.96,1.30,20)
    y = np.linspace(200,320,20)

    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(y[0], y[-1])

    for model in models:
        f = model.get_f_with_Qfactor()
        partplot_root(ax, f, x, y, label=model.name)

    ax.legend(loc='best')

    return fig

def partplot_quiver(ax, f, x, y):
    X1 , Y1  = np.meshgrid(x, y)
    DX1 = 0*X1
    DY1 = f(Y1, X1)
    M = np.hypot(DX1, DY1)

    ax.quiver(X1, Y1, DX1, DY1, M, pivot='mid')

def partplot_root(ax, f, x, y, *plot_args, **plot_kwargs):
    yy = np.linspace(y[0], y[-1], 400)
    xx = vectorize(lambda T: nan_on_error(lambda: optimize.brentq(lambda Qf: f(T, Qf), x[0], x[-1])))(yy)
    ax.plot(xx, yy, *plot_args, **plot_kwargs)

def nan_on_error(calculation):
    try:
        result = calculation()
        return result
    except ValueError:
        return np.nan
    except RuntimeError:
        return np.nan
