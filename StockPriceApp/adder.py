import pandas as pd
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
# or: requests.get(url).content


securities = pd.read_csv(
    "https://archives.nseindia.com/content/equities/EQUITY_L.csv")

securities.to_csv("securities.csv", index=False)

resp = urlopen(
    "https://archives.nseindia.com/content/historical/EQUITIES/2022/MAR/cm30MAR2022bhav.csv.zip")
zipfile = ZipFile(BytesIO(resp.read()))
zipfile.namelist()

bhavcopy = pd.read_csv(zipfile.open('cm30MAR2022bhav.csv'))
bhavcopy.to_csv("bhavcopy.csv", index=False)
