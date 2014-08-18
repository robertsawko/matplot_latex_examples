import numpy as np
import matplotlib as mpl
# Define a backend
# MUST be invoked before pyplot import
mpl.use("pgf")
import matplotlib.pyplot as plt

# For R-style plotting
from mpltools import style
style.use('ggplot')


def set_plt_params(relative_fig_width=1.0, landscape=True, page_width=345.0):
    fig_width_pt = page_width * relative_fig_width
    inches_per_pt = 1.0 / 72.27               # Convert pt to inch
    golden_mean = (np.sqrt(5.0) - 1.0) / 2.0  # Aesthetic ratio
    fig_width = fig_width_pt * inches_per_pt  # width in inches

    if landscape:
        fig_height = fig_width * golden_mean  # height in inches
    else:
        fig_height = fig_width / golden_mean  # height in inches

    fig_size = [fig_width, fig_height]
    params = {
        'font.family': 'serif',
        'axes.labelsize': 9,
        'text.fontsize': 7,
        'legend.fontsize': 9,
        'lines.markersize': 3,
        'xtick.labelsize': 7,
        'ytick.labelsize': 7,
        'text.usetex': True,
        'figure.figsize': fig_size,
        'pgf.texsystem': "xelatex",
        'pgf.rcfonts': False,
        'pgf.preamble': [
            r"\usepackage{fontspec}",
            r"\defaultfontfeatures{Scale=MatchLowercase,Mapping=tex-text}",
            r"\setmainfont{Liberation Serif}",
        ]
    }

    plt.rcParams.update(params)

plt.ioff()
