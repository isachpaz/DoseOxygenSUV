import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
from scipy.stats.distributions import t

# Import PySwarms
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx


def exp_func(x, a, b, c):
    return c + a * np.exp(b * x)


def main():
    # df = pd.read_csv('Dataset_piert_2000_line_fit.csv')
    df = pd.read_csv('Dataset_piert_2000_points.csv')

    print(df.head())

    po2 = np.array(df['po2'])  # x-axis
    uptake = np.array(df['suv'])  # y-axis
    # po2 = np.array(df['po2'])
    # uptake = np.array(df['suv'])
    print('----------------------------------------------------------')

    bounds = (-100, 100)
    parameters, covariance = curve_fit(exp_func, po2, uptake,
                                       bounds=bounds,
                                       maxfev=10000)
    print(parameters)
    print(covariance)

    estimated_values = exp_func(po2, *parameters)
    correlation_matrix = np.corrcoef(estimated_values, uptake)
    correlation_xy = correlation_matrix[0, 1]

    r_squared = correlation_xy ** 2

    print(f"r_squared = {r_squared:.2f}")

    # Get the standard deviations of the parameters (square roots of the # diagonal of the covariance)
    stdevs = np.sqrt(np.diag(covariance))  # Calculate the residuals
    print(f"Std deviation= {stdevs}")

    alpha = 0.05  # 95% confidence interval

    n = len(uptake)  # number of data points
    p = len(parameters)  # number of parameters

    dof = max(0, n - p)  # number of degrees of freedom

    tval = t.ppf(1.0 - alpha / 2.0, dof)  # student-t value for the dof and confidence level

    for i, p, var in zip(range(n), parameters, np.diag(covariance)):
        sigma = var ** 0.5
        print('c{0}: {1} [{2}  {3}]'.format(i, p,
                                      p - sigma * tval,
                                      p + sigma * tval))

    xline = (np.arange(start=1, stop=40, step=0.01))
    fit_y = exp_func(xline, *parameters)

    plt.plot(xline, fit_y, '-', label='fit')
    plt.scatter(po2, uptake, label='data points')
    plt.legend()

    plt.xlabel("$tPO_2$ (mmHg)", fontsize=16)
    plt.ylabel(f"FMISO SUV", fontsize=16)

    # plt.xscale('log')
    # plt.yscale('log')

    # plt.ylim(0, 17, 1)

    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    # plt.minorticks_on()

    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    # plt.tick_params(labelsize=14)
    # plt.yticks(np.arange(1, 10, 10))

    plt.show()


if __name__ == '__main__':
    main()
