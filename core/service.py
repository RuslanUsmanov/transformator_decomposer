import os
from enum import Enum

import numpy as np
import pandas as pd

from core.decompose import get_coefficients, get_metrics
from core.parameters import SourceParams


class DataSet:
    def __init__(self):
        self.__dataset = None
        self.dataset_scaled = None

    def __len__(self):
        return len(self.__dataset)

    @property
    def dataset(self):
        return self.__dataset

    @dataset.setter
    def dataset(self, data: pd.DataFrame):
        self.__dataset = data
        self.__dataset["dataset"] = (
            self.__dataset["dataset"] - self.__dataset.min(axis=0)["dataset"]
        )

    def refresh_current(self, params: SourceParams):
        self.__dataset["I, A"] = self.__dataset["dataset"] * (
            params.K_u / params.R_meas
        )

    def scale_dataset(
        self,
        params: SourceParams,
        from_points: int = None,
        to_points: int = None,
    ):
        if not from_points or not to_points:
            from_points = 0
            to_points = len(self.__dataset)
        self.dataset_scaled = self.__dataset.iloc[from_points:to_points] * (
            params.K_u / params.R_meas
        )

    def get_coefficients(self):
        return get_coefficients(
            t=self.dataset_scaled["time"],
            y=self.dataset_scaled["dataset"],
        )

    def get_metrics(self, popt):
        return get_metrics(
            t=self.dataset_scaled["time"],
            y=self.dataset_scaled["dataset"],
            popt=popt,
        )


class PlotType(str, Enum):
    SCATTER = "scatter"
    PLOT = "plot"


class Plot:
    def __init__(
        self,
        x: np.array,
        y: np.array,
        label: str = "",
    ):
        self.x = x
        self.y = y
        self.label = label


def read_data_from_files(filenames: list[str]) -> dict[str, DataSet]:
    datasets = {}
    for filename in filenames:
        data = pd.read_csv(
            filename,
            sep=r"\s+",
            names=["time", "dataset"],
            dtype={"time": np.float64, "dataset": np.float64},
        )
        dataset = DataSet()
        dataset.dataset = data
        filename_bare = os.path.basename(filename).split(".")[0]
        datasets[filename_bare] = dataset
    return datasets
