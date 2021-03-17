import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd


def fmiso(uptake, A, B, C):
    return C * (A - uptake) / (B - A + uptake)


def calculate_uptake_from_po2(po2, A, B, C):
    # C=2.5
    #C = 2.46
    return A - (B * po2 / (C + po2))


def calculate_normalized_uptake_from_po2(po2, A, B, C):
    f = calculate_uptake_from_po2(60, A, B, C)
    return A / f - (B / f * po2 / (C + po2))


def main():
    # po2Points = [0.0076, 0.76, 3.8, 38, 152]
    po2Points = [0.0076, 0.76, 3.8, 38, 152]
    uptakePoints = [10.9, 7.7, 5.6, 1, 0.5]
    sigma = [0.3, 1.0, 1.0, 0.001, 1]

    xdata = np.asarray(po2Points)
    ydata = np.asarray(uptakePoints)
    plt.plot(xdata, ydata, 'o')
    plt.grid()
    plt.show()

    print('----------------------------------------------------------')
    parameters, covariance = curve_fit(f=calculate_uptake_from_po2,
                                       xdata=xdata,
                                       ydata=ydata,
                                       sigma=sigma)
    print(parameters)
    print(covariance)

    # Get the standard deviations of the parameters (square roots of the # diagonal of the covariance)
    stdevs = np.sqrt(np.diag(covariance))  # Calculate the residuals
    print(f"Std deviation= {stdevs}")
    res = ydata - calculate_uptake_from_po2(xdata, *parameters)
    print(f"Residuals: {res}")
    plt.scatter(xdata, res)
    plt.show()

    xline = np.arange(start=0, stop=150, step=0.01)
    fit_y = calculate_uptake_from_po2(xline, *parameters)
    fit_y_previous = calculate_uptake_from_po2(xline, A=10.9, B=10.7, C=2.5)

    plt.plot(xline, fit_y, '-', label='fit')
    plt.plot(xline, fit_y_previous, '-', label='previously-fitted')
    plt.plot(xdata, ydata, 'o', label='data')
    plt.legend()
    plt.xscale('log')
    plt.grid()
    plt.show()


def plot1():
    A = 10.9
    B = 10.7
    C = 2.5
    xline = np.arange(start=0.1, stop=1000, step=0.001)
    fit_y = calculate_normalized_uptake_from_po2(xline, A, B, C)

    plt.plot(xline, fit_y, '-')
    plt.xscale('log')
    plt.ylim(0, 17, 1)
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()

    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.tick_params(labelsize=14)

    plt.yticks(np.arange(0, 17 + 1, 1.0))

    plt.xlabel("$pO_2$ (mmHg)", fontsize=16)
    plt.ylabel(f"Tracer uptake\n(normalized to 60 mmHg)", fontsize=16)
    plt.show()


# Press the green button in the gutter to run the script.
def fit_dasu_data():
    df = pd.read_csv('FMISO_Dasu_UptakePlot.csv')
    print(df.head())
    po2 = np.array(df['po2'])
    uptake = np.array(df['normalizedUptake']) * 0.628
    print('----------------------------------------------------------')
    parameters, covariance = curve_fit(calculate_uptake_from_po2, po2, uptake)
    print(parameters)
    print(covariance)

    # Get the standard deviations of the parameters (square roots of the # diagonal of the covariance)
    stdevs = np.sqrt(np.diag(covariance))  # Calculate the residuals
    print(f"Std deviation= {stdevs}")


if __name__ == '__main__':
    main()
    # fit_dasu_data()
    # plot1()
