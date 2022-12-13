import os
import pandas as pd

dirname = os.path.dirname(__file__)
data_file_path = os.path.join(dirname, "..", "..", "data", "Helsingin_ja_Espoon_kaupunkipyöräasemat_avoin.csv")

df = pd.read_csv(data_file_path)

print(df.columns)