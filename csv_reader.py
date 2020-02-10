# Reads the contents of a csv and converts it into a numpy array.

import csv
import numpy as np


def getInput() -> np.ndarray:
    dataList = []

    with open("input.csv", "r") as file:
        reader = csv.reader(file)
        dataList = list(reader)

    return np.array(dataList, dtype=np.double)
