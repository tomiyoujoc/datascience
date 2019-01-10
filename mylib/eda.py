# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

def count_missing_values(data):
    return data.isna().sum()
