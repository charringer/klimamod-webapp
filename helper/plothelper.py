from io import StringIO
import matplotlib.pyplot as plt

def svg_plot(fig):
    f = StringIO()
    plt.savefig(f, format="svg")
    f.seek(0)
    header = ""
    for i in range(4):
        header += f.readline()
    return (header, f.read())

def headerless_svg(svg):
    return svg[1]

def downloadable_svg(svg):
    return svg[0]+svg[1]
