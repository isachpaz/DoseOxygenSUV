from scipy.optimize import curve_fit
import numpy as np


def uptake_func(po2, a, b, c):
    return a - ((b * po2) / (c + po2))


def fit():
    uptake = [10.91, 10.9, 7.7, 5.6, 1.0, 0.628, 0.5]
    po2 = [0.0, 0.0076, 0.76, 3.8, 38, 60, 152]
    #po2 = [0.0, 0.76, 3.8, 38, 152]

    pars, cov = curve_fit(f=uptake_func, xdata=po2, ydata=uptake,
                          p0=[10.9, 10.7, 2.5])
                          # sigma=[1, 1, 10, 10, 10, 10, 1])

    stdevs = np.sqrt(np.diag(cov))  # Calculate the residuals
    # res = y_dummy - power_law(x_dummy, *pars)
    print(pars)
    print(cov)


if __name__ == "__main__":
    # execute only if run as a script
    fit()
