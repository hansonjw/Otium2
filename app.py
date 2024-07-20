import os
import read_write
import finance

# Environment variables
S3_LOC = os.environ.get("S3_LOC", "./")

FILENAME = "fin_all.csv"

df = finance.get_raw_dataframe_all()
read_write.write_dataframe_to_file(df, S3_LOC, FILENAME)