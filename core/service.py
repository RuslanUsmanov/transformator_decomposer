import numpy as np
import pandas as pd

from core.decompose import get_coefficients


class DataHandler:
    def __init__(self):
        self.__data = None
        self.R = 352.8

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: pd.DataFrame):
        self.__data = data
        self.__data.set_index("time", inplace=True)
        self.__data["dataset"] = (
            self.__data["dataset"] - self.__data.min(axis=0)["dataset"]
        )

        self.__data = self.__data * (2000 / self.R)

    def read_from_file(self, filename):
        self.data = pd.read_csv(
            filename,
            sep=r"\s+",
            names=["time", "dataset"],
            dtype={"time": np.float64, "dataset": np.float64},
        )

    def get_coefficients(self):
        return get_coefficients(t=self.__data.index, y=self.__data["dataset"])
