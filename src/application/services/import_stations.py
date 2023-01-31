import os
import pandas as pd
from .. import db

dirname = os.path.dirname(__file__)
data_file_path = os.path.join(dirname, "..", "..", "..", "data", 
    "Helsingin_ja_Espoon_kaupunkipyöräasemat_avoin.csv")

def import_stations():
    """Import station data from csv file.
    """
    df = pd.read_csv(data_file_path)

    if not df.empty:
        df.to_sql(
            "stations",
            db.engine,
            index=False,
            if_exists="replace")

        sql = """ ALTER TABLE stations ADD PRIMARY KEY ("FID") """
        db.session.execute(sql)
        return True
    return False
