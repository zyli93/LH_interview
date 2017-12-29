import os, sys
import pandas as pd
import numpy as np

"""
Preprocessing the data

"""

DATA_DIR = "./data/"
RAW_DATA_FILE = DATA_DIR + "data.csv"

# Check if data dir or file exist
if not os.path.exists(DATA_DIR) \
    or not os.path.exists(RAW_DATA_FILE):
    print(
        "CANNOT find {} or {}".format(DATA_DIR, RAW_DATA_FILE),
        file=sys.stderr
    )
    sys.exit()

# Load csv data
raw_data = pd.read_csv(RAW_DATA_FILE)

# Columns that we think useful
COLS = [
            "property_id",
            "transaction_amount",
            "loan_amount",
            "lender",
            "transaction_date",
            "property_type",
            "year_built",
            "sqft"
        ]

data = raw_data[COLS]

print("""
=======================
    DATA Overview
=======================
Size of Data: {:d}
Num. of Lenders: {:d}, Num. of "* Undisclosed" {:d}



""".format(
    data.shape[0],
    data.lender.nunique()), data.)



