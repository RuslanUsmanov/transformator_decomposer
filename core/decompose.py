import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import (
    mean_absolute_error,
    mean_absolute_percentage_error,
    mean_squared_error,
    median_absolute_error,
    r2_score,
)


class FuncCoefficients:
    def __init__(
        self,
        c_1: float,
        a_1: float,
        c_2: float,
        a_2: float,
        c_3: float,
        a_3: float,
    ) -> None:
        self.c_1 = c_1
        self.c_2 = c_2
        self.c_3 = c_3
        self.a_1 = a_1
        self.a_2 = a_2
        self.a_3 = a_3

    def unpack(self):
        return (self.c_1, self.a_1, self.c_2, self.a_2, self.c_3, self.a_3)


def get_coefficients(t: np.array, y: np.array) -> FuncCoefficients:
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
    return FuncCoefficients(*popt)


def get_metrics(
    t: np.ndarray, y: np.array, coeffs: FuncCoefficients
) -> dict[str, np.float64]:
    """Вычисление метрик между реальными значениями и моделируемой функцией.

    Args:
        t: Массив значений времени.
        y: Массив значений ряда.
        coeffs: Объект с коэффициентами, которые подставляются в функцию.

    Returns:
        Словарь с метриками.
    """
    mae = mean_absolute_error(y, func(t, *coeffs.unpack()))
    mape = mean_absolute_percentage_error(y, func(t, *coeffs.unpack()))
    mdae = median_absolute_error(y, func(t, *coeffs.unpack()))
    mse = mean_squared_error(y, func(t, *coeffs.unpack()))
    r2 = r2_score(y, func(t, *coeffs.unpack()))

    return {"mae": mae, "mape": mape, "mdae": mdae, "mse": mse, "r2": r2}


def func(t, c_1, a_1, c_2, a_2, c_3, a_3):
    """Моделируемая функция - сумма трех экспонент.

    f(t) = c_1 * e^(-a_1 * t) + c_2 * e^(-a_2 * t) + c_3 * e^(-a_3 * t)
    """
    return (
        np.multiply(c_1, np.exp(-a_1 * t))
        + np.multiply(c_2, np.exp(-a_2 * t))
        + np.multiply(c_3, np.exp(-a_3 * t))
    )


def calc_kvkz(norm: FuncCoefficients, short: FuncCoefficients):
    """Вычисление коэффициента Квкз.

    Args:
        norm: Коэффициенты штатного режима.
        short: Коэффициенты режима короткого замыкания.

    Returns:
        Коэффициент Квкз.
    """
    k_c1 = (norm.c_1 - short.c_1) * 100 / norm.c_1
    k_c2 = (norm.c_2 - short.c_2) * 100 / norm.c_2
    k_c3 = (norm.c_3 - short.c_3) * 100 / norm.c_3
    k_a1 = (norm.a_1 - short.a_1) * 100 / norm.a_1
    K_vkz = np.sqrt(k_c1**2 + k_c2**2 + k_c3**2 + k_a1**2)
    return K_vkz


def calc_kst(norm: FuncCoefficients, short: FuncCoefficients):
    """Вычисление коэффициента Кст.

    Args:
        norm: Коэффициенты штатного режима.
        short: Коэффициенты режима короткого замыкания.

    Returns:
        Коэффициент Кст.
    """
    k_a2 = (norm.a_2 - short.a_2) * 100 / norm.a_2
    k_a3 = (norm.a_3 - short.a_3) * 100 / norm.a_3
    k_st = np.sqrt(k_a2**2 + k_a3**2)
    return k_st
