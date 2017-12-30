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

print(
    "\n=======================\n"
    "    DATA Overview\n"
    "=======================\n"
    "Size of Data: {:d}\n"
    "Zero Transction Amount {:d}\n"
    "Zero Loan Amount {:d}\n"
    "Num. of Lenders:{:d}, \n\t Num. of \"* Undisclosed\" {:d}\n"
    "Num. of property_type {:d}\n"
    .format(
        data.shape[0],
        data.transaction_amount.value_counts()[0],
        data.loan_amount.value_counts()[0],
        data.lender.nunique(),
        data.lender.value_counts()['* Undisclosed'],
        data.property_type.nunique()
    )
)

"""
Now draw plot to look at different distribution of data. Using NumPy and Matplotlib.
    Transaction amount: ta
    Loan amount: la
    Lender: ld (might have long tail)
    Transaction data: td
    Property type: pt
    Year built: yb
    Square foot: sf
"""

# Transaction amount:
np_ta = data.as_matrix(columns=["transaction_amount"])\
            .transpose()

ta_min, ta_max = np.amin(np_ta), np.amax(np_ta)

print(np_ta)
print(np_ta.shape)

