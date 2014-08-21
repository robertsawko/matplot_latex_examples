from aux import *


Re_gas = [150, 1500]
Re_liquid = [150, 1500]

# Note that I am using formatting strings
# See this
# https://docs.python.org/2/library/string.html#string-formatting

file_name_analytic = "./analytic/ReG{0:0>4d}ReL{1:0>4d}.csv"
file_name_numerical = "./numerical/ReG{0:0>4d}ReL{1:0>4d}.csv"
file_name_graph = "./ReG{0:0>4d}ReL{1:0>4d}.pgf"

for Re_g in Re_gas:
    for Re_l in Re_liquid:
        analytic = np.genfromtxt(file_name_analytic.format(Re_g, Re_l))
        numerical = np.genfromtxt(file_name_numerical.format(Re_g, Re_l))
        set_plt_params(0.49, False, rescale_h=0.8)
        fig = plt.figure()
        ax = fig.gca()
        plt.ylabel('Dimensionless height $x_2/H$')
        plt.xlabel(r'Dimensionless velocity $u_1/U_\textrm{sg}')

        ax.plot(analytic[:, 1], analytic[:, 0])
        ax.plot(
            numerical[:, 1], numerical[:, 0], linestyle='None',
            marker='s', markevery=1, markersize=3, alpha=0.5)

        fig.suptitle(
            "$Re_l={0} \quad Re_g={1}$".format(Re_g, Re_l))

        fig.savefig(
            file_name_graph.format(Re_g, Re_l),
            transparent=True, bbox_inches='tight', pad_inches=0)

# In order to get a legend separately we draw a dummy figure
dummyfig = plt.figure()
ax = dummyfig.gca()
# The lines must be created with the same properties
l1, = ax.plot(range(10))
l2, = ax.plot(range(10), linestyle='None', marker='s', alpha=0.5)
# Unfortunately you need to adjust the numbers below manually
legendfig = plt.figure(figsize=(3.9, 0.1))
l = legendfig.legend([l1, l2], ["Analytical solution", "CFD solution"], ncol=2)
l.get_frame().set_facecolor('none')
# Save - note that we don't use tight layout
legendfig.savefig("legend.pgf", transparent=True, pad_inches=0)
