from io import StringIO
import matplotlib.pyplot as plt

def svg_plot(fig):
    f = StringIO()
    plt.savefig(f, format="svg")
    f.seek(0)
    for i in range(4):
        f.readline()
    return f.read()
