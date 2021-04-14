import pandas as pd
import numpy as np

def import_csv(filename):
    data = pd.read_csv (filename)
    print (data.head())
    print (data.index)
    print (data.info)

import_csv("Starbucks satisfactory survey.csv")


