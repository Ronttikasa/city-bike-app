import os
import pandas as pd
from .. import db

dirname = os.path.dirname(__file__)
data_file_path = os.path.join(dirname, "..", "..", "..", "data")

def import_journeys(filename):
    file_path = os.path.join(data_file_path, filename)
    df = pd.read_csv(file_path)

    if not df.empty:
        df.rename(columns={"Covered distance (m)": "Distance", "Duration (sec.)": "Duration"}, inplace=True)
        df.drop(columns=["Departure station name", "Return station name"], inplace=True)

        index_filter = df[(df["Distance"] < 10) | (df["Duration"] < 10)].index
        df.drop(index_filter, inplace=True)

        df.to_sql(
            "journeys",
            db.engine, 
            index=False,
            chunksize=10000, 
            if_exists="append")
        return True
    return False