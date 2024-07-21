import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import (
    mean_absolute_error,
    mean_absolute_percentage_error,
    mean_squared_error,
    median_absolute_error,
    r2_score,
)


def get_coefficients(t: np.array, y: np.array) -> np.ndarray[np.float64]:
    """Выполняет оптимизацию целевой функции к заданным значениям.

    Args:
        t: Массив значений времени.
        y: Массив значений ряда.

    Returns:
        Массив коэффициентов целевой функции.
    """
    popt, _ = curve_fit(
        f=func,
        xdata=t,
        ydata=y,
        p0=(2, 0, 2, 0, 2, 0),
    )
    return popt


def get_metrics(
    t: np.ndarray, y: np.array, popt: list[np.float64]
) -> dict[str, np.float64]:
    """Вычисление метрик между реальными значениями и моделируемой функцией.

    Args:
        t: Массив значений времени.
        y: Массив значений ряда.
        popt: Список коэффициентов, которые подставляются в функцию.

    Returns:
        Словарь с метриками.
    """
    mae = mean_absolute_error(y, func(t, *popt))
    mape = mean_absolute_percentage_error(y, func(t, *popt))
    mdae = median_absolute_error(y, func(t, *popt))
    mse = mean_squared_error(y, func(t, *popt))
    r2 = r2_score(y, func(t, *popt))

    return {"mae": mae, "mape": mape, "mdae": mdae, "mse": mse, "r2": r2}


def func(t, c_1, a_1, c_2, a_2, c_3, a_3):
    """Моделируемая функция - сумма трех экспонент."""
    return (
        np.multiply(c_1, np.exp(-a_1 * t))
        + np.multiply(c_2, np.exp(-a_2 * t))
        + np.multiply(c_3, np.exp(-a_3 * t))
    )


def calc_kvkz(popt_1, popt_2):
    """
    popt_1: (C_1, A_1, C_2, A_2, C_3, A_3)
    popt_2: (C_4, A_4, C_5, A_5, C_6, A_6)
    kvkz = abs(A_5/A_2)
    """
    return np.abs(popt_2[3] / popt_1[3])


def calc_kst(popt_1, popt_2):
    """
    popt_1: (C_1, A_1, C_2, A_2, C_3, A_3)
    popt_2: (C_4, A_4, C_5, A_5, C_6, A_6)
    kst = abs(A_4/A_1)
    """
    if np.abs(popt_1[1]) < np.abs(popt_1[3]) < np.abs(popt_1[5]) and np.abs(
        popt_2[1]
    ) < np.abs(popt_2[3]) < np.abs(popt_2[5]):
        return np.abs(popt_2[1] / popt_1[1])
    return None
