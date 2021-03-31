import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd


def linear_func(x, a, b):
    return a * x + b


def main():
    df = pd.read_csv('Dataset_fitted_line_piert_1999.csv')
    print(df.head())

    po2 = np.log(np.array(df['po2']))  # x-axis
    uptake = np.log(np.array(df['suv']))  # y-axis
    #po2 = np.array(df['po2'])
    #uptake = np.array(df['suv'])
    print('----------------------------------------------------------')
    parameters, covariance = curve_fit(linear_func, po2, uptake)
    print(parameters)
    print(covariance)

    # Get the standard deviations of the parameters (square roots of the # diagonal of the covariance)
    stdevs = np.sqrt(np.diag(covariance))  # Calculate the residuals
    print(f"Std deviation= {stdevs}")

    xline = (np.arange(start=1, stop=40, step=0.01))
    fit_y = linear_func(xline, *parameters)

    #plt.plot(xline, fit_y, '-', label='fit')
    plt.scatter(po2, uptake)
    plt.legend()
    #plt.xscale('log')
    #plt.yscale('log')

    # plt.ylim(0, 17, 1)

    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    # plt.minorticks_on()

    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    # plt.tick_params(labelsize=14)
    # plt.yticks(np.arange(1, 10, 10))

    plt.show()


if __name__ == '__main__':
    main()
