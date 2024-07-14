import numpy as np
from scipy.optimize import curve_fit


def get_coefficients(t: np.array, y: np.array) -> np.ndarray[np.float64]:
    """"""
    popt, _ = curve_fit(
        f=_func,
        xdata=t,
        ydata=y,
        p0=(2, 0, 2, 0, 2, 0),
    )
    return popt


def _func(t, c_1, a_1, c_2, a_2, c_3, a_3):
    """Моедлируемая функция - сумма трех экспонент.
    """
    return (
        np.multiply(c_1, np.exp(a_1*t)) +
        np.multiply(c_2, np.exp(a_2*t)) +
        np.multiply(c_3, np.exp(a_3*t))
    )
