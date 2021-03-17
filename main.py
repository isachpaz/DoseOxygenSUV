from dosemodificationfactor import DoseModificationFactor
from oxygenmodificationfactor import OxygenModificationFactor
import numpy as np
import matplotlib.pyplot as plt
from PO2 import PO2


def plot_omf():
    omf = OxygenModificationFactor(max_oer=3.0, k_mmHg=2.5)
    po2line = np.linspace(start=0.0, stop=20.0, num=400)
    plt.plot(po2line, omf.calculate(po2line))
    plt.show()


def plot_po2():
    a = 10.9
    b = 10.7
    c = 2.5
    po2func = PO2(a, b, c)
    minUptake = po2func.calculate_uptake_from_po2(60)
    maxUptake = po2func.calculate_uptake_from_po2(0.0)
    print(f"Uptake_min = {po2func.calculate_uptake_from_po2(60)} for 60 mmHg")
    print(f"Uptake_max = {po2func.calculate_uptake_from_po2(0.0)} for 0 mmHg")
    # print(f"pO2 = {po2func.calculate_from_uptake(40)} for 400 Uptake")
    # uptakes = np.linspace(start=minUptake, stop=20, num=40000)
    uptakes = np.linspace(start=0.3, stop=maxUptake, num=40000)
    spo2s = po2func.calculate_from_uptake(uptakes)
    plt.plot(uptakes, spo2s)
    # plt.yscale('log')
    plt.ylim(-1, 160)
    plt.xlim(0.1, maxUptake + 0.5)
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.tick_params(labelsize=14)
    # plt.yticks(np.arange(0, 13 + 1, 1.0))
    plt.ylabel("$pO_2$ (mmHg)", fontsize=16)
    plt.xlabel("Uptake (normalized to 60mmHg)", fontsize=16)

    po2Points = [0, 0.76, 3.8, 38, 152]
    uptakePoints = [10.9, 7.7, 5.6, 1, 0.5]

    plt.scatter(uptakePoints, po2Points)
    plt.show()


def plot_uptake():
    A = 10.9
    B = 10.7
    C = 2.5
    po2func = PO2(A, B, C)
    print(f"Uptake = {po2func.calculate_uptake_from_po2(60)} for 60 mmHg")
    spo2s = np.linspace(start=0, stop=1000, num=400000)
    uptakes = po2func.calculate_uptake_from_po2(spo2s)
    plt.plot(spo2s, uptakes)
    plt.xscale('log')
    plt.ylim(0, 13, 1)
    # plt.xlim(0, 2000)
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.tick_params(labelsize=14)
    plt.yticks(np.arange(0, 13 + 1, 1.0))
    plt.xlabel("$pO_2$ (mmHg)", fontsize=16)
    plt.ylabel("Tracer uptake", fontsize=16)
    po2Points = [0.0076, 0.76, 3.8, 38, 152]
    uptakePoints = [10.9, 7.7, 5.6, 1, 0.5]
    plt.scatter(po2Points, uptakePoints)
    plt.show()


def plot_normalized_uptake():
    A = 10.9
    B = 10.7
    C = 2.5
    po2func = PO2(A, B, C)
    print(f"Uptake = {po2func.calculate_uptake_from_po2(60)} for 60 mmHg")
    spo2s = np.linspace(start=.1, stop=60, num=4000)
    uptakes = po2func.calculate_normalized_uptake_from_po2(spo2s)
    plt.plot(spo2s, uptakes)
    #plt.xscale('log')
    plt.ylim(0, 20, 1)
    # plt.xlim(0, 2000)
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.tick_params(labelsize=14)
    plt.yticks(np.arange(0, 20 + 1, 1.0))
    plt.xlabel("$pO_2$ (mmHg)", fontsize=16)
    plt.ylabel("Uptake (normalized to 60mmHg)", fontsize=16)

    po2Points = [0.0, 0.76, 3.8, 38, 152]
    uptakePoints = [10.9, 7.7, 5.6, 1, 0.5]

    #plt.scatter(po2Points, uptakePoints)

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
    # plot_dmf()
    #plot_po2()
    plot_uptake()
    #plot_normalized_uptake()
