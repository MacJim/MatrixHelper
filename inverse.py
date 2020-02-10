import numpy as np

import csv_reader


inputMatrix = csv_reader.getInput()
inverseMatrix = np.linalg.inv(inputMatrix)
print("Original matrix:\n", inputMatrix)
print("Inverse matrix:\n", inverseMatrix)
