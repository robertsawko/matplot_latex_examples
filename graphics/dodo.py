from header import *
import glob
import matplotlib.ticker

def task_alpha():
  def plot_fig(caseid='80',draw_legend=False):
    #Load data
    kEps = np.loadtxt("kEps-c%s.csv" % caseid, float,delimiter=',', skiprows=1)
    LRR = np.loadtxt("LRR-c%s.csv" % caseid, float,delimiter=',', skiprows=1)
    ngan = np.loadtxt("exp%s.dat" % caseid, float)

    set_plt_params(0.29,False)
    fig = plt.figure()
    ax = fig.gca();

    plt.ylim((0, 1.05))  
    plt.xlim((-0.05, 1.05))  
    plt.ylabel('Dimensionless height $x_2/H$')  
    plt.xlabel('Water fraction $\\alpha_{w}$')
    fig.suptitle("Inlet {0}% water-cut".format(caseid), fontsize=7)

    lines = []
    line, = ax.plot(1 - ngan[:, 0], ngan[:, 1], linestyle='None',marker='s',markersize=4)
    lines.append(line)

    line, = ax.plot(1 - kEps[:, 10], kEps[:, 20] / 0.019 / 2 + 0.5,marker='v', markevery=5)
    lines.append(line)

    line, = ax.plot(1 - LRR[:, 16], LRR[:, 26] / 0.019 / 2 + 0.5,marker='+', markevery=5)
    lines.append(line)

    fig.savefig("c%s.pgf" % caseid,
        transparent=True, bbox_inches='tight', pad_inches=0)

    if draw_legend == True:
      figlegend = plt.figure(figsize=(3.1,0.29))
      #figlegend = plt.figure()
      lgnd=figlegend.legend(lines, (["Ngan (2010)", "$k$-$\\epsilon$ model", "LRR"]), ncol=3)
      lgnd.get_frame().set_facecolor('none')
      figlegend.savefig("legend.pgf", transparent=True, pad_inches=0)

  def plot_all_figs() : 
    plot_fig(draw_legend=True)

    remainings_figs_id = ['60','40']
    for fig_id in remainings_figs_id : 
      plot_fig(fig_id)

    plt.close("all")

  return {
      'actions': [plot_all_figs],
      'file_dep': ( ["dodo.py", "header.py"] ),
      'targets': ["alpha-80.pdf"],
  }

