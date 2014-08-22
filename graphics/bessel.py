from aux import *
from scipy.special import jn

set_plt_params()

x = np.arange(0.0, 20.0 + 0.01, 0.01)
jn0 = jn(0, x)
jn1 = jn(1, x)
jn2 = jn(2, x)

l1, = plt.plot(x, jn0)
l2, = plt.plot(x, jn1)
l3, = plt.plot(x, jn2)

plt.ylabel('ordinate')
plt.xlabel('abscissa')
plt.suptitle(
    r"$J_\alpha(x) = \sum_{m=0}^\infty\frac{(-1)^m}{m!\Gamma(m+\alpha+1)}"
    + r"\left(\frac{x}{2}\right)^{2m+\alpha}$")
plt.subplots_adjust(top=0.8)

legend = plt.legend(
    [l1, l2, l3], ["$J_{0}(x)$", "$J_{1}(x)$", "$J_{2}(x)$"],
    loc='upper right')

# Take out the colour from the legend
legend.get_frame().set_facecolor('none')

plt.savefig('bessel.pgf', transparent=True, bbox_inches='tight')
