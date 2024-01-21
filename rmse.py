"""
This module contains the following function thats claculates rmse as loss

"""
import numpy as np


def rmse(predictions, targets):
    """
    Argunments : predicted values and actual targets.
    output: Root squared mean error.
    """
    pred = np.array(predictions)
    tar = np.array(targets)
    mse = np.mean((pred - tar)**2)
    return np.sqrt(mse)
    