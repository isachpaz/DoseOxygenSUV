from dosemodificationfactor import DoseModificationFactor
from oxygenmodificationfactor import OxygenModificationFactor
import numpy as np
import matplotlib.pyplot as plt


def plot_omf():
    omf = OxygenModificationFactor(max_oer=3.0, k_mmHg=2.5)
    po2line = np.linspace(start=0.0, stop=20.0, num=400)
    plt.plot(po2line, omf.calculate(po2line))
    plt.show()


def plot_dmf():
    dmf = DoseModificationFactor(max_oer=3.0, k_mmHg=2.5)
    po2line = np.linspace(start=0.0, stop=10.0, num=400)
    plt.plot(po2line, dmf.calculate(po2line), linewidth=2)
    plt.xlabel("$pO_2$ (mmHg)", fontsize=16)
    plt.ylabel("Dose modification factor", fontsize=16)

    plt.tick_params(labelsize=14)

    # Show the major grid lines with dark grey lines
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.savefig('dmf.png', dpi=600, bbox_inches='tight')
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # plot_omf()
    plot_dmf()
