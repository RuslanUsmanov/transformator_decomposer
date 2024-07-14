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
    popt, _ = curve_fit(
        f=_func,
        xdata=t,
        ydata=y,
        p0=(2, 0, 2, 0, 2, 0),
    )
    return popt


def get_metrics(
    t: np.ndarray, y: np.array, popt: list[np.float64]
) -> dict[str, np.float64]:
    mae = mean_absolute_error(y, _func(t, *popt))
    mape = mean_absolute_percentage_error(y, _func(t, *popt))
    mdae = median_absolute_error(y, _func(t, *popt))
    mse = mean_squared_error(y, _func(t, *popt))
    r2 = r2_score(y, _func(t, *popt))

    return {"mae": mae, "mape": mape, "mdae": mdae, "mse": mse, "r2": r2}


def _func(t, c_1, a_1, c_2, a_2, c_3, a_3):
    """Моделируемая функция - сумма трех экспонент."""
    return (
        np.multiply(c_1, np.exp(a_1 * t))
        + np.multiply(c_2, np.exp(a_2 * t))
        + np.multiply(c_3, np.exp(a_3 * t))
    )
